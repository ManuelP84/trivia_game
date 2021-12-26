
class Array(object):
    """Data structure to save the questions from the txt file."""

    def __init__(self):
        self._items = list()
       
    def __len__(self):
        return len(self._items)    
    
    def __getitem__(self, index: int):
        return self._items[index]

    def __setitem__(self, index: int , new_item):        
        self._items[index] = new_item
    
    def pushitem(self, new_item):
        self._items.append(new_item)

    def popitem(self, index):
        self._items.pop(index)
