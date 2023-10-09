import time
from package.observer import Observer


SEND_REPORT_EVERY = 60


if __name__ == '__main__':

    observer = Observer(interval=SEND_REPORT_EVERY)
    observer.start()