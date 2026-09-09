# ==============================================================================
#  Organization : TINITIATE TECHNOLOGIES PVT LTD
#  Website      : tinitiate.com
#  Script Title : Python Tutorial
#  Description  : Create Threads Using The `threading` Module
#  Author       : Team Tinitiate
# ==============================================================================



from threading import Thread
import time

# Create a function that takes FIVE seconds to execute
# `sleep()` pauses the program for FIVE seconds
def five_seconds_process(thread_id):
    "This function when called takes 5 Seconds to execute"
    # Thread Start message
    print("ThreadID: ",thread_id," Started at: ", time.time())
    for c in range(5):
        print("thread_id: ", thread_id," Iteration Number ", c+1)
        time.sleep(1) # This causes the program to PAUSE for 1 Sec
    # Thread END message
    print("ThreadID: ",thread_id," Ended at: ", time.time())

# Create a Thread Object using the Thread class of the threading module
t1 = Thread(target=five_seconds_process, args=(1,))
t1.start()

# Create one more Thread Object using the Thread class of the threading module
t2 = Thread(target=five_seconds_process, args=(2,))
t2.start()
