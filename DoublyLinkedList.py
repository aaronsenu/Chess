class Node(object):

    def __init__ (self, d, n = None, p = None):
        self.data = d
        self.next = n
        self.prev = p

    def get_next (self):
        return self.next

    def set_next (self, n):
        self.next = n

    def get_prev (self):
        return self.prev

    def set_prev (self, p):
        self.prev = p

    def get_data (self):
        return self.data

    def set_data (self, d):
        self.data = d


class DoublyLinkedList (object):

    def __init__(self, r = None):
        self.root = r
        self.tail = r
        self.size = 0
        self.current = r

    def get_size (self):
        return self.size

    def add (self, d):
        if self.size == 0:
            new_node = Node(d, None, None)
            self.root = new_node
            self.tail = self.root
            self.current = self.root
            self.size += 1

        else: 
            new_node = Node (d, None, self.current)
            self.tail = new_node
            self.current.set_next(new_node)
            self.current.get_next().set_prev(self.current)
            self.current = self.current.get_next()
            self.size += 1

    def remove (self, d):
        this_node = self.root

        while this_node:
            if this_node.get_data() == d:
                next = this_node.get_next()
                prev = this_node.get_prev()
                
                if next:
                    next.set_prev(prev)
                if prev:
                    prev.set_next(next)
                else:
                    self.root = this_node
                self.size -= 1
                return True		# data removed
            else:
                this_node = this_node.get_next()
        return False  # data not found
    
#myList = DoublyLinkedList()

#myList.add(5)
#myList.add(8)
#myList.add(12)

#current = myList.tail
#print(current.prev.data)

