
class stack:
    def __init__(self,data=None):
        self.items = [] if data==None else data

    def size(self):
        return len(self.items)
    def __str__(self):
        s = ''
        for i in self.items:
            s+= str(i)
        return s
        #return 'stack   size '+str(self.size())+'\t => ' + str(self.items)
    def pop(self):
        if self.size()>0:
            return self.items.pop()
        else:
            return None
    def push(self,data):
        self.items.append(data)

class queue:
    def __init__(self,data=None):
        self.items = [] if data==None else data

    def __str__(self):
        s = ''
        for i in self.items :
            s += str(i)
        return s
    
    def enQ(self,data):
        self.items.append(data)

    def deQ(self):
        return self.items.pop(0)

    def size(self):
        return len(self.items)

print('-----1-----')
l = [c for c in input('input: ').split()]
print('l= ',l)

s = stack(l)
print(s)
#############################
q = queue()
while s.size()!=0:
    q.enQ(s.pop())
while q.size()!=0:
    s.push(q.deQ())

#############################
print(s)
