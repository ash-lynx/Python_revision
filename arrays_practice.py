"""Array calsses 
- LinearArray
- SortedArray
"""

#--------------------------------------------------------------------------
class LinearArray():
    """Implement an linear and un-ordered array using Python list."""
    
    def __init__(self):
        self.data = list()
        self.comparisons = 0
        
    def append(self, value):
        """Add an item of the given value to the end of the array."""
        self.comparisons = 0
        self.data.append(value)
        
    def remove(self,value):
        """Remove the first occurance of value in the array."""
        index = self.get_index(value)
        
        if not index is None:
            del self.data[index]
            
    def contains(self, value):
        """Return True if the array contains the value or return False if not"""
        value_index = self.get_index(value)
        
        if value_index != None:
            return True
        else:
            return False
        
    def get_index(self, value):
        """Find the index of the given value in the array. 
        Return index of the list or return None if the value does not exist"""
        self.comparisons = 0
        self.data.append(value)  # Set a sentinel.
        last_index = len(self.data) - 1
        index = 0
        found = False
        
        while not found:
            if self.data[index] == value:
                found = True
            else:
                index += 1
            self.comparisons += 1
        
        if index == last_index:  # Check if the found value is real or dummy
            index = None
        del self.data[last_index]
        
        return index
    
    def __str__(self):
        """Print all the values in the array"""
        string = ''
        for index, value in enumerate(self.data):
            string += '{}, {}\n'.format(index, value)
        return string


#--------------------------------------------------------------------------
class SortedArray():
    """Implement an ordered linear array using Python list"""
    
    def __init__(self):
        self.data = list()
        self.comparisons = 0
        
    def insert(self, value):
        """Insert the value in to the array in its sorted position."""
        self.comparisons = 0
        lower_bound = 0
        upper_bound = len(self.data)
        index = 0
        
        while lower_bound < upper_bound:  # Use binary search to find the position
            index = (lower_bound + upper_bound) // 2
            self.comparisons += 1
            
            if self.data[index] < value:
                lower_bound = index + 1
            else:
                upper_bound = index
                
        self.data.insert(lower_bound, value)  # Insert the item using Python insert module
        
    def remove(self, value):
        """Remove the first occurance of the given value in the array."""
        index = self.get_index(value)
        
        if not index is not None:
            del self.data[index]
            
    def contains(self, value):
        """Return True if the array contains the given value. Return False if it does not"""
        index = self.get_index(value)
        
        if not index is None:
            return True
        else:
            return False
        
    def get_index(self, value):
        """Find the index of the given value in the array. 
        Return the index if it was found, return None if the item does not exist."""
        self.comparisons = 0
        lower_bound = 0
        upper_bound = len(self.data)
        index = 0
        found = False
        
        while (lower_bound < upper_bound) and (not found):  # Use binary search to find the position
            index = (lower_bound + upper_bound) // 2
            self.comparisons += 1
            
            if self.data[index] == value:  # The value is found
                found = True
            elif self.data[index] < value:
                lower_bound = index + 1
            else:
                upper_bound = index
                
        if found:
            return index
        else:
            return None
            
    def __str__(self):
        """Print all the items in the array"""
        string = ''
        for index, value in enumerate(self.data):
            string += '{}, {}\n'.format(index, value)
        return string
    