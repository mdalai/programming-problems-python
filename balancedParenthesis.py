from pythonds.basic.stack import Stack

def parentheseChecker(symbols):
  s = Stack()
  balanced =True
  i = 0
  while i < len(symbols) and balanced:
    if symbols[i] == "(":
      s.push("(")
    else:
      if s.isEmpty():
        balanced = False
      else:
        s.pop()
    i += 1
    
  if balanced and s.isEmpty():
    balanced = True
  else:
    balanced = False
    
  return balanced
  
  
print(parentheseChecker('((()))'))
print(parentheseChecker('(()'))