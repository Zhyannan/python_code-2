# coding=utf-8
import threading
import time


class MyThtread(threading.Thread):
    def run(self):
        for i in range(3):
            time.sleep(1)
            msg = "I'm " + self.name + " @ " + str(i)
            print(msg)


if __name__ == '__main__':
    t = MyThtread()
    t.start()
