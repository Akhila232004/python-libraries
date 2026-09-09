# ==============================================================================
#  Organization : TINITIATE TECHNOLOGIES PVT LTD
#  Website      : tinitiate.com
#  Script Title : Python Tutorial
#  Description  : Thread Contention Scenario
#  Author       : Team Tinitiate
# ==============================================================================



# Create a shared resource a 'print to screen' method 
# Required for sleep operation
from threading import Thread 
import time

# THREAD UNSAFE EXECUTION SCENARIO: where there is no Order of printing messages

# * This is a class `commonResource` a function prints a message  
#   to SCREEN three times, waiting a second in-between the PRINT.
# * We run the CLASS-Function three times in THREE Threads.
# * The output is not consistent and overlaps
# * This is because the common resource (the Print3Times function)
#   is not locked or synchronized 

class commonResource:
    "this is a class that provides a file and file writing function"
    def Print3Times(self, message):
        for c in range(3):
            print(message)
            time.sleep(1) # This causes the program to PAUSE for 1 Sec
# End of Class

# Create 3 Objects for the class
# each object will run the same function as a single thread
ObjRunner =  commonResource();

# We have 3 messages to print one for each thread
AAA_message="A"
BBB_message="B"
CCC_message="C"

# start the Thread to write to file
t1 = Thread( target=ObjRunner.Print3Times
            ,args=(AAA_message,))

t2 = Thread( target=ObjRunner.Print3Times
            ,args=(BBB_message,))

t3 = Thread( target=ObjRunner.Print3Times
            ,args=(CCC_message,))

# Start each of the thread
t1.start()
t2.start()
t3.start()

# Wait for the threads to complete
t1.join()
t2.join()
t3.join()

# Note that output is not in order and is inconsistent, as same print statement 
# is being used by all the threads
