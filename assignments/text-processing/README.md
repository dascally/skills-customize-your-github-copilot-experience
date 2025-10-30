```markdown
# 📘 Assignment: Python Text Processing

## 🎯 Objective

Practice working with strings, file I/O, and basic text manipulation in Python. Students will build small utilities to analyze and transform text files.

## 📝 Tasks

### 🛠️ Analyze a text file

#### Description
Write a Python script that reads a plain text file, summarizes its contents, and produces a small report with counts and the most common words.

#### Requirements
Completed program should:

- Read input from a text file using proper file I/O (handle missing or empty files gracefully)
- Normalize text (case-insensitive) and strip basic punctuation
- Count total words and unique words
- Produce a list of the top 5 most frequent words with counts
- Write a short report to a new output file (e.g., `<input>-report.txt`) and print a concise summary to the console

### 🛠️ Text transformation (optional extension)

#### Description
Add a function to perform a simple find-and-replace across the file and save the transformed text to a new file.

#### Requirements
Completed extension should:

- Accept a target string and replacement string
- Perform a case-insensitive replacement while preserving case of unchanged text where reasonable
- Save the transformed file with a clear filename (e.g., `<input>-replaced.txt`)

---

### Example usage

```
$ python3 starter-code.py sample.txt
Input: sample.txt
Total words: 78
Unique words: 54
Top 5 words:
  the — 8
  and — 5
  to — 4
  of — 4
  a — 3
Report written to: sample-report.txt
```

Tip: A starter script `starter-code.py` and `sample.txt` are provided in this folder. Use them as a scaffold and extend the functionality for extra credit.

``` 
