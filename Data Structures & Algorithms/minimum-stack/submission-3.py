class MinStack:

    def __init__(self):
        self.stack = deque() 
        self.minimum = deque()
        

    def push(self, val: int) -> None:
        self.stack.appendleft(val)
        if not self.minimum:
            self.minimum.append(val)
        else:
            if val > self.minimum[-1]:
                self.minimum.append(val)
            elif val <= self.minimum[0]:
                self.minimum.appendleft(val)
        

    def pop(self) -> None:
        if self.stack[0] == self.minimum[0]:

            self.minimum.popleft()

        self.stack.popleft()
    

    def top(self) -> int:
        return self.stack[0]
        

    def getMin(self) -> int:
        return self.minimum[0]
    

# minStack = MinStack()
# print(minStack.stack, minStack.minimum)
# minStack.push(1);
# print(minStack.stack, minStack.minimum)
# # minStack.push(2);
# print(minStack.stack, minStack.minimum)
# # minStack.push(0);
# print(minStack.stack, minStack.minimum)
# minStack.getMin(); ## return 0
# print(minStack.stack, minStack.minimum)
# # minStack.pop();
# print(minStack.stack, minStack.minimum)
# # minStack.top();    ## return 2
# print(minStack.stack, minStack.minimum)
# # minStack.getMin(); ## return 1
# print(minStack.stack, minStack.minimum)
        
