# Audit Documentation

## 1. README Audit Table

| Claim made in README | True? | Evidence or correction made |
| :--- | :--- | :--- |
| Requires `pip install -r requirements.txt` | No | No requirements.txt exists; standard library only. Delete the line. |
| Calculates the factorial of a number using NumPy. | No | `factorial.py` uses a standard iterative `for` loop, not the NumPy library. Removed mention of NumPy. |
| Calculates the Fibonacci sequence based on interactive command-line user input. | No | `fibonacci.py` has a hardcoded value of `n = 10`. Corrected to state it uses a hardcoded variable. |
| Requires Python 3.8+. | Yes | `struct.py` uses the `@dataclass` decorator, which requires Python 3.7+. Kept as a valid requirement. |

## 2. Commit Comparison Table

| Commit | My message | AI message | Which is clearer, and why? |
| :--- | :--- | :--- | :--- |
| **1** | Using Python, created a program that can calculate factorial for a number n. | feat: add iterative loop to factorial.py | The AI message is clearer. It follows the conventional commit format, is concise, and stays under the 50-character limit. |
| **2** | Python program for calculating fibonacci sequence for a number n. | feat: add fibonacci.py | The AI message is clearer. It is much more concise and immediately states the exact file and feature added without unnecessary words. |
| **3** | Python program for storing name, roll number and marks in a struct data type like. | feat: add student struct program | The AI message is clearer. It uses standard commit conventions, is punchy, and removes the trailing, incomplete thought at the end of the manual message. |

## 3. Partner Review Notes
**Reviewed by:** Jainam
*   **factorial.py:** The loop logic is sound, but consider adding inline comments to explain how the step of `-1` works in the `range()` function.
*   **fibonacci.py:** Works perfectly. 
*   **struct.py:** Great use of `@dataclass`. Suggested formatting the `marks` float to two decimal places instead of one for better precision.
