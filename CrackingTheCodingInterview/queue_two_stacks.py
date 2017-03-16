class MyStack(object):
    def __init__(self):
        self._stack = []
    
    def __len__(self):
        return len(self._stack)

    def put(self, value):
        self._stack.append(value)
    
    def pop(self):
        return self._stack.pop() if len(self._stack) > 0 else None
    
    def peek(self):
        return self._stack[-1] if len(self._stack) > 0 else None
    
    def __repr__(self):
        return str(self._stack)


class MyQueue(object):
    def __init__(self):
        self._head = MyStack()
        self._tail = MyStack()
    
    def _fill_head(self):
        if len(self._head) == 0:
            while len(self._tail) > 0:
                item = self._tail.pop()
                self._head.put(item)

    def peek(self):
        self._fill_head()
        return self._head.peek()
        
    def pop(self):
        self._fill_head()
        return self._head.pop()
        
    def put(self, value):
        self._fill_head()
        self._tail.put(value)
        
    def __repr__(self):
        return '<{cls} {attrs} at {id}>'.format(
            cls=self.__class__.__name__, attrs=self.__dict__, id=id(self))
        

queue = MyQueue()
t = int(input())
for line in range(t):
    values = map(int, input().split())
    values = list(values)
    if values[0] == 1:
        queue.put(values[1])        
    elif values[0] == 2:
        queue.pop()
    else:
        print(queue.peek())