from LinkedQFile import *
from arrayQFile import *

if __name__ == '__main__':
    #Function trollkarl game
    def trollkarl(test):
        order = raw_input('Which order? Answer by , in between the cards ') # The solution 7,1,12,2,8,3,11,4,9,5,13,6,10
        try:
            order = order.split(',')
            order = list(map(int,order)) #Make list of str to list of int
            q = test() #creates an object of given class
            for i in order:
                q.enqueue(i)

            while q.isEmpty() == False:
                    x = q.dequeue()
                    q.enqueue(x) #First card places last
                    y = q.dequeue() #Removes the next card
                    print y

        except ValueError:
            print 'Not a correct input'
            trollkarl()

def main():
    trollkarl(ArrayQ)
    trollkarl(LinkedQ)
main()