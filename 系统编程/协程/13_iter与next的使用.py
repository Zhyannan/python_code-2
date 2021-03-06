# 自定义迭代器

from collections import Iterable


# 我们迭代器一初始化就有一个列表


class MyList(object):
    # 初始化的时候就有列表
    def __init__(self):
        use_list = [1, 2, 3, 4, 5]
        # 来一个空的列表
        # use_list = list()
        self.use_list = use_list  # 初始化的时候有一个列表了
        self.count = 0  # 列表的第一个索引

    def __iter__(self):  # 可迭代对象,返回一个可迭代对象,返回自己
        return self

    def add(self, value):  # 添加数据
        self.use_list.append(value)

    def __next__(self):  # 迭代的时候取值
        # 如果我们的个数已经到底了,那么我们手动的去抛出异常
        if self.count < len(self.use_list):
            # 调用的时候加1
            value = self.use_list[self.count]
            self.count += 1
            return value  # 怎么让我们的迭代器停下来,使用异常
        else:
            # 超出了
            raise StopIteration  # 停止迭代


# iter()
# next()
# my_list = MyList()
#
# my_list.add("飞龙在天")
# my_list.add("青龙")
# my_list.add("白虎")
# my_list.add("坑龙在天")

list = MyList()
my_list = iter(list)  # 得到一个可迭代的对象  # 如果本身就是一个迭代器那么可以不写,建议后期都 写
# next("用来取值")
print(next(my_list))
print(next(my_list))
print(next(my_list))
print(next(my_list))

# 不是我们自己写的列表
a = [1, 2, 3, 4]
i = iter(a)
next(i)
