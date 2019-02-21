from BinaryTree import Node

root = Node(10)
root.insert(5)
root.insert(49)
root.insert(19)
root.insert(3)

print('--- In Order ----')
root.printInOrder()
print('--- Pre Order ----')
root.printPreOrder()
print('--- Post Order ----')
root.printPostOrder()
