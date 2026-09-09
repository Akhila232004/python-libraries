# ==============================================================================
#  Organization : TINITIATE TECHNOLOGIES PVT LTD
#  Website      : tinitiate.com
#  Script Title : Python Tutorial
#  Description  : Create Threads Using The `_thread` Module
#  Author       : Team Tinitiate
# ==============================================================================



import _thread
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

print("Demonstration of THREADS using the _thread module's start_new_thread function")

# Run five_seconds_process function as a THREAD with a THREAD-ID 1
_thread.start_new_thread(five_seconds_process,(1,))

# Run five_seconds_process function as a THREAD with a THREAD-ID 2
_thread.start_new_thread(five_seconds_process,(2,))

# This is needed, because all the threads will exit, if main program finishes
# in order to keep the program alive we make the program execute for 5 seconds
# This infact is running 3 Threads including the time.sleep(5) below
time.sleep(5)
