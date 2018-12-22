"""Queue using Python list and linked list."""

#--------------------------------------------------------------------------
class Queue(object):
    """Implement queue using Python list."""
    
    def __init__(self):
        self._items = []
        
    def enqueue(self, item):
        """Add the item in the end of queue."""
        self._items.append(item)
        
    def dequeue(self):
        """Pop and return the item from the front of the queue.
        Raise IndexError if the queue is empty.
        """
        try:
            return self._items.pop(0)
        except:
            raise IndexError('The queue is empty')
        
    def is_empty(self):
        """Return True if the queue is empty."""
        return len(self._items) == 0
    
    def __len__(self):
        """Return the length of the queue."""
        return len(self._items)
    
    def __str__(self):
        """Return the string showing the queue."""
        return "Front -> " + repr(self._items) + " <- Rear"
    
    def __repr__(self):
        """Return the string representation of the queue."""
        return str(self)
    
    