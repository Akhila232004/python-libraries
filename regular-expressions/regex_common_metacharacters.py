# ==============================================================================
#  Organization : TINITIATE TECHNOLOGIES PVT LTD
#  Website      : tinitiate.com
#  Script Title : Python Tutorial
#  Description  : Common metacharacters demonstration
#  Author       : Team Tinitiate
# ==============================================================================



import re

text = "Hello world! 123 cats, 45 dogs. Price: $100. File: data.csv"

# 1. .  (any character except newline)
print(re.findall(r"H.llo", text))   # ['Hello']

# 2. ^  (start of string)
print(re.findall(r"^Hello", text))  # ['Hello']

# 3. $  (end of string)
print(re.findall(r"csv$", text))    # ['csv']

# 4. *  (0 or more)
print(re.findall(r"ca*t", "ct cat caaat"))  # ['ct', 'cat', 'caaat']

# 5. +  (1 or more)
print(re.findall(r"ca+t", "ct cat caaat"))  # ['cat', 'caaat']

# 6. ?  (0 or 1)
print(re.findall(r"colou?r", "color colour"))  # ['color', 'colour']

# 7. {n}  (exactly n times)
print(re.findall(r"\d{3}", text))  # ['123', '100']

# 8. {n,}  (n or more)
print(re.findall(r"\d{2,}", text))  # ['123', '45', '100']

# 9. {n,m}  (between n and m)
print(re.findall(r"\d{2,3}", text))  # ['123', '45', '100']

# 10. []  (character class)
print(re.findall(r"[aeiou]", text))  # ['e', 'o', 'o', 'a', 'i', 'e', 'a', 'a']

# 11. [^ ]  (negated class)
print(re.findall(r"[^0-9\s]", "A1 B2"))  # ['A', 'B']

# 12. \d  (digit)
print(re.findall(r"\d+", text))  # ['123', '45', '100']

# 13. \D  (non-digit)
print(re.findall(r"\D+", "123abc456"))  # ['abc']

# 14. \w  (word characters)
print(re.findall(r"\w+", text))  # ['Hello', 'world', '123', 'cats', '45', 'dogs', 'Price', '100', 'File', 'data', 'csv']

# 15. \W  (non-word characters)
print(re.findall(r"\W+", text))  # [' ', '! ', ' ', ', ', ' ', '. ', ': $', '. ']

# 16. \s  (whitespace)
print(re.findall(r"\s+", text))  # [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']

# 17. \S  (non-whitespace)
print(re.findall(r"\S+", "Hi 123"))  # ['Hi', '123']

# 18. \b  (word boundary)
print(re.findall(r"\bcat\b", "The cat sat on scatter."))  # ['cat']

# 19. \B  (not a word boundary)
print(re.findall(r"\Bcat\B", "educate bobcat scatter"))  # ['cat', 'cat']

# 20. |  (OR)
print(re.findall(r"cat|dog", "cat dog mouse"))  # ['cat', 'dog']

# 21. ()  (grouping)
print(re.findall(r"(ca)+t", "cat cacat"))  # ['ca', 'ca']

# 22. (?: )  (non-capturing group)
print(re.findall(r"(?:ab)+", "abababc"))  # ['ababab']

# 23. (?P<name> )  (named group)
match = re.search(r"(?P<price>\d+)", text)
print(match.group("price"))  # 123 (first match)

# 24. (?= )  (lookahead)
print(re.findall(r"\d+(?= cats)", text))  # ['123']

# 25. (?! )  (negative lookahead)
print(re.findall(r"\d+(?! cats)", text))  # ['12', '45', '100']

# 26. (?<= )  (lookbehind)
print(re.findall(r"(?<=\$)\d+", text))  # ['100']

# 27. (?<! )  (negative lookbehind)
print(re.findall(r"(?<!\$)\d+", text))  # ['123', '45', '00']
