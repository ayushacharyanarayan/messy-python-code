# Messy Python Code Improvement

Takes a messy Python program and refactors it for readability and structure, with help from AI (Cursor AI).

## Files
- `messy_code.py` – the original, hard-to-read version
- `improved_code.py` – the cleaned-up version (same output)

## What was improved
| Before | After |
|---|---|
| Names like `a`, `t`, `m`, `av` | Clear names like `students`, `average`, `topper` |
| Everything in one block | Small functions with one job each |
| Deeply nested if/else for grades | Grade boundaries stored in a list and looped over |
| Data stored as nested lists | Data stored as dictionaries with named keys |
| Manual max tracking | Built-in `max()` |
| No documentation | Docstrings and comments |
| Runs on import | `if __name__ == "__main__"` guard |

## How to run
```
python messy_code.py
python improved_code.py
```
Both print the same result.

## Author
Dimpal Tailor
