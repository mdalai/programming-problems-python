def BinaryTree(r):
    return [r,[],[]]

def insertLeft(root,newBranch):
    t = root.pop(1)
    #print(t,len(t))
    if len(t) > 1:
        root.insert(1,[newBranch, t, []])
    else:
        root.insert(1,[newBranch,[], []])

    return root

def insertRight(root,newBranch):
    t = root.pop(2)
    if len(t) > 1:
        root.insert(2,[newBranch,[],t])
    else:
        root.insert(2,[newBranch,[],[]])

    return root

def getRootVal(root):
    return root[0]

def setRootVal(root, newRootVal):
    root[0] = newRootVal

def getLeftChild(root):
    return root[1]

def getRightChild(root):
    return root[2]


            
r = BinaryTree(3)
insertLeft(r,4)
insertLeft(r,5)
insertRight(r,6)
insertRight(r,7)
#print(r)

l = getLeftChild(r)
print(l)

setRootVal(l,9)
print(r)
insertLeft(l,11)
print(r)
print(getRightChild(getRightChild(r)))

def buildTree():
    r = BinaryTree('a')
    insertLeft(r,'b')
    insertRight(getLeftChild(r),'d')

    insertRight(r,'c')
    insertLeft(getRightChild(r),'e')
    insertRight(getRightChild(r),'f')

    return r

ttree = buildTree()
print(ttree)

