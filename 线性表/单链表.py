class Node():
    def __init__(self, val):
        self.val = val
        self.next = None

class SingleLinkedList():

    def __init__(self):
        """[初始化单链表]
        """
        self.head = None
        self.tail = None

    def emtpy(self):
        """[
            判断单链表是否为空
            若表头指针指向空，则单链表为空
            ]

        Returns:
            [bool]: [单链表是否为空]
        """
        return self.head is None

    def length(self):
        size = 0
        cur = self.head
        while cur != None:
            size += 1
            cur = cur.next
        return size

    def prepend(self, val):
        """[头插法]

        Args:
            val ([Any]]): [插入的值]
        """
        newNode = Node(val)
        if self.head is None:
            self.head = newNode
            self.tail = self.head
        else:
            newNode.next = self.head
            self.head = newNode

    def insert(self, index, val):
        """[
            将新节点插入到链表的第i个位置时，需要先遍历单链表到i-1个节点，
            将第i-1个节点的直接后继指针指向新节点，将新节点的直接后继指针指向第i个位置
        ]

        Args:
            index ([type]): [description]
            val ([type]): [description]
        """
        newNone = Node(val)

        cur = self.head

        for _ in range(index-1):
            cur = cur.next
        
        temp = cur.next
        newNone.next = temp
        cur.next = newNone

    def append(self, value):
        """[summary]

        Args:
            value ([type]): [description]
        """
        newNode = Node(value)

        if self.emtpy():
            self.head = newNode
            self.tail = newNode
        else:
            self.tail.next = newNode
            self.tail = newNode

    def del_first(self):
        """[
            删除头节点
            1.单链表为空，抛出异常
            2.单链表不为空且只有一个节点，将头、尾指针指向空
            3.单链表不为空且有多个节点， 将头指针指向下一个节点
        ]

        Raises:
            IndexError: [description]
        """
        if self.head is None:
            raise IndexError("链表为空")
        if self.length() == 1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next

    def delete(self):
        """[summary]
        """

    def del_last(self):
        """[删除尾节点]
        """
        if self.head is None:
            raise IndexError("链表为空")
        if self.length() == 1:
            self.head = None
            self.tail = None
        else:
            pre = self.head
            cur = pre.next

            while cur.next is not None:
                pre = cur
                cur = cur.next
            cur = None
            pre.next = None
            self.tail = None


if __name__ == '__main__':
    sll = SingleLinkedList()
    print(sll.emtpy())
    print(sll.length())

