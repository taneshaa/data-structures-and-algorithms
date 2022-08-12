class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        input_ = ""
        current = self.head

        while current:
            input_ += f"{{ {str(current.value)} }} -> "
            current = current.next
        return input_ + "NULL"

    def insert(self, value):
        self.head = Node(value, self.head)

    def includes(self, value):
        current = self.head

        while current:
            if current.value == value:
                return True

            current = current.next

        return False

    def append(self, new):
        new_node = Node(new)

        if self.head:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
        else:
            self.head = new_node
        return new_node

    def insert_before(self, value, new_value):
        previous = current = self.head

        if self.head is None:
            raise TargetError
        if self.includes(value) is False:
            raise TargetError

        while current:
            if value == current.value:
                new_node = Node(new_value)
                if current == self.head:
                    new_node.next = self.head
                    self.head = new_node
                    return new_node
                else:
                    previous.next = new_node
                    new_node.next = current
                    return new_node
            else:
                previous = current
                current = current.next

    def insert_after(self, value, new):
        current = self.head

        if self.head is None:
            raise TargetError
        if self.includes(value) is False:
            raise TargetError
        while current:
            if current.value == value:
                new_node = Node(new)
                new_node.next = current.next
                current.next = new_node
                return new_node
            else:
                current = current.next

    def length_of_linked_list(self):
        n = 0
        current = self.head

        while current:
            current = current.next
            n += 1
        return n

    def kth_from_end(self, k):
        if k >= 0:
            current = self.head
            length = self.length_of_linked_list()
            target = length - k

            if target < 1:
                raise TargetError
            for i in range(1, target):
                current = current.next
            return current.value
        else:
            raise TargetError


class Node:
    def __init__(self, value, next_=None):
        self.value = value
        self.next = next_


class TargetError(Exception):
    pass
