# -*- coding: utf-8 -*-
# @Time    : 2021/8/26 11:57 上午
# @Author  : Ike
# @File    : bubble-sort.py
# @Software: PyCharm


def bubble_sort(arr):
    """
    时间复杂度：O(n²)  空间复杂度：O(1)
    冒泡排序思路：
    1.遍历列表中前n-1个元素，每一个元素都与后一个元素进行比较，如果arr[index]>arr[index+1]，则呼唤位置
    2.遍历一遍后，此时列表内最大元素会被替换到列表尾部，下次遍历的范围变为n-2
    3.重复直到n的大小为0结束，此时列表有序
    :param arr:
    :return:
    """
    length = len(arr)
    while length > 0:
        for index in range(length - 1):
            if arr[index] > arr[index + 1]:
                arr[index], arr[index + 1] = arr[index + 1], arr[index]
        length -= 1
    return arr


if __name__ == '__main__':
    print(bubble_sort([3, 1, 5, 4, 2, 6]))
