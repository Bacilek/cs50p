import re

email = input("Email: ")

"""
!   . : any char except for '\n'
!   * : 0+ repetitions
!   + : 1+ repetitions
!   ? : 0 or 1 repetition
!   {m} : m repetitions
!   {m, n} : m-n repetitions 
!   ^ : start of the string
!   $ : end of the string
!   [] : set of characters (anything from brackets)
!   [^] : complementing the set (anything but not complement in brackets)
?   \w : word char [a-zA-Z0-9_]
?   \w : not a word char
?   \d : decimal digit [0-9]
?   \d : not a decimal digit
?   \s : whitespace char
?   \S : not a whitespace char
*   | : or
*   (...) : a group, capture (return)
*   (?:...) : non-capturing group (no return)
    re.IGNOTECASE
    re.MULTILINE
    re.DOTALL
"""


if re.search(r"^\w+@(\w+\.)?\w+\.edu$", email, re.IGNORECASE):  # r -> raw -> '\' doesn't lead to any escape sequence, just escaping one char
    print("valid")

# re.match(pattern, string, flags) -> same, but automatically matches from the start of the string (no ^ needed)
# re.fullmatch(pattern, stron, flags) -> same, but autoamtically matches from the start to the end of the strin (no ^ and $ needed)