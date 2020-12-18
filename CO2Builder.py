"""
Appannie backend intern homework
Build co2 molecule from carbon threads and oxygen threads
"""
from threading import Thread
from queue import Queue


class Barrier:
    def __init__(self):
        self.c_store = list()
        self.o_store = list()

    def builder(self):
        while True:
            if q.get() == 'start':
                break
        atom = q.get()
        while atom != 'end':
            if atom == 'C':
                self.c_store.append('C')
            elif atom == 'O':
                self.o_store.append('O')
            atom = q.get()

            if self.checker() == True:
                print(''.join(self.c_store.pop(0) + self.o_store.pop(0) + self.o_store.pop(0)),end='')

    def checker(self):
        if len(self.c_store) >= 1 and len(self.o_store) >= 2:
            return True
        else:
            return False


class Stream:
    def __init__(self, s):
        self.source = s

    def start(self):
        q.put('start')
        for atom in self.source:
            if atom == 'C' or atom == 'O':
                q.put(atom)
        q.put('end')
        return 0


if __name__ == "__main__":
    s = input()
    q = Queue()
    stream = Stream(s)
    barrier = Barrier()

    t1 = Thread(target=stream.start, args=())
    t2 = Thread(target=barrier.builder, args=())

    t1.start()
    t2.start()
    t1.join()
    t2.join()