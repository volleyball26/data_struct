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

if __name__ == '__main__':
    seq_list = SequenceList(3)
    print(seq_list.empty())