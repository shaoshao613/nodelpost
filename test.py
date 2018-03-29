import sys


class Node:
    '''
    data: 节点保存的数据
    _next: 保存下一个节点对象
    '''
    def __init__(self, data, pnext=None):
        self.data = data
        self._next = pnext

    def __repr__(self):
        '''
        用来定义Node的字符输出，
        print为输出data
        '''
        return str(self.data)


if __name__ == '__main__':
    list = sys.argv[1:]
    print(list)
    size = len(list)
    ex_count = 1
    i = size - 1
    count = 0;
    l = 1;
    index = 0;
    while i>2*(size - 1 - i):
        print("i:%s i2:%s,count:%s l:%s list:%s" % (i,2 * (size - 1 - i), count, l,list))
        if count == 0:
            (list[i], list[2 * (size - 1 - i)]) = (list[2 * (size - 1 - i)],list[i])
            count += 1
            l += 1
            pass
        elif count == 1:

            a = size - 1
            # if (l-2 )% 4 ==0:
            #     a = size - (l+2)/4
            # elif  l % 6 ==0:
            #     a = size - 2

            (list[a], list[2 * (size - 1 - i) + 1]) = (list[2 * (size - 1 - i) + 1],list[a])
            count = 0
            l +=1
            i -= 1
            pass
    print(list)