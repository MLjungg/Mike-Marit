from array import array
class ArrayQ:
    def __init__(self):
        self.__queue = array('b',[])

    def __str__(self):
        return str(self.__queue)

    def enqueue(self,item):
        self.__queue.append(item)
        return self.__queue

    def dequeue(self):
        return self.__queue.pop(0)

    def isEmpty(self):
        return len(self.__queue) == 0

'''
    q = ArrayQ()
    q.enqueue(1)
    q.enqueue(2)
    x = q.dequeue()
    y = q.dequeue()
    if (x == 1 and y == 2):
        print("Fungerar")
    else:
        print("Nagot ar fel. 1 och 2 forvantades men vi fick", x, y)
'''
