"""Deque using Python list and linked list."""

#--------------------------------------------------------------------------
class Deque(object):
    """Implementing deque using Python list."""
    
    def __init__(self):
        self._items = []
        
    def enqueue_front(self, item):
        """Push the item in the front of the deque"""
        self._items.insert(0, item)
        
    def enqueue_rear(self, item):
        """Push the item in the end of the deque"""
        self._items.append(item)
        
    def dequeue_front(self):
        """Pop the item in the front of the deque. 
        Raise IndexError if the deque is empty.
        """
        try:
            return self._items.pop(0)
        except:
            raise IndexError('The deque is empty')
        
    def dequeue_rear(self):
        """Pop the item in the end of the deque.
        Raise IndexError if the deque is empty.
        """
        try:
            return self._items.pop()
        except:
            raise IndexError('The deque is empty')
        
    def is_empty(self):
        """Return True if the deque is empty."""
        return len(self._items) == 0
    
    def __len__(self):
        """Return the length of the deque."""
        return len(self._items)
    
    def __repr__(self):
        """Return the representation of the deque"""
        return "Front -> " + repr(self._items) + " <- Rear"
    
    