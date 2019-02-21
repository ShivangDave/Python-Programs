import LinkedList
from LinkedList import Node

node1 = Node("3")
node2 = Node("7")
node3 = Node("10")

node1.nextNode = node2
node2.nextNode = node3
head = node1
currentNode = head

while currentNode is not None:
    print(currentNode.value + "->")
    currentNode = currentNode.nextNode
