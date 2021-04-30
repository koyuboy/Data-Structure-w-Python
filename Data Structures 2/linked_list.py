class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Can be used with only Node class. LinkedList class is not necessery.


class LinkedList:
    def __init__(self):
        self.head = None

    def insertAtBegining(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def inserAfter(self,node,data):

        if node is None:
            print("Given previous node can not be None!")
            return

        new_node = Node(data)
        new_node.next = node.next
        node.next = new_node
    
    def insertAtEnd(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        
        last_node = self.head
        while last_node.next:
            last_node = last_node.next

        last_node.next = new_node


    def deleteNode(self, key):
        if self.head is None:
            return
        
        temp_node = self.head
        
        if temp_node.data == key:
            self.head = self.head.next
            return


        while temp_node is not None:
            if temp_node.data == key:
                break
            prev = temp_node
            temp_node = temp_node.next
        
        if temp_node is None:
            return
        
        prev.next = temp_node.next




    def sizeOfList(self):
        temp_head = self.head
        size=0
        while temp_head:
            size+=1
            temp_head = temp_head.next
        return size


    def printList(self):
        temp_node = self.head
        while temp_node:
            print(str(temp_node.data), end=" ")
            temp_node = temp_node.next
        print("\n")



if __name__ == '__main__':

    llist = LinkedList()

    llist.head = Node(1)
    second = Node(2)
    third = Node(3)

    #connect
    llist.head.next = second
    second.next = third
    
    print("Original list")
    llist.printList()

    print("Insert 0 at beginning")
    llist.insertAtBegining(0)
    llist.printList()

    print("Insert 11 after 1")
    llist.inserAfter(llist.head.next, 11)
    llist.printList()

    print("Insert 4 at the end")
    llist.insertAtEnd(4)
    llist.printList()


    print("Size of list: ", llist.sizeOfList())

    print("Delete 11")
    llist.deleteNode(11)
    llist.printList()
    
