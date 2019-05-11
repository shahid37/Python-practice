from element import Element


class Queue(object):

    def __init__(self):
        self.front = None
        self.rear = None
        self.length = 0

    def enqueue(self, data):
        new_element = Element(data)
        if self.rear is None:
            self.rear = self.front = new_element
            new_element.next = None
        else:
            self.rear.next = new_element
            self.rear = new_element
            new_element.next = None
        self.length += 1

    def print(self):
        current = self.front
        if self.front:
            while current.next:
                print("[" + str(current.value) + "]")
                current = current.next
            print("[" + str(current.value) + "]")
        else:
            print("list is empty")

    def de_queue(self):
        if self.front is not None:
            first_node = self.front
            self.front = self.front.next
            self.length -= 1
            print('deleted node: ' + str(first_node.value))
            del first_node
        else:
            print("list is empty")
