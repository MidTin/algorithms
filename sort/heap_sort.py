"""
堆排序（Heap Sort）

分类:               内部比较排序
数据结构:           数组
最差时间复杂度:     O(nlogn)
最优时间复杂度:     O(nlogn)
稳定性:             不稳定


首先，按堆的定义将数组R[0..n]调整为堆（这个过程称为创建初始堆），交换R[0]和R[n]；
然后，将R[0..n-1]调整为堆，交换R[0]和R[n-1]；
如此反复，直到交换了R[0]和R[1]为止。

以上思想可归纳为两个操作：
1. 根据初始数组去构造初始堆（构建一个完全二叉树，保证所有的父结点都比它的孩子结点数值大）。
2. 每次交换第一个和最后一个元素，输出最后一个元素（最大值），然后把剩下元素重新调整为大根堆。
"""


def heap_sort(s, tail_idx):

    def swap(a, b):
        s[a], s[b] = s[b], s[a]

    if tail_idx == 0:
        return s

    n = tail_idx + 1
    for i in range(tail_idx, -1, -1):
            chld_idx = i * 2 + 1
            if chld_idx < n:
                nxt_chld_idx = chld_idx + 1
                if nxt_chld_idx < n and s[chld_idx] < s[nxt_chld_idx]:
                    chld_idx = nxt_chld_idx

                if s[i] < s[chld_idx]:
                    swap(i, chld_idx)

    swap(0, tail_idx)
    print("第", abs(tail_idx - len(s)), "趟:", s)
    return heap_sort(s, tail_idx-1)


if __name__ == "__main__":
    s = [1, 4, 3, 5, 2, 6, 9, 7, 8, 0]
    print("Before:", s)
    heap_sort(s, len(s) - 1)
    print("After:", s)
