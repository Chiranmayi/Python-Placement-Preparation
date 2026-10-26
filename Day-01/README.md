# Day 1 — Python Fundamentals & Problem Solving

**Placement Preparation Series — Python Developer Interview Notes**

- Name:S.Chiranmayi
- Date: 26 October 2026
- Day: 1

## 1. Coding Problem — First Non-Repeating Character

### Approach

1. Remove spaces from the input string.
2. Create an empty dictionary to store the frequency of each character.
3. Traverse the string and increment each character's count using `dict.get()`.
4. Traverse the string again in its original order.
5. Return the first character whose frequency is `1`.
6. If no unique character exists, return a suitable message.

The solution is case-sensitive, so uppercase and lowercase characters are treated differently.

### Code

```python
def first_non_repeating(text):
    text = text.replace(" ", "")
    freq = {}

    # Count the frequency of each character
    for char in text:
        freq[char] = freq.get(char, 0) + 1

    # Find the first character that appears once
    for char in text:
        if freq[char] == 1:
            return char

    return "No non-repeating character found"


print(first_non_repeating("programming"))
print(first_non_repeating("aabbcdd"))
print(first_non_repeating("aabbcc"))
```

### Test Inputs and Outputs

| Input | Expected output |
|---|---|
| `"programming"` | `p` |
| `"aabbcdd"` | `c` |
| `"aabbcc"` | No non-repeating character found |
| `"a b c"` | `a` |
| `"Aa"` | `A` |
| `""` | No non-repeating character found |
| `"   "` | No non-repeating character found |
| `"a"` | `a` |

### Time and Space Complexity

- **Time complexity:** O(n), because the algorithm makes two passes through the string.
- **Auxiliary space complexity:** O(k), where k is the number of distinct non-space characters stored in the dictionary.

Here, n is the length of the input string.

## 2. Concept Question — Python Data Structures

### List vs Tuple vs Set vs Dictionary

| Feature | List | Tuple | Set | Dictionary |
|---|---|---|---|---|
| Ordered | Yes | Yes | No positional order | Yes |
| Duplicates | Allowed | Allowed | Not allowed | Keys must be unique |
| Mutable | Yes | No | Yes | Yes |
| Main use | Ordered collections | Fixed records | Unique values | Key-value mapping |
| Example | `[1, 2, 2]` | `(10, 20)` | `{1, 2}` | `{"name": "Ravi"}` |

### Scenario 1: Store Unique Student IDs

I would use a **set** because it stores unique values and supports efficient average-case membership checks.

```python
student_ids = {101, 102, 103, 101}
print(student_ids)
```

The duplicate ID `101` is stored only once.

### Scenario 2: Store Student Profile Fields

I would use a **dictionary** because student details can be stored as key-value pairs.

```python
student = {
    "name": "Ravi",
    "email": "ravi@example.com",
    "phone": "9999999999"
}

print(student["name"])
print(student.get("grade", "Not assigned"))
```

The dictionary allows values to be accessed by meaningful keys.

## 3. Debugging Challenge — Student Search

### Issue

The original code prints `"Student not found"` for every student who does not match `"Kiran"`. The `else` belongs to the `if` inside the loop, so it executes for every nonmatching student, even when Kiran appears later.

### Fixed Code

```python
students = ["Ravi", "Anil", "Kiran", "Suresh"]

for student in students:
    if student == "Kiran":
        print("Student found:", student)
        break
else:
    print("Student not found")
```

### Explanation

The `break` statement exits the loop as soon as Kiran is found. The `for/else` block executes its `else` only if the loop finishes without encountering `break`.

This ensures that exactly one correct message is printed.

Time complexity: O(n) in the worst case.
Auxiliary space complexity:O(1), excluding the input list.

## 4. What I Learned

- I learned about Python's built-in data types and the difference between mutable and immutable objects.
- I understood how lists, tuples, sets, and dictionaries differ and when to use each.
- I learned how to use dictionaries for character frequency counting.
- I practised writing functions, using loops, and handling edge cases.
- I understood the difference between `==` and `is`, and the purpose of `break`, `continue`, and `pass`.
- I learned how to explain time and space complexity.
- I understood how the `for/else` construct helps solve a search problem correctly.

## 5. What I Found Difficult

I initially found it challenging to understand how a dictionary can count character frequencies efficiently and how to find the first non-repeating character without using `count()` repeatedly.



## Conclusion

Day 1 helped me strengthen my Python fundamentals and problem-solving approach. I learned to choose appropriate data structures, write readable code, test edge cases, debug logically, and explain the complexity of my solutions.
