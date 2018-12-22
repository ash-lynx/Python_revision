"""Stack using Python list and linked list."""

#--------------------------------------------------------------------------
class Stack(object):
    """Implement stack using Python list."""
    
    def __init__(self):
        self._items = []
        
    def push(self, item):
        """Push the item to the top of the stack."""
        self._items.append(item)
        
    def pop(self):
        """Pop and return the item on the top of the stack.
        Raise IndexError if the stack is empty."""
        try:
            return self._items.pop()
        except:
            raise IndexError('The stack is empty.')
    
    def peek(self):
        """Return the item on the top of the stack without popping."""
        item = self._items[-1]
        return item
    
    def is_empty(self):
        """Return True if the stack is empty."""
        return len(self._items) == 0
    
    def __len__(self):
        """Return the size of the stack."""
        return len(self._items)
    
    def __str__(self):
        """Print all the items in the stack."""
        return "Bottom -> " + repr(self._items) + " <- Top"
    
    def __repr__(self):
        """Return a string representation of the stack."""
        str(self)
        
        