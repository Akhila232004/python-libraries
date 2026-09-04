# ==============================================================================
#  Organization : TINITIATE TECHNOLOGIES PVT LTD
#  Website      : tinitiate.com
#  Script Title : Python Tutorial
#  Description  : deque()
#  Author       : Team Tinitiate
# ==============================================================================



import collections

# initializing deque
dq = collections.deque([1,2,3])

# Add Element on the Right, using append
dq.append(4)

# Add Element on the left, using appendleft()
dq.appendleft(6)

print (dq)

# Remove Element from Right
dq.pop()

# Remove Element from Left
dq.popleft()

print (dq)
