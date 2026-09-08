# Audit Documentation

## 1. README Audit Table

| Claim made in AI README | True? | Evidence or correction made |
| :--- | :--- | :--- |
| `factorial.py` uses the NumPy library. | No | **Correction:** Checked the source code. It uses a standard iterative `for` loop. Removed mention of NumPy. |
| `struct.py` uses `@dataclass` requiring Python 3.7+ | Yes | **Evidence:** The file begins with `from dataclasses import dataclass`. Official Python documentation states the `dataclasses` module was introduced in Python 3.7. |
| `calculator.py` uses the `math` module. | No | **Correction:** The script only uses basic built-in arithmetic (`x + y`). No `import math` exists. Deleted this claim. |
| `prime_checker.py` handles negative numbers automatically. | No | **Correction:** The code only evaluates `if num > 1`. It ignores negative numbers completely rather than handling them. Corrected the description to reflect this. |
| Requires `pip install -r requirements.txt` | No | **Correction:** No external dependencies are imported in any of the six scripts, and no `requirements.txt` file exists in the repo. Deleted this line. |
| Requires Python 3.7+ overall. | Yes | **Evidence:** Because `struct.py` is included in this repository and relies on `@dataclass`, the minimum viable Python version to run the *entire* suite of programs is indeed 3.7+. |

## 2. Commit Comparison Table

| Commit | My original manual message | AI-generated message | Which is clearer, and why? |
| :--- | :--- | :--- | :--- |
| **1** | Using Python, created a program that can calculate factorial for a number n. | `feat: add iterative loop to factorial.py` | AI is clearer. Follows conventional formatting and is concise. |
| **2** | Python program for calculating fibonacci sequence for a number n. | `feat: add fibonacci.py` | AI is clearer. Drops the conversational tone for direct impact. |
| **3** | Python program for storing name, roll number and marks in a struct data type like. | `feat: add student struct program` | AI is clearer. Removes the trailing incomplete thought from my draft. |
| **4** | Wrote a program to do basic addition calculation. | `feat: add basic addition to calculator.py` | AI is clearer. It specifies the exact file modified and standardizes the phrasing. |
| **5** | Code to check if a hardcoded number is a prime number or not. | `feat: add prime number checker script` | AI is clearer. It stays well under the 50-character limit while retaining the core meaning. |
| **6** | Added palindrome check using python string slicing. | `feat: implement palindrome string slicing` | AI is clearer. "Implement" is a stronger imperative verb than "Added," and it omits the redundant word "python." |

## 3. Partner Review Notes
**Reviewed by:** Jainam

*   **factorial.py:** The reverse loop logic works well. Adding a quick inline comment explaining that `-1` is the step parameter in `range(n, 0, -1)` would make it instantly clear to beginners.
*   **fibonacci.py:** Great use of tuple unpacking (`a, b = b, a + b`)! One small fix: add an empty `print()` at the very end of the script so the final tabbed output doesn't bleed into the terminal prompt.
*   **struct.py:** Using `@dataclass` keeps the class definition perfectly clean. Formatting the marks output to one decimal place (`{s1.marks:.1f}`) was a great attention to detail.
