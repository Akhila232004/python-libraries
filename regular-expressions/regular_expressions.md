![Python Tinitiate Image](../../python_tinitiate.png)

# Python Tutorial
&copy; TINITIATE.COM

##### [Back To Contents](../../README.md)

# Regular Expressions
* Regular expressions are string patterns to search in other strings.
* Regular expressions functionality is provided by the `re` module.
* The `re` module provides all the functions required to enable regular expressions.
* Regular expressions is all about matching a "pattern" in a "string".

## Regex Basic Functions
Python regular expressions basic functions includes the following:
### match() Function
* `match()` function, looks for a match only at the beginning of the string, returns true or false for the match found/not found.
```python
import re

# Create a test string with repeating letters/words
test_string = "The Test string 123 121212 tinitiate TINITIATE a1b2c3"

# Search for match: The
match = re.search(r'The',test_string)

if match:
    print("Word 'The' is found in beginning of string:", "\n", test_string)
else:
    print("Word 'The' is NOT found in beginning of  string:", "\n", test_string)
```
### search() Function
* `search()` function, returns true or false for the string found/not found.
```python
import re

# Create a test string with repeating letters/words
test_string = "The Test string 123 121212 tinitiate TINITIATE a1b2c3"

# Search for pattern: tinitiate (in small letters)
match = re.search(r'tinitiate',test_string)

if match:
    print("The word 'tinitiate' is found in the string:", "\n", test_string)
else:
    print("The word 'tinitiate' is NOT found in the string:", "\n", test_string)


# Search for more complicated patterns, search for 12*, where *
# is wildcard character which matches everything else after the pattern "12"
match = re.search(r'12*',test_string)

if match:
    print("The word '12*' is found in the string:", "\n", test_string)
else:
    print("The word '12*' is NOT found in the string:", "\n", test_string)
```
### findall() Function
* `findall()` function, returns a tuple of all occurrences of the pattern.
```python
import re

# Prints all the words with a small "t" in the test-string
# The options are:
# word with a "t" in between `\w+t\w+`,
# OR indicated by the PIPE symbol `|`
# word with a "t" as the last character `\w+t`,
# OR indicated by the PIPE symbol `|`
# word with a "t" as the first character `t\w+`,

# Create a test string with repeating letters words
test_string = "The Test string 123 121212 tinitiate TINITIATE a1b2c3"

all_t = re.findall(r'\w+t\w+|\w+t|t\w+',test_string)

# The re.findall returns a TUPLE and we print all the elements looping
# through the TUPLE
for lpr in all_t:
    print(lpr)
```
### sub() Function
* `sub()` function is used to replace parts of strings, with a pattern.
```python
import re

# This is used to replace parts of strings, with a pattern
string = "Tinitiate good python examples"

# Replace "good" with "great"
new_string = re.sub("good", "great", string)
print(string)
print(new_string)
```
### split() Function
* `split()` function separates a string by space or any delimeter.
```python
import re

words2list = re.split(r's','Tinitiate good python examples')
print(words2list)

# Split a Comma Separated String
csv2list = re.split(r',','1,AAA,2000')
print(csv2list)
```

## Common Regex Metacharacters
| Symbol | Meaning | Example Match |
|--------|----------|---------------|
| `.`    | Any single character (except newline) | `a.c` → `"abc"`, `"axc"` |
| `^`    | Start of string | `^Hello` → `"Hello world"` |
| `$`    | End of string | `world$` → `"Hello world"` |
| `*`    | 0 or more repetitions | `ab*` → `"a"`, `"ab"`, `"abb..."` |
| `+`    | 1 or more repetitions | `ab+` → `"ab"`, `"abb..."` |
| `?`    | 0 or 1 repetition (optional) | `colou?r` → `"color"`, `"colour"` |
| `{n}`  | Exactly n times | `\d{3}` → `"123"` |
| `{n,}` | n or more times | `\d{2,}` → `"12"`, `"1234"` |
| `{n,m}`| Between n and m times | `\d{2,4}` → `"12"`, `"123"`, `"1234"` |
| `[]`   | Character class (any inside) | `[aeiou]` → `"a"`, `"e"` |
| `[^ ]` | Negated class (not inside) | `[^0-9]` → `"a"`, `"@"` |
| `\d`   | Digit `[0-9]` | `\d+` → `"123"` |
| `\D`   | Non-digit | `\D+` → `"abc"` |
| `\w`   | Word char `[A-Za-z0-9_]` | `\w+` → `"Hello123"` |
| `\W`   | Non-word char | `\W+` → `"@#$"` |
| `\s`   | Whitespace (space, tab, newline) | `\s+` → `"   "` |
| `\S`   | Non-whitespace | `\S+` → `"word"` |
| `\b`   | Word boundary | `\bcat\b` → `"cat"` not `"scatter"` |
| `\B`   | Not a word boundary | `\Bcat\B` → `"educate"` |
| `\|`   | OR (alternation) | `cat\|dog` → `"cat"`, `"dog"` |
| `()`   | Grouping / capture | `(ab)+` → `"ab"`, `"abab"` |
| `(?: )`| Non-capturing group | `(?:ab)+` → `"ab"`, `"abab"` |
| `(?P<name> )` | Named group | `(?P<num>\d+)` → captures digits into group `num` |
| `(?= )` | Lookahead (match if followed by) | `\d(?=px)` → `"5"` in `"5px"` |
| `(?! )` | Negative lookahead | `\d(?!px)` → `"5"` in `"5kg"` |
| `(?<= )` | Lookbehind (match if preceded by) | `(?<=\$)\d+` → `"100"` in `"$100"` |
| `(?<! )` | Negative lookbehind | `(?<!\$)\d+` → `"100"` not preceded by `$` |

```python
# Regex common metacharacters demonstration
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
print(re.findall(r"\d+(?! cats)", text))  # ['12', 45', '100']

# 26. (?<= )  (lookbehind)
print(re.findall(r"(?<=\$)\d+", text))  # ['100']

# 27. (?<! )  (negative lookbehind)
print(re.findall(r"(?<!\$)\d+", text))  # ['123', '45', '00']
```

## Using Regex
### Multiple pattern matching in words of a given string.
```python
import re

my_string = 'Hour01 Min22 VOIDDDDD Sec29 BLAH min3erere Hour32 OTHERS Min33 Hour32'

# Word pattern 'starts with'
# From 'my_string' find all words starting with 'H'
starting_h = re.findall(r'\bH+\w+.\b', my_string)

for word in starting_h:
    print(word)

# Word pattern 'ends with'
# From 'my_string' find all words ending with '2'
ending_2 = re.findall(r'\b\w+2\b', my_string)

for word in ending_2:
    print(word)

# Word pattern 'has pattern in between'
# From 'my_string' find all words those have '3' in them
has_3 = re.findall(r'\w*3\w*', my_string)

for c in has_3:
    print(c)

# Word pattern with multiple patterns (using an pattern1 OR pattern2)
# From 'my_string' find all words those have 'ou' OR 'OI' in them
has_3 = re.findall(r'\w*OI\w*|\w*ur\w*', my_string)

for c in has_3:
    print(c)
```
### Multiple pattern matching in a given string.
```python
import re

# String pattern match with 'exact word'
# Print 'my_string' if exact word 'Hour32' is found in it
my_string = 'Hour01 Min22 VOIDDDDD Sec29 BLAH min3erere Hour32 OTHERS Min33 Hour32'

Hour32 = re.search('Hour32', my_string)
if Hour32:
    print(my_string)
    
# String pattern 'starts with'
# Print 'my_string' if it starts with 'H'
starting_h = re.search('H*$', my_string)

if starting_h:
    print(my_string)

# String pattern 'ends with'
# Print 'my_string' if string ends with '2'
ending_2 = re.search('2$', my_string)

if ending_2:
    print(my_string)

# String with multiple Patterns (using an pattern1 OR pattern2)
# Print 'my_string' if there are words with 'ou' OR 'OI' in them
has_OIur = re.search('OI|ur', my_string)

if has_OIur:
    print(my_string)
```
### Multiple pattern matching with metacharacters
```python
import re

# Matches any single character using '.'
# ------------------------------------------------------------------------------
TargetString = "ABCDEFG"
RegExPattern = "B(.)D"
ReplaceString = "BXD"
retValue = re.sub(RegExPattern, ReplaceString, TargetString)
print(retValue)
# OUTPUT: ABXDEFG


# Matches START of line '^'
# ------------------------------------------------------------------------------
TargetString = " is a line."
RegExPattern = "^"
ReplaceString = "Here"
retValue = re.sub(RegExPattern, ReplaceString, TargetString)
print(retValue)
# OUTPUT: Here is a line.


# Matches END of line '$'
# ------------------------------------------------------------------------------
TargetString = "This is a "
RegExPattern = "$"
ReplaceString = "line"
retValue = re.sub(RegExPattern, ReplaceString, TargetString)
print(retValue)
# OUTPUT: This is a line


# Matches any single character in brackets. [...]
# ------------------------------------------------------------------------------
TargetString = "SAT SIT SET"
RegExPattern = "S[AI]T"
ReplaceString = "SXT"
retValue = re.sub(RegExPattern, ReplaceString, TargetString)
print(retValue)
# OUTPUT: SXT SXT SET


# Matches any single character NOT in brackets. [^...]
# ------------------------------------------------------------------------------
TargetString = "SAT SIT SET"
RegExPattern = "S[^AI]T"
ReplaceString = "SXT"
retValue = re.sub(RegExPattern, ReplaceString, TargetString)
print(retValue)
# OUTPUT: SAT SIT SXT


# Matches Beginning of entire string '\\A'
# ------------------------------------------------------------------------------
TargetString = "there was PASCAL"
RegExPattern = "\\A"; # Using the Escape Character "\"
ReplaceString = "Once upon a time "
retValue = re.sub(RegExPattern, ReplaceString, TargetString)
print(retValue)
# OUTPUT: Once upon a time there was PASCAL


# Matches End of entire string except valid final line terminator CAPS(Z)'\\Z'
# ------------------------------------------------------------------------------
TargetString = "there was \n"
RegExPattern = "\\Z"            # Using the Escape Character "\"
ReplaceString = "PASCAL."
retValue = re.sub(RegExPattern, ReplaceString, TargetString)
print(retValue)
# OUTPUT: there was 
#         PASCAL.


# Matches 0 or more occurrences of preceding expression. '*'
# ------------------------------------------------------------------------------
TargetString = "JA is Cool, JAJA is Cool"
RegExPattern = "J*"
ReplaceString = "JAVA"
retValue = re.sub(RegExPattern, ReplaceString, TargetString)
print(retValue)
# OUTPUT: JAVAAJAVA JAVAiJAVAsJAVA JAVACJAVAoJAVAoJAVAlJAVA,JAVA 
#         JAVAAJAVAAJAVA JAVAiJAVAsJAVA JAVACJAVAoJAVAoJAVAlJAVA


# Matches 1 or more of the preceding expression. '+'
# ------------------------------------------------------------------------------
TargetString = "JA is Cool, JAJA is Cool"
RegExPattern = "J+"
ReplaceString = "JAVA"
retValue = re.sub(RegExPattern, ReplaceString, TargetString)
print(retValue)
# OUTPUT: JAVAA is Cool, JAVAAJAVAA is Cool


# Matches 0 or 1 occurrence of preceding expression. '?'
# ------------------------------------------------------------------------------
TargetString = "JA is Cool, JAJA is Cool"
RegExPattern = "J?"
ReplaceString = "JAVA"
retValue = re.sub(RegExPattern, ReplaceString, TargetString)
print(retValue)
# OUTPUT: JAVAAJAVA JAVAiJAVAsJAVA JAVACJAVAoJAVAoJAVAlJAVA,JAVA
#         JAVAAJAVAAJAVA JAVAiJAVAsJAVA JAVACJAVAoJAVAoJAVAlJAVA


# Matches exactly n number of occurrences of preceding expression.'exp{n}'
# ------------------------------------------------------------------------------
TargetString = "avav av avavav avavavavavav"
RegExPattern = "(av){2}"
ReplaceString = "JAVA"
retValue = re.sub(RegExPattern, ReplaceString, TargetString)
print(retValue)
# OUTPUT: JAVA av JAVAav JAVAJAVAJAVA


# Matches n or more occurrences of preceding expression. 'exp{n,}'
# ------------------------------------------------------------------------------
TargetString = "avav av avavav avavavavavav"
RegExPattern = "(av){2,}"
ReplaceString = "JAVA"
retValue = re.sub(RegExPattern, ReplaceString, TargetString)
print(retValue)
# OUTPUT: JAVA av JAVA JAVA


# Matches exactly n occurrences and m times,of preceding expression.'exp{n,m}'
# ------------------------------------------------------------------------------
TargetString = "avav av avavav avavavavavav"
RegExPattern = "(av){2,2}"
ReplaceString = "JAVA"
retValue = re.sub(RegExPattern, ReplaceString, TargetString)
print(retValue)
# OUTPUT: JAVA av JAVAav JAVAJAVAJAVA


# Matches X OR Y. 'X|Y'
# ------------------------------------------------------------------------------
TargetString = "ERLANG is great"
RegExPattern = "(ERLANG|SCALA)"
ReplaceString = "JAVA"
retValue = re.sub(RegExPattern, ReplaceString, TargetString)
print(retValue)
# OUTPUT: JAVA is great


# Matches word characters '\\w'
# ------------------------------------------------------------------------------
TargetString = "Java is great"
RegExPattern = "(\\w)"
ReplaceString = "JAVA"
retValue = re.sub(RegExPattern, ReplaceString, TargetString)
print(retValue)
# OUTPUT: JAVAJAVAJAVAJAVA JAVAJAVA JAVAJAVAJAVAJAVAJAVA


# Matches NON word characters '\\W'
# ------------------------------------------------------------------------------
TargetString = "Java is great"
RegExPattern = "(\\W)"
ReplaceString = "JAVA"
retValue = re.sub(RegExPattern, ReplaceString, TargetString)
print(retValue)
# OUTPUT: JavaJAVAisJAVAgreat


# Matches whitespace. Equivalent to [\t\n\r\f]. '\\s'
# ------------------------------------------------------------------------------
TargetString = "Java is        great"
RegExPattern = "(\\s)"
ReplaceString = "JAVA"
retValue = re.sub(RegExPattern, ReplaceString, TargetString)
print(retValue)
# OUTPUT: JavaJAVAisJAVAJAVAJAVAJAVAJAVAJAVAJAVAJAVAgreat


# Matches NON whitespace. NOT Equivalent to [\t\n\r\f]. '\\S'
# ------------------------------------------------------------------------------
TargetString = "Java is        great"
RegExPattern = "(\\S)"
ReplaceString = "JAVA"
retValue = re.sub(RegExPattern, ReplaceString, TargetString)
print(retValue)
# OUTPUT: JAVAJAVAJAVAJAVA JAVAJAVA        JAVAJAVAJAVAJAVAJAVA


# Matches digits. Equivalent to [0-9]. '\\d'
# ------------------------------------------------------------------------------
TargetString = "Java is Number 1 !!"
RegExPattern = "(\\d)"
ReplaceString = "one"
retValue = re.sub(RegExPattern, ReplaceString, TargetString)
print(retValue)
# OUTPUT: Java is Number one !!


# Matches NON digits. '\\D'
# ------------------------------------------------------------------------------
TargetString = "1a2b3"
RegExPattern = "(\\D)"
ReplaceString = "JAVA"
retValue = re.sub(RegExPattern, ReplaceString, TargetString)
print(retValue)
# OUTPUT: 1JAVA2JAVA3
```

##### [Back To Contents](../../README.md)
***
| &copy; TINITIATE.COM |
|----------------------|