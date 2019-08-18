# packet:
import threading

# create thread and assign to the variable:
# daemon thread means it will die when the main thread returns
t_var = thrading.Thread(target=thread_function, args=(arg1, ...), daemon=True/False)

# mutual exclusion:
# the Lock object sth like mutex at FreeRTOS
# if one thread takes it and doesn't give back, the program will stuck
l = threading.Lock()
l.aquire() # blocks until Lock is released
l.release()

threading.RLock() # multiple-take lock

# other:
threading.Semaphore
threading.Timer
threading.Barrier - wait for specified number of threads - i.e. for initialization, makes sure all threads do it before running

# packet:
import logging 

# set log level
logging.getLoger().setLevel(logging.DEBUG/WARNING)
format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO,
                        datefmt="%H:%M:%S")

