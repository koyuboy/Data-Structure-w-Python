class Queue:
    def __init__(self):
        self.queue = []
    
    def length(self):
        return len(self.queue)
    
    def isEmpty(self):
        return len(self.queue) == 0

    def getFront(self):
        return self.queue[0]

    def getRear(self):
        return self.queue[-1]
    
    def enqueue(self, element):
        self.queue.append(element)

    def dequeue(self):
        if self.isEmpty():
            return("Queue is empty!")
        else:
            self.queue.pop(0)
    
    def display(self):
        print(self.queue)

#TEST#

q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
q.enqueue(5)

q.display()

q.dequeue()
print(q.getFront())
print(q.getRear())
print("After removing an element")
q.display()