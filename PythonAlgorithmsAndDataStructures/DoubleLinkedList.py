from __future__ import print_function
class Node:
    def __init__(self, data, prev=None, next=None):
        self.data=data
        self.prev=None
        self.next=None

class DoubleLinkedList:
    def __init__(self, data=None):
        self.head=self.tail=None
        if data is not None:
            self.head=self.tail=Node(data)
            
    def append(self, data):
        node=Node(data, None, None)
        if self.head is None:
            self.head=self.tail=node
        else:
            node.prev=self.tail
            self.tail.next=node
            self.tail=node
        print("Added item ", node.data)
            
    def show(self):
        node=self.head
        printString=''
        while node is not None:
            if node==self.tail:
                printString+=str(node.data)
            else:
                printString+=str(node.data)+' <-> '
            node=node.next
        print(printString)
        return printString
    def length(self):
        node=self.head
        treeLength=0
        while node is not None:
            treeLength+=1
            node=node.next
        return treeLength

    def remove(self, item):
        node=self.head
        if node is not None:
            while node is not None:
                if node.data==item:
                    if node==self.head and node==self.tail:
                        self.head=None
                        self.tail=None
                    elif node==self.head:
                        self.head=node.next
                        if node.next is not None:
                            node.next.prev=node.prev
                    elif node==self.tail:
                        self.tail=node.prev
                        if node.prev is not None:
                            node.prev.next=node.next
                    else:
                        node.next.prev=node.prev
                        node.prev.next=node.next
                    print("Removed item", node.data)
                    removedNode=node
                    del removedNode
                node=node.next   
        else:
            print("List empty, unable to remove item", item)
            





    
