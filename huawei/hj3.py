stu_list = []
while True:
    range_num = int(input())
    try:
        for _ in range(range_num):
            stu_num = input()
            if stu_num is None:
                break
            else:
                stu_list.append(int(stu_num))
    except (ValueError, EOFError):
        break


_ = list(set(stu_list))
stu_list = _.sort(reverse=False)
for i in stu_list:
    print(i, end=('\n'))