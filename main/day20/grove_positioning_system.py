def solve(original_list, decryption_key=1, number_of_mixes=1):
    len_list = len(original_list)
    dll = create_linked_list(original_list)
    for _ in range(number_of_mixes):
        for i in range(len(original_list)):
            node = find_node_by_idx(dll.head, i)
            if node.numeric_value != 0:
                val = (decryption_key * node.numeric_value) % (len_list - 1)
                DoublyLinkedList.move(node, val)
    return score(find_node_by_val(dll.head, 0), decryption_key)


def score(node, decryption_key):
    ans = 0
    for i in range(3001):
        if i % 1000 == 0:
            ans += (node.numeric_value * decryption_key)
        node = node.next
    return ans


def create_linked_list(original_list):
    dll = DoublyLinkedList()
    for idx, val in enumerate(original_list):
        dll.push(val, idx)
    dll.tail.next = dll.head
    dll.head.prev = dll.tail
    return dll


def find_node_by_idx(node, idx):
    while node.original_idx != idx:
        node = node.next
    return node


def find_node_by_val(node, val):
    while node.numeric_value != val:
        node = node.next
    return node


class Node:
    def __init__(self, numeric_value, original_idx):
        self.numeric_value = numeric_value
        self.original_idx = original_idx
        self.next: Node
        self.last: Node

    def __str__(self):
        return f"numeric_value = {self.numeric_value}, original_idx = {self.original_idx}"


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def push(self, numeric_value, original_idx):
        new_node = Node(numeric_value, original_idx)
        new_node.prev = self.tail

        if self.tail is None:
            self.head = new_node
            self.tail = new_node
            new_node.next = None
        else:
            self.tail.next = new_node
            new_node.next = None
            self.tail = new_node

    @staticmethod
    def move(node, num_steps):
        nxt = node.next
        node.next.prev = node.prev
        node.prev.next = node.next

        ptr = nxt
        for _ in range(num_steps - 1):
            ptr = ptr.next

        new_next = ptr.next
        ptr.next.prev = node
        ptr.next = node
        node.prev = ptr
        node.next = new_next
        return node
