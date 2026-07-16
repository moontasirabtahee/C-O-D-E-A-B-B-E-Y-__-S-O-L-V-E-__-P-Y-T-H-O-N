# 🏛️ CodeAbbey Solutions — Python

> **20 CodeAbbey problems** solved in Python — from basic arithmetic to bracket balancing, covering input parsing, math, string processing, and algorithmic challenges.

---

## 📋 Table of Contents

- [Repository Overview](#-repository-overview)
- [Statistics Dashboard](#-statistics-dashboard)
- [Problem Solutions](#-problem-solutions)
  - [Arithmetic & Basics](#-arithmetic--basics-problems-1-6)
  - [Applied Math & Formulas](#-applied-math--formulas-problems-7-12)
  - [Algorithms & Logic](#-algorithms--logic-problems-13-20)
- [Techniques & Patterns Used](#-techniques--patterns-used)
- [Solution Highlights](#-solution-highlights)
- [How to Run](#-how-to-run)

---

## 🔬 Repository Overview

```
┌──────────────────────────────────────────────────────────────────────┐
│                    CODEABBEY PYTHON SOLUTIONS                       │
│                                                                      │
│   Platform: CodeAbbey.com        Language: Python                    │
│   Total Problems: 20             Input: stdin                        │
│                                                                      │
│   ┌──────────────┐  ┌──────────────┐  ┌──────────────┐             │
│   │  Arithmetic  │  │ Applied Math │  │  Algorithms  │             │
│   │   & Basics   │  │  & Formulas  │  │   & Logic    │             │
│   │   #1 – #6    │  │  #7 – #12    │  │  #13 – #20   │             │
│   └──────────────┘  └──────────────┘  └──────────────┘             │
│                                                                      │
│   All solutions read from stdin and print to stdout                  │
│   (competitive programming style)                                    │
└──────────────────────────────────────────────────────────────────────┘
```

---

## 📊 Statistics Dashboard

```
CATEGORY DISTRIBUTION                    DIFFICULTY PROGRESSION
══════════════════════                    ═══════════════════════

  Arithmetic     ██████████████████  6     #1──#6   ████░░░░░░  Basic
  Applied Math   ██████████████████  6     #7──#12  ██████░░░░  Intermediate
  Algorithms     ████████████████████████  8     #13─#20  ████████░░  Advanced

  INPUT PATTERN BREAKDOWN
  ═══════════════════════
  Single-line input:     ████  #1, #15, #17
  N + N lines:           ████████████████████  #3-#12, #16, #18-#20
  Interactive/loop:      ████  #14
```

---

## 📂 Problem Solutions

### 🔢 Arithmetic & Basics (Problems #1–#6)

```
BASIC I/O WIREFRAME
══════════════════════════════════════════════════════════

  INPUT PATTERN (Problems 2-6):
  ┌──────────────────────────────────┐
  │ Line 1: N (number of test cases)│
  │ Line 2: a₁ b₁ [c₁]             │
  │ Line 3: a₂ b₂ [c₂]             │
  │ ...                              │
  │ Line N+1: aₙ bₙ [cₙ]           │
  └──────────────────────────────────┘
              │
              ▼
  ┌──────────────────────────────────┐
  │ Process each line               │
  │ → store result in outList       │
  │ → print all results space-sep   │
  └──────────────────────────────────┘
```

| # | Problem Name | Description | Key Code |
|---|-------------|-------------|----------|
| 1 | Sum of Two | Add two numbers | `a + b` |
| 2 | Sum in Loop | Sum of N numbers | `sum(num_list)` |
| 3 | Sums in Loop | Sum pairs across N lines | Loop + `sum()` per line |
| 4 | Minimum of Two | Find min of each pair | Loop + `min()` |
| 5 | Minimum of Three | Find min of each triple | Loop + `min()` |
| 6 | Rounding | Divide and round properly | Custom rounding at 0.5 boundary |

#### Code Pattern (Problems 3–6)

```python
# Standard multi-test-case pattern used throughout
length = int(input())               # Read N
outList = list()
for i in range(length):
    numList = list(map(int, input().split(" ")))
    outList.append(process(numList)) # Process each case

for i in outList:
    print(i, end=" ")              # Output all results
```

---

### 📐 Applied Math & Formulas (Problems #7–#12)

```
APPLIED MATH WIREFRAME
══════════════════════════════════════════════════════════

  #7  FAHRENHEIT → CELSIUS          #8  ARITHMETIC PROGRESSION SUM
  ──────────────────────             ──────────────────────────────
  F = 212°F                         a=1, step=2, n=5
  C = (F - 32) × 5/9               Series: 1, 3, 5, 7, 9
  C = 100°C ✓                       Sum = 1+3+5+7+9 = 25

  #9  TRIANGLE INEQUALITY           #10 LINE THROUGH TWO POINTS
  ──────────────────────             ──────────────────────────────
  a + b > c?                        (x₁,y₁) and (x₂,y₂)
  a + c > b?  ← ALL must hold       slope a = (y₁-y₂)/(x₁-x₂)
  b + c > a?                        intercept b = y₁ - a×x₁

  #11 WEIGHTED DIGIT SUM            #12 TIME DIFFERENCE
  ─────────────────────              ──────────────────────────────
  1234                               day₁ h₁ m₁ s₁ → total_sec₁
  1×1 + 2×2 + 3×3 + 4×4             day₂ h₂ m₂ s₂ → total_sec₂
  = 1 + 4 + 9 + 16 = 30             diff = sec₂ - sec₁
                                     → convert back to d/h/m/s
```

| # | Problem Name | Description | Key Code |
|---|-------------|-------------|----------|
| 7 | Fahrenheit to Celsius | Temperature conversion | `(F - 32) * 5 / 9` |
| 8 | Arithmetic Progression | Sum of AP series | `Sum += first + (i * step)` |
| 9 | Triangle Inequality | Can 3 sides form a triangle? | `a+b>c and a+c>b and b+c>a` |
| 10 | Linear Function | Line equation from 2 points | `a = (y1-y2)/(x1-x2); b = y1-a*x1` |
| 11 | Weighted Digit Sum | Sum of digit × position weight | `digit × position` accumulation |
| 12 | Time Difference | Time span between two timestamps | Convert to seconds → diff → convert back |

---

### 🧠 Algorithms & Logic (Problems #13–#20)

```
ALGORITHM COMPLEXITY WIREFRAME
══════════════════════════════════════════════════════════

  #13 POSITIONAL DIGIT SUM          #14 MODULAR CALCULATOR
  ─────────────────────              ──────────────────────
  "1234"                             total = 15
  1×1 + 2×2 + 3×3 + 4×4             + 7 → 22
  = 30                               * 3 → 66
  (ascending weight factor)          % 5 → 1 (stop & print)

  #17 ARRAY CHECKSUM                 #19 BRACKET MATCHING
  ────────────────────               ──────────────────────
  Input: [a₁, a₂, ..., aₙ]         "({[<>]})"
  result = 0                           ↓ push ( { [ <
  for each aᵢ:                        ↓ pop on ) } ] >
    result = result + aᵢ              ↓ stack empty? → 1 (valid)
    result = result * 113
  output = result % 10000007         "({[<]>})"
                                       ↓ mismatch → 0 (invalid)

  #18 SQUARE ROOT (NEWTON'S)
  ──────────────────────────
  √x using iterative refinement:
  r₀ = 1
  rₙ₊₁ = (rₙ + x/rₙ) / 2
  repeat y times → converges to √x
```

| # | Problem Name | Description | Key Code |
|---|-------------|-------------|----------|
| 13 | Weighted Digit Sum | Digit × ascending position | `int(digit) * position` |
| 14 | Modular Calculator | Apply `+`, `*`, `%` operations | Interactive loop until `%` |
| 15 | Maximum and Minimum | Find max and min of array | `max()`, `min()` |
| 16 | Average of Array | Average of N numbers per line | `sum(array) / len(array)` |
| 17 | Array Checksum | Hash array with multiply-and-add | `(result + x) * 113 % 10000007` |
| 18 | Square Root (Newton's) | Iterative √x approximation | `r = (r + x/r) / 2` |
| 19 | Bracket Matching | Validate balanced brackets | Stack-based `(){}[]<>` matching |
| 20 | Vowel Count | Count vowels in strings | Set membership `in [a,e,i,o,u,y]` |

---

## 🧩 Techniques & Patterns Used

```
┌──────────────────────────────────────────────────────────────────────────┐
│                       TECHNIQUE FREQUENCY MAP                            │
├──────────────────────────────────────────────────────────────────────────┤
│                                                                          │
│  Input Parsing (map/split) ████████████████████████████  All problems    │
│  Loop + Accumulate         ████████████████████████      #2-#8, #11-#17 │
│  Math Formulas             ████████████████              #7-#10, #18    │
│  Conditionals              ██████████████                #6, #9, #14    │
│  List Operations           ████████████████              #2, #4, #5, #15│
│  Digit Manipulation        ████████████                  #11, #13       │
│  Modular Arithmetic        ████████                      #14, #17       │
│  Stack (LIFO)              ██████                        #19            │
│  String Iteration          ██████                        #13, #20       │
│  Numerical Methods         ████                          #18            │
│                                                                          │
└──────────────────────────────────────────────────────────────────────────┘
```

### Pattern Quick Reference

```
╔═══════════════════════╦═══════════════════════════════════════════════════╗
║ Pattern               ║ When Used                                        ║
╠═══════════════════════╬═══════════════════════════════════════════════════╣
║ map(int, split())     ║ Parse space-separated integers from stdin        ║
║ Accumulator Loop      ║ Build result list over N test cases              ║
║ Flag Variable         ║ Track state changes (blocking, matching)         ║
║ Stack (list + pop)    ║ Bracket matching — push open, pop on close       ║
║ Newton's Method       ║ Iterative approximation of square root           ║
║ Modular Arithmetic    ║ Prevent overflow in checksum / calculator        ║
║ Time Conversion       ║ Convert d/h/m/s to seconds for easy diff         ║
║ Linear Algebra        ║ Slope-intercept from two points                  ║
╚═══════════════════════╩═══════════════════════════════════════════════════╝
```

---

## 💡 Solution Highlights

### #19 — Bracket Matching (Stack-Based Validator)

```python
# Classic stack-based balanced bracket checker
# Supports: () {} [] <>
def validate(string):
    checker = []
    for char in string:
        if char in '([{<':
            checker.append(char)       # Push opening brackets
        elif char in ')]}>':
            if not checker:            # Closing without opening
                return 0
            # Match closing with last opening
            expected = {'(':')', '[':']', '{':'}', '<':'>'}
            if expected.get(checker[-1]) == char:
                checker.pop()          # Matched — pop
            else:
                return 0               # Mismatch
    return 0 if checker else 1         # Leftover = invalid
```

### #18 — Square Root via Newton's Method

```python
# Babylonian method / Newton's iteration for √x
# Converges quadratically — doubles correct digits each step
r = 1                    # Initial guess
for i in range(iterations):
    D = x / r            # Division step
    r = (r + D) / 2      # Average step → converges to √x
# After ~20 iterations: machine precision for any x
```

### #17 — Array Checksum (Rolling Hash)

```python
# Multiplicative hash with modular arithmetic
result = 0
for value in array:
    result = result + value
    result = result * 113     # Prime multiplier for dispersion
print(result % 10000007)      # Mod to prevent overflow
```

### #12 — Time Difference (Seconds Conversion)

```python
# Convert timestamp to total seconds → diff → convert back
Start = day1*86400 + hour1*3600 + min1*60 + sec1
End   = day2*86400 + hour2*3600 + min2*60 + sec2
diff  = End - Start

# Decompose back to days/hours/minutes/seconds
day     = diff // 86400
hour    = (diff % 86400) // 3600
minutes = (diff % 3600) // 60
seconds = diff % 60
```

---

## 📁 Directory Structure

```
C-O-D-E-A-B-B-E-Y-__-S-O-L-V-E-__-P-Y-T-H-O-N/
│
├── Problem #1.py       # Sum of Two
├── Problem #2.py       # Sum in Loop
├── Problem #3.py       # Sums in Loop
├── Problem #4.py       # Minimum of Two
├── Problem #5.py       # Minimum of Three
├── Problem #6.py       # Rounding
├── Problem #7.py       # Fahrenheit to Celsius
├── Problem #8.py       # Arithmetic Progression Sum
├── Problem #9.py       # Triangle Inequality
├── Problem #10.py      # Line Through Two Points
├── Problem #11.py      # Weighted Digit Sum (Multiplication)
├── Problem #12.py      # Time Difference
├── Problem #13.py      # Weighted Digit Sum (Positional)
├── Problem #14.py      # Modular Calculator
├── Problem #15.py      # Maximum and Minimum
├── Problem #16.py      # Average of Array
├── Problem #17.py      # Array Checksum
├── Problem #18.py      # Square Root (Newton's Method)
├── Problem #19.py      # Bracket Matching
└── Problem #20.py      # Vowel Count
```

---

## 🚀 How to Run

```bash
# Clone the repository
git clone <repo-url>
cd C-O-D-E-A-B-B-E-Y-__-S-O-L-V-E-__-P-Y-T-H-O-N

# Run with manual input
python "Problem #1.py"
# Then type: 3 5
# Output: 8

# Run with input file (competitive programming style)
echo "3 5" | python "Problem #1.py"

# Or redirect from a file
python "Problem #9.py" < input.txt
```

### Requirements

- **Python 3.x** — No external dependencies
- All solutions use `stdin`/`stdout` (competitive programming format)
- Input format matches [CodeAbbey](https://www.codeabbey.com/) problem specifications

---

> **Platform:** [CodeAbbey.com](https://www.codeabbey.com/) · **Language:** Python 3 · **Author:** Moontasir Abtahee · **Date:** June 2021
