"""
选择排序（Selection Sort）

分类：          内部比较排序
最差时间复杂度：      O(n^2)
最优时间复杂度：      O(n^2)
稳定性：              不稳定


首先在未排序序列中找到最小（大）元素，存放到排序序列的起始位置，
然后，再从剩余未排序元素中继续寻找最小（大）元素，然后放到已排序序列的末尾。
以此类推，直到所有元素均排序完毕。
"""


def selection_sort(s):
    n = len(s)
    for i in range(n):
        min_idx = i
        for j in range(i, n):
            if s[min_idx] > s[j]:
                min_idx = j

        s[i], s[min_idx] = s[min_idx], s[i]

    return s


if __name__ == "__main__":
    s = [4, 5, 1, 0, 6, 8, 7, 3]
    print("Before:", s)
    selection_sort(s)
    print("After:", s)
