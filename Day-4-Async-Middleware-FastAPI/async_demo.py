import asyncio
import time


async def fetch_data(name, delay):
    print(f"Fetching {name}...")

    await asyncio.sleep(delay)

    print(f"{name} completed")

    return f"{name} data received"


async def sequential_execution():

    start = time.perf_counter()

    result1 = await fetch_data("Profile", 2)
    result2 = await fetch_data("Notifications", 2)
    result3 = await fetch_data("Recommendations", 2)

    end = time.perf_counter()

    print("\nSequential Results:")
    print(result1)
    print(result2)
    print(result3)

    print("Sequential Time:", round(end - start, 2), "seconds")


async def concurrent_execution():

    start = time.perf_counter()

    results = await asyncio.gather(
        fetch_data("Profile", 2),
        fetch_data("Notifications", 2),
        fetch_data("Recommendations", 2)
    )

    end = time.perf_counter()

    print("\nConcurrent Results:")

    for result in results:
        print(result)

    print("Concurrent Time:", round(end - start, 2), "seconds")


async def main():

    await sequential_execution()

    print("\n--------------------------\n")

    await concurrent_execution()


if __name__ == "__main__":
    asyncio.run(main())