class Node:
    def __init__(self,value, nextNode=None):
        self.value = value
        self.nextNode = nextNode

class LinkedList:
    def insertNode(head,value):
        currentNode = head

        while currentNode is not None:
            if currentNode.nextNode is None:
                currentNode.nextNode = Node(value)
                return head
            currentNode = currentNode.nextNode

    def deleteNode(head,value):
        currentNode = head
        previousNode = None

        while currentNode is not None:
            if currentNode.value == value:
                if previousNode is None:
                    newHead = currentNode.nextNode
                    currentNode.nextNode = None
                    return newHead
                previousNode.nextNode = currentNode.nextNode
                return head
            previousNode = currentNode
            currentNode = currentNode.nextNode
        return head
