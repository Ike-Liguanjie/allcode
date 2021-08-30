# -*- coding: utf-8 -*-
# @Time    : 2021/8/26 11:05 上午
# @Author  : Ike
# @File    : insertion-sort.py
# @Software: PyCharm
from config import *


@time_log("插入排序算法")
def insertion_sort(arr: list) -> list:
    """
    时间复杂度：O(n²)  空间复杂度：O(1)
    插入排序算法思路：
    1.循环保存被插入的元素insert_num,比较的索引insert_index为被插元素的前一个，即index-1
    2.从列表第二个元素开始，不断的和前一个比较，当前一个元素insert_index>-1且比insert_num大的时候，说明满足替换条件
      此时把insert_index位置的值后移一位，即arr[insert_index + 1] = arr[insert_index]，同时insert_index-1继续比较寻找
    3.当不满足替换条件的时候，说明上一步找到的insert_index就是正确的插入位置，此时arr[insert_index + 1] = insert_num，完成插入
    4.重复index循环直到列表尾部结束，此时列表有序
    :param arr:
    :return:
    """
    for index in range(len(arr)):
        insert_num = arr[index]
        insert_index = index - 1
        while insert_index > -1 and arr[insert_index] > insert_num:
            arr[insert_index + 1] = arr[insert_index]
            insert_index -= 1
        arr[insert_index + 1] = insert_num
    return arr


if __name__ == '__main__':
    print(insertion_sort(sort_list))
