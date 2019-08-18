import logging
import threading
import time

def thread_fun(name):
    logging.info('Thread %s started', name)
    time.sleep(2)
    logging.info('Thread %s finishing', name)

if __name__ == "__main__":
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO, datefmt="%H:%M:%S")

    logging.info("Main:     before creating a thread")
    x = threading.Thread(target=thread_fun, args=(1,), daemon=True)
    logging.info("Main:     before running a thread")
    x.start()
    logging.info("Main:     Waiting for thread to finish")
    x.join()
    logging.info("Main:     all done")
    
