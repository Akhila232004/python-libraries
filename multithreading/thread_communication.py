# ==============================================================================
#  Organization : TINITIATE TECHNOLOGIES PVT LTD
#  Website      : tinitiate.com
#  Script Title : Python Tutorial
#  Description  : Thread Communication
#  Author       : Team Tinitiate
# ==============================================================================



from threading import Thread, Event
import time

# Create a function that is common to all threads
def Print3Times(message, event ):
    " This is a function that prints the input message THREE times"

    # Put a wait on the thread if the wait_flag is "1"
    # This will create a blocking state
    print("Message from Print3Times:")
    print("-------------------------")
    print("Pausing this thread, wait() called ")
    print("Wait will be over in 3 Secs by the ")
    event.wait()

    #Print a message three times
    for c in range(3):
        print("Print3Times Message: ", message)
# End of function Print3Times

# Create the common event object
event = Event()

# Create a messages to print
AAA_message = "A"

# Run the function as a thread
t1 = Thread( target=Print3Times
            ,args=(AAA_message, event ))
t1.setName("t1")
# Reset the wait_flag variable, so that the next thread doesn't wait
wait_flag = 0

# Start the event
t1.start()

# Sleep for 3 Secs
time.sleep(3) 

def setBlockers(event):
    " This releases all blockers"
    print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    print("Message from setBlockers: All waits are set(), continue execution..")
    print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    event.set()

# Create another thread, to set(), resume all blocking threads
t2 = Thread( target=setBlockers
            ,args=(event, ))

# Start the event
t2.start()

# Make sure all threads execute before code execution
t1.join()
t2.join()
