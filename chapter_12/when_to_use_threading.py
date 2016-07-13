# GIL limit python only run in single thread, not proper to run cpu concentration task
# Better to handle them with mutiple cpu
# But thread is appropriate to use when handling potential blocking muti-task
# like IO / get result from databse these kind of jobs

from threading import Thread

class CountdownThread(Thread):
    def __init__(self, n):
        super(CountdownThread,self).__init__()
        self.n = 0
    def run(self):
        while self.n > 0:
            print('T-minus', self.n)
            self.n -= 1
            time.sleep(5)

c = CountdownThread(5)
c.start()