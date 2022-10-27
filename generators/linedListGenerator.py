

class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None
    def __str__(self):
        return str(self.data)

class SinglyLinkedList:
    def __init__(self) -> None:
        self.head = None


    def __iter__(self):
        temp = self.head

        while temp:
            yield temp
            temp = temp.next




node1 = Node(5)
node2 = Node(6)
node3 = Node(7)
node4 = Node(8)

node1.next = node2
node2.next = node3
node3.next = node4

singly_list = SinglyLinkedList()
singly_list.head = node1

for node in singly_list:
    print(node, end=" ")