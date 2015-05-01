class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.warp = None
        self.final = None
        self.head = None
        self.list = []

    def __str__(self):
        return repr(self.data)

class Weird:
    def __init__(self,data=None):
        self.root = Node(data)
        if data:
            self.size = 1 
    def append(self,data):
        if self.root.data==None:
            self.root = Node(data)
            self.size = 1
        else:
            cur = self.root
            counter = 0
            warp=None
            while cur.next:
                cur = cur.next
                if (counter%self.size/2)==0:
                    warp=cur
                
            new_node = Node(data)
            if warp:
                new_node.warp=warp
            self.update_final(new_node)
            cur.next = new_node
    
    def prepend(self,data):
        new_head = Node(data)
        new_head.next = self.root
        new_head.head = self.root
        self.root = new_head

    def update_final(self,node):
        cur = self.root 
        counter=0
        while cur:
            if counter%2==0:
                cur.final = node
            counter+= 1
            cur = cur.next
    
    
