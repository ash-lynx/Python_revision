"""Stack and queue implemented using linked list."""

#--------------------------------------------------------------------------
class Node(object):
    """Initialize a node and next node pointer for linked list."""
    
    def __init__(self, initdata):
        self.data = initdata
        self.next_node = None
        
#--------------------------------------------------------------------------        
class Stack(object):
    """Implement stack using linked list."""
    
    def __init__(self):
        self.head = None
        
    def push(self, item):
        """Push the item on the top of the stack"""
        node = Node(item)
        node.next_node = self.head
        self.head = node
            
    def pop(self):
        """Pop and return the item on the top of the stack."""
        if not self.is_empty():
            item = self.head.data
            self.head = self.head.next_node
            return item
        else:
            raise IndexError("The stack is empty.")
        
    def peek(self):
        """Return the item on the top of stack without removing it"""
        if not self.is_empty:
            item = self.head.data
            return item
        else:
            raise IndexError("The stack is empty.")
        
    def is_empty(self):
        """Return true if the stack is empty."""
        return self.head is None
    
    def __len__(self):
        """Return the number of items in the stack"""
        count = 0
        current_node = self.head
        
        while not current_node is None:
            count += 1
            current_node = current_node.next_node
            
        return count
    
    def __str__(self):
        """Print all the itmes in the stack"""
        current_node = self.head
        string = "Items in the stack starting from the top is: "
        while not current_node is None:
            string += str(currend_node.data) + " -> "
            current_node = current_node.next_node
        string += "None"
        return srting
    
#--------------------------------------------------------------------------
class Queue(object):
    """Implement queue using linked list."""
    
    def __init__(self):
        self.head = None
        self.tail = None
        
    def enqueue(self, item):
        """Add the item to the tail of the queue."""
        node = Node(item)
        
        if not self.tail is None:
            self.tail.next_node = node
            self.tail = node
        else:
            self.tail = node
            self.head = node
            
    def dequeue(self):
        """Pop and return the item from the front of the queue"""
        if not is_empty():
            item = self.head.data
            self.head = self.head.next_node
            return item
        else:
            raise IndexError("The queue is empty.")
        
    def is_empty(self):
        """Return true if the queue is empty"""
        return self.head is None
    
    def __len__(self):
        """Return the number of items in the queue"""
        count = 0
        current_node = self.head
        
        while not current_node is None:
            count += 1
            current_node = current_node.next_node
        
        return count
    
    def __str__(self):
        """Print out all the items in the queue"""
        current_node = self.head
        string = "Items in the queue starting from the head is: "
        
        while not current_node is None:
            string += str(current_node.data) + " -> "
            current_node = current_node.next_node
            
        string += "None"
        return string
    
        
    
    