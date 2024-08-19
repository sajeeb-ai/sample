class Node:
    def __init__(self,e = 0,n = None):
        self.element = e
        self.next = n

class Queue:
    def __init__(self):
        self.front == None
        self.rear = None
        
    def Enqueue(self,data):
        if self.front == None:
            self.front = self.rear = Node(data)

        else:
            self.rear.next = Node(data)
            self.rear = self.rear.next
    
    def Dequeue(self):
        if self.front != None:
            cur = self.front.element
            self.front = self.front.next
            return cur
        else:
            print("Queue is empty!")
    
    def isEmpty(self):
        if self.front == None:
            return True
        
    
    def size(self):
        count = 0
        cur_node = self.front
        while cur_node != None:
            count += 1
            cur_node = cur_node.next
        return count
    
    def Front(self):
        return self.front.element
    
    def Rear(self):
        return self.rear.element
    
q = Queue()
q.Enqueue(1)  
q.Enqueue(2)   
q.Enqueue(3)
q.Enqueue(4)
