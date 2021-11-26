# -*- coding: utf-8 -*-
# @Time    : 2021/9/30 8:33 下午
# @Author  : Ike
# @File    : my_test_code.py
# @Software: PyCharm
import bisect
import heapq
import collections



def test_f(envelopes):
    l = sorted(envelopes, key=lambda x: (x[0], -x[1]))
    hs = [h for w, h in l]

    lowest = []
    for h in hs:
        pos = bisect.bisect_left(lowest, h)
        lowest[pos:pos + 1] = [h]

    return len(lowest)


if __name__ == '__main__':
    a = [[1,3],[1,5],[1,7],[1,8],[1,4],[2,5]]
    print(test_f(a))
