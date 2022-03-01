
# if cur.start <= last.end:
#     merge
# else:
#     insert new list


# [[1,3],[2,6],[8,10],[15,18]]

# [[1,6],[8,10],[15,18]]
class Solution:
    def merge(self, intervals):
        if not intervals:
            return []
        intervals.sort(reverse=False)
        result = [intervals[0]]
        for item in intervals:
            if result[-1][1] >= item[0]:
                result[-1][1] = max(result[-1][1], item[1])
            else:
                result.append(item)
        return result
                


if __name__ == '__main__':
    s = Solution()
    x = s.merge([[1,4],[2,3]])
    print(x)
    