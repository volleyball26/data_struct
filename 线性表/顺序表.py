class SequenceList:

    def __init__(self, max):
        """[初始化顺序表]

        Args:
            max ([int]): [顺序表长度]
        """
        self.max = max
        self.index = 0
        self.data = [None for _ in range(self.max)]

    def __getitem__(self, index):
        """[获取下标值为index的元素]

        Args:
            index ([int]): [下标]
        """
        if index < 0 or index >= self.index:
            raise IndexError("Index 不合法")
        else:
            return self.data[index]

    def __setitem__(self, index, value):
        """[修改index下标的元素值]

        Args:
        index ([int]): [下标]
        value ([int]): [替换元素]
        """
        if index < 0 or index > self.index:
            raise IndexError("Index 不合法")
        else:
            self.data[index] = value

    def append(self, value):
        """[表尾插入数据]

        Args:
            value ([type]): [description]
        """
        if self.index == self.max:
            return
        else:
            self.data[self.index] = value
            self.index += 1


    def insert(self, index, value):
        """[在任意位置插入元素]

        Args:
            index ([int]): [下标]
            value ([int]): [元素]]
        """
        if index < 0 or index > self.index:
            raise IndexError("Index 不合法")
        if index == self.index:
            self.append(value)
        else:
            0, 3, -1
            for i in range(self.index, index, -1):
                print(i)
                self.data[i] = self.data[i-1]
            self.data[index] = value
            self.index += 1

    def delete(self, index, value):
        """[删除任意位置的元素]

        Args:
            index ([int]): [下标]
            value ([int]): [元素]
        """
        if index < 0 and index > self.index:
            raise IndexError("Index 不合法")
        if index == self.index:
            self.pop()
        for i in range(index, self.index):
            self.data[i] = self.data[i+1]
        self.index -= 1
        

    def pop(self):
        """[删除表尾的元素]
        """
        if self.empty() == True:
            return
        remove data[-1]
        del self.data[-1] 
        self.index -= 1


    def empty(self):
        """[判断顺序表是否为空]

        Returns:
            [Bool]: [返回True 或者 False]
        """
        return True if self.index == 0 else False

    def append(self, value):
        """[表尾插入元素]

        Args:
            value ([int]): [元素]
        """
        if self.index is self.max:
            return
        else:
            self.data[self.index] = value
            self.index += 1

    def length(self):
        """[返回顺序表长度]
        """
        return self.index

    def traversal(self):
        """[遍历顺序表]
        """
        if self.length == 0:
            return
        for i in self.data:
            print(i)

if __name__ == '__main__':
    seq_list = SequenceList(4)
    # print(seq_list.__getitem__(2))
    # seq_list.insert(0, 1)
    # seq_list.insert(0, 2)
    # seq_list.insert(0, 3)
    # seq_list.insert(0, 4)

    # seq_list.traversal()