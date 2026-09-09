# ==============================================================================
#  Organization : TINITIATE TECHNOLOGIES PVT LTD
#  Website      : tinitiate.com
#  Script Title : Python Tutorial
#  Description  : Counter()
#  Author       : Team Tinitiate
# ==============================================================================



from collections import Counter

# Count Elements in a String
c = Counter('ABCDABCABA')
print(c)

# Count Words in a Sentence
s = 'Python is cool Java is great SQL is cool and great'
words = s.split()
c = Counter(words)
print(c)

# Count elements in a List
L1 = [1,2,3,4,2,3,4,3,4,4]
c = Counter(L1)
print(c)

# Get Most Common using most_common([n])
# Here we get the Top 2 most common occurances of the List elements
L1 = [1,2,3,4,2,3,4,3,4,4]
c = Counter(L1).most_common(2)
print(c)

# Remove Elements using Subtract
L1 = [1,2,3,4,2,3,4,3,4,4]
c = Counter(L1)
L_Remove = {4:2, 3:1}
c.subtract(L_Remove)
print(c)

#  Elements, Is used to convert a Counter to List
L1 = [1,2,3,4,2,3,4,3,4,4]

# Create Counter
c = Counter(L1)

# Use element to convert counter to List
print(sorted(c.elements()))
