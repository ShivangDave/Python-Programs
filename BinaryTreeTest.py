from BinaryTree import Node

root = Node(10)
root.insert(15)
root.insert(9)
root.insert(49)
root.insert(3)
root.insert(41)
root.insert(7)
root.insert(50)

print('--- In Order ----')
root.printInOrder()
print('--- Pre Order ----')
root.printPreOrder()
print('--- Post Order ----')
root.printPostOrder()
