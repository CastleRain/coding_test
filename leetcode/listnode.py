class ListNode():
    def __init__(self, val = None):
        self.val = val
        self.next = None

class LinkedList():
    def __init__(self):
        self.head = ListNode()

    def add(self, data):
        new_node = ListNode(data)
        cur = self.head
        while cur.next != None:
            cur = cur.next
        cur.next = new_node

    def length(self):
        cur = self.head
        result = 0
        while cur.next != None:
            cur = cur.next
            result += 1
        return result

    def display(self):
        elem = []
        cur = self.head

        while cur.next != None:

            cur = cur.next
            elem.append(cur.val)

        print(elem)

    def erase(self, index):
        if index >= self.length():
            print("error")
            return


        cur = self.head
        cur_index = 0

        while True:
            last_node = cur
            cur_node = cur.next
            if cur_index == index:
                last_node.next = cur_node.next
                return
            cur_index+=1
    def get(self, index):
        if index >= self.length():
            print("error")
            return

        cur = self.head




def main():

    ll = LinkedList()
    ll.add(1)
    ll.display()
    ll.add(2)
    ll.display()
    ll.add(3)
    ll.display()
    ll.erase(0)
    ll.display()




if __name__ == "__main__":
    main()