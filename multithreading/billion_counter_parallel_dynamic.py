# ==============================================================================
#  Organization : TINITIATE TECHNOLOGIES PVT LTD
#  Website      : tinitiate.com
#  Script Title : Python Tutorial
#  Description  : Billion Counter Parallel Execution Dynamic Thread Count
#  Author       : Team Tinitiate
# ==============================================================================



import datetime
from threading import Thread 

print("Parallel Dynamic Billion Counter Start", datetime.datetime.now())
data = {}

def count_large_num(i_thread_id, i_st, i_end):

    c = 0
    for i in range(i_st, i_end+1):
        c+=1
    data[i_thread_id] = c

n=5
target = 1000000000

# Create a Threads List
threads = []
threshold = target/n

l_st = 0
l_ed = 0

# Create n Threads
for threadID in range(n):

    l_st = l_ed + 1
    l_ed = l_ed + threshold
    
    t = Thread(target=count_large_num, args=(threadID,int(l_st),int(l_ed), ))
    t.start()
    threads.append(t)

# Join all threads
for t in threads:
    t.join()
    
print(data)
res = 0
for i in data.values():
   res += i

print(res)   
print("Parallel Dynamic Billion Counter End", datetime.datetime.now())
# OUTPUT:
# Parallel Dynamic Billion Counter Start 2025-09-08 12:50:55.326818
# {0: 200000000, 4: 200000000, 1: 200000000, 2: 200000000, 3: 200000000}
# 1000000000
# Parallel Dynamic Billion Counter End 2025-09-08 12:51:29.312450
