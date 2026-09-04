# ==============================================================================
#  Organization : TINITIATE TECHNOLOGIES PVT LTD
#  Website      : tinitiate.com
#  Script Title : Python Tutorial
#  Description  : Using Locks To Avoid Contention
#  Author       : Team Tinitiate
# ==============================================================================



from threading import Thread, Lock
import time

class ThreadSafeCommonResource:
    "this is a class that provides a file and file writing function"

 # The function Print2Console to make it synchronized,
 # must accept a LOCK TYPE parameters
    def Print2Console(self, message, lock):

        # CREATE A LOCK, Using the lock object 
        # (this is a common object across all the threads)
        lock.acquire()

        # Do the Processing
        for c in range(3):
            time.sleep(1) # This causes the program to PAUSE for 1 Sec
            print(message)

        # RELEASE the LOCK, Using the lock object 
        # (this is a common object across all the threads)
        lock.release()
# End of Class

# Create a common LOCK object for all the threads
# Create ONE Objects for the class
# The same object will run as 3 threads
ts_ObjRunner =  ThreadSafeCommonResource()

lock = Lock()

# We have 3 messages to print one for each thread
AAA_message="A"
BBB_message="B"
CCC_message="C"

# start the Thread to write to file
t1 = Thread( target=ts_ObjRunner.Print2Console, args=[AAA_message, lock,])
t2 = Thread( target=ts_ObjRunner.Print2Console, args=[BBB_message, lock,])
t3 = Thread( target=ts_ObjRunner.Print2Console, args=[CCC_message, lock,])

# Start each of the thread
t1.start()
t2.start()
t3.start()

# Wait for the threads to complete
t1.join()
t2.join()
t3.join()

# Here using the LOCK, the output is consistent and as expected
# there is no contention, but the flip side is performance is lowered 
# on using the LOCK synchronization.
