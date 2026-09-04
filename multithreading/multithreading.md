![Python Tinitiate Image](../../python_tinitiate.png)

# Python Tutorial
&copy; TINITIATE.COM

##### [Back To Contents](../../README.md)

# Multithreading
* Multithreading is the ability to run multiple threads concurrently within a single process.
* Normal execution of python, where each step in the code is executed one after another is run as a single THREAD. But in a multi-threaded application, code (or steps) can be run together with another in parallel (two or more steps at the same time) even though the code is written one after another.
* Such a requirement is very much needed in a variety of applications, such as games, GUI applications, large volume data processing.
* To invoke multithreading features we need to use the threading module.
* The `threading` module provides a way to create and manage threads in Python.
* Here we demonstrate multithreading by
  * Running a function that takes 5 seconds to complete execution using a SLEEP command.
  * We run the function TWICE and it takes 10 Secs to complete the execution in sequential execution.
  * But when we run the same function in TWO threads parallelly then it takes only 5 secs to run both the functions at the same time concurrently.
```python
from threading import Thread 
import time

# Create a function that takes FIVE seconds to execute
# `sleep()` pauses the program for FIVE seconds
def five_seconds_process(thread_id):
    print("ThreadID: ",thread_id," Started at: ", time.time())
    for c in range(5):
        print("thread_id: ", thread_id," Iteration Number ", c+1)
        time.sleep(1) # This causes the program to PAUSE for 1 Sec
    print("ThreadID: ",thread_id," Ended at: ", time.time())

# Sequential Execution
five_seconds_process(1)
five_seconds_process(2)



# Parallel Execution
# Create 2 Threads
# Create a Thread Object using the Thread class of the threading module
t1 = Thread(target=five_seconds_process, args=(1,))
t1.start()

# Create one more Thread Object using the Thread class of the threading module
t2 = Thread(target=five_seconds_process, args=(2,))
t2.start()



# Parallel Execution DYNAMIC THREAD COUNT
# Create a Threads List
threads = []
print("Start")

# Create 5 Threads
for threadID in range(5):
    t = Thread(target=five_seconds_process, args=(threadID+1, ))
    t.start()
    threads.append(t)
print("End Before Join")

# Join all threads, It stops the main program from completing execution before
#  all threads are done executing 
for e in threads:
    e.join()
print("End After Join")
```

## Create Threads Using The `_thread` Module
* Using the `_thread.start_new_thread` we can pass any function and its parameters that we want to run as a parallel thread.
* This function accepts two parameters (1)`Target function` (2)`List of function parameters`
* In this case we want to run the function: `five_seconds_process` and its SINGLE parameter.  Also make sure to include a "COMMA" after the LAST PARAMETER that is being passed to the `_thread.start_new_thread`
```python
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
```

## Create Threads Using The `threading` Module
* The **Thread** class from the **threading** module is another and preferred way to create threads.
* The Thread CLASS constructor accepts a function and its argument list as a tuple.
* When the `OBJECT.start()` function is called, it runs as a thread. 
```python
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
```

## Create Dynamic Number Threads
* Sometimes the number of threads that are needed might depend on volume of process, for such scenarios we can dynamically create threads, using a loop.
* Here we demonstrate creating THREE threads using a for loop and run the same function `five_seconds_process` THRICE using a thread each.
```python
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

# Create a Threads List
threads = []

# Create 3 Threads
for threadID in range(2):
    t = Thread(target=five_seconds_process, args=(threadID+1, ))
    t.start()
    # threads.append(t)

# join all threads
for t in threads:
    t.join()
```

## Billion Counter Example
* Sequential Execution
```python
import datetime

today = datetime.datetime.now()
print("Start",today.strftime("%d-%b-%Y %H:%M:%S"))

a = 0
for c in range(1,1000000001):
    a = a+1

print(a)

today = datetime.datetime.now()
print("End",today.strftime("%d-%b-%Y %H:%M:%S"))
# OUTPUT:
# Start 08-Sep-2025 12:55:07
# 1000000000
# End 08-Sep-2025 12:56:24
```
* Parallel Execution
```python
import datetime
from threading import Thread

today = datetime.datetime.today()
print("Start",today.strftime("%d-%b-%Y %H:%M:%S"))

l_thread_stats = {}
# {1:250000000,2:250000000,3:250000000,4:250000000}
def counter_vals(p_start,p_end,p_thread):
    a = 0
    for c1 in range(p_start,p_end+1):
        a = a+1

    l_thread_stats[p_thread] = a 

# counter_vals(1,250000000,1)
# counter_vals(250000001,500000000,2)
# counter_vals(500000001,750000000,3)
# counter_vals(750000001,1000000000,4)

t1 = Thread(target=counter_vals, args=(1,250000000,1))
t1.start()
t2 = Thread(target=counter_vals, args=(250000001,500000000,2))
t2.start()
t3 = Thread(target=counter_vals, args=(500000001,750000000,3))
t3.start()
t4 = Thread(target=counter_vals, args=(750000001,1000000000,4))
t4.start()

t1.join()
t2.join()
t3.join()
t4.join()

ctr = 0
# l_thread_stats = {1:250000000,2:250000000,3:250000000,4:250000000}
for k,v in l_thread_stats.items():
    ctr = ctr + v

print(ctr)

today = datetime.datetime.today()
print("End",today.strftime("%d-%b-%Y %H:%M:%S"))
# OUTPUT:
# Start 08-Sep-2025 12:50:01
# 1000000000
# End 08-Sep-2025 12:50:35
```
* Parallel Execution Dynamic Thread Count
```python
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
```

## Thread Synchronization
* Threads share memory. Without coordination, you get race conditions (interleaved reads/writes produce wrong results) thread conflict, lost updates, and deadlocks. This is where Thread Synchronization comes in.
* **Thread Contention:** Threads might share the same resource and in such cases there could be various contention issues (who should use the resource first)
    * A resource here could be anything from a variable to a file or any thing that must be used sequentially.
* **Locks:** One solution to overcome this issue is using **Locks**.
    * Locks supports locked and unlocked states, a lock will have **exclusive** access to the shared resource during the lock period, this will prevent contention. 
    * Lock can be acquired using the `acquire()` function and unlock can be issued using `release()` function.
* **Semaphores:** Semaphores are one more mechanism to implement synchronization, `semaphores.acquire()` and `semaphore.release()`
    * They have an internal counter which starts to decrement when an `acquire()` call is made and starts to increment when a `release()` call is made. The counter will never go below zero, but when it is zero, it blocks, waiting for a thread to call the `release()`
    * They are very useful to manage Database connection pools, file writing services and situations where precaution needs to be taken when the shared resource has limited capacity. 
### Thread Contention Scenario
* Here we create a shared resource that will be called THREE times in threads.
```python
# Create a shared resource a 'print to screen' method 
# Required for sleep operation
from threading import Thread 

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
```
### Using Locks To Avoid Contention
* Using the lock mechanism to implement synchronization.
* Re-writing the same above program with locking using `acquire()` and `release()`.
```python
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
```
### Using Semaphores To Avoid Contention
* Using the semaphores to implement synchronization.
* Re-writing the same above program with locking using `semaphore.acquire()` and `semaphore.release()`.
```python
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
```

## Thread Communication
* Python provides mechanisms for threads to communicate with each other.
* **Event** is a communication mechanism between threads.
* A `wait()` call is made to create a blocking thread, **Blocking** whose execution will be halted.
* A `set()` call releases all the blocking threads and continues execution.
* The operations must be for the same event object.
```python
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
```

##### [Back To Contents](../../README.md)
***
| &copy; TINITIATE.COM |
|----------------------|