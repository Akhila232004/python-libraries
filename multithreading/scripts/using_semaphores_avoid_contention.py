# ==============================================================================
#  Organization : TINITIATE TECHNOLOGIES PVT LTD
#  Website      : tinitiate.com
#  Script Title : Python Tutorial
#  Description  : Using Semaphores To Avoid Contention
#  Author       : Team Tinitiate
# ==============================================================================



from threading import Thread, Semaphore
import time

def Print2ConsoleSemaphore(message, semaphore):

    # CREATE A semaphore, Using the semaphore object 
    # (this is a common object across all the threads)
    semaphore.acquire()

    # Do the Processing
    for c in range(3):
        time.sleep(1) # This causes the program to PAUSE for 1 Sec
        print(message)

    # RELEASE the semaphore, Using the semaphore object 
    # (this is a common object across all the threads)
    semaphore.release()

# Run the above function in Three threads
semaphore = Semaphore()

# We have 3 messages to print one for each thread
AAA_message="A"
BBB_message="B"
CCC_message="C"

# start the Thread to write to file
t1 = Thread( target=Print2ConsoleSemaphore, args=[AAA_message, semaphore,])
t2 = Thread( target=Print2ConsoleSemaphore, args=[BBB_message, semaphore,])
t3 = Thread( target=Print2ConsoleSemaphore, args=[CCC_message, semaphore,])

# Start each of the thread
t1.start()
t2.start()
t3.start()

# Wait for the threads to complete
t1.join()
t2.join()
t3.join()
