from collections import deque
def brackets(line):
   stack = deque()
   for i in line:
       if i == '(':
           stack.append(i)
       elif i == ')':
           if len(stack) == 0:
               return False
           stack.pop()
   if len(stack) == 0:
       return True
   return False