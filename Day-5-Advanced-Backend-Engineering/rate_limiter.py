
import time
from collections import defaultdict, deque

from fastapi import HTTPException, Request, status


# Maximum 5 requests in 60 seconds
MAX_REQUESTS = 5
TIME_WINDOW = 60

# Store request timestamps for each client
request_history = defaultdict(deque)


async def rate_limit(request: Request):
    client_ip = request.client.host if request.client else "unknown"

    current_time = time.time()
    requests = request_history[client_ip]

    # Remove expired request timestamps
    while requests and current_time - requests[0] >= TIME_WINDOW:
        requests.popleft()

    # Check request limit
    if len(requests) >= MAX_REQUESTS:
        raise HTTPException(
            status_code=status.HTTP_429_TOO_MANY_REQUESTS,
            detail="Too many requests. Please try again later.",
            headers={"Retry-After": str(TIME_WINDOW)}
        )

    # Record current request
    requests.append(current_time)
