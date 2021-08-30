# -*- coding: utf-8 -*-
# @Time    : 2021/8/26 3:21 下午
# @Author  : Ike
# @File    : merge-sort.py
# @Software: PyCharm
from config import *


def merge(left_list: list, right_list: list) -> list:
    result = []
    while left_list or right_list:
        if left_list:
            if right_list:
                if left_list[0] < right_list[0]:
                    result.append(left_list.pop(0))
                else:
                    result.append(right_list.pop(0))
            else:
                result += left_list
                left_list = []
        elif right_list:
            result += right_list
            right_list = []
    return result


@time_log("归并排序算法-递归实现")
def merge_sort_merge(arr: list, left=None, right=None) -> list:
    """
    时间复杂度：O(nlogn)  空间复杂度：O(n)
    归并排序算法-递归实现：
    1.将列表根据中位数分成左右两部分，重复这一步骤，直到分到最小
    2.将分成的最小部分排序，然后合并之后继续排序
    3.重复直到最大的两部分排序完成，此时列表有序
    :param arr:
    :param left:
    :param right:
    :return:
    """
    if left is not None:
        if left < right:
            mid = (left + right) // 2
            merge_sort_merge(arr, left, mid)
            merge_sort_merge(arr, mid + 1, right)
            arr[left:right + 1] = merge(arr[left:mid + 1], arr[mid + 1:right + 1])
    else:
        merge_sort_merge(arr, 0, len(arr) - 1)
    return arr


@time_log("归并排序算法-迭代实现")
def merge_sort_in_iteration(arr: list) -> list:
    """
    时间复杂度：O(nlogn)  空间复杂度：O(n)
    归并排序算法-迭代实现：
    1.设置步长step为1，根据步长将数组内相邻的区间进行排序
    2.每循环一次，step*2  PS：步长的选择也会影响算法的复杂度，这里用2的n次方比较简单
    3.直到step>arr.length，循环结束，此时列表有序
    :param arr:
    :return:
    """
    length = len(arr)
    step = 1
    while step < length:
        left, mid, right = 0, step, 2 * step
        while left < length:
            arr[left:right] = merge(arr[left:mid], arr[mid:right] if mid <= length else [])
            left = right
            mid = left + step
            right = mid + step
        step *= 2
    return arr


if __name__ == "__main__":
    print(merge_sort_merge(sort_list))
    print(merge_sort_in_iteration(sort_list))
