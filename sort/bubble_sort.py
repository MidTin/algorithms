"""
冒泡排序算法（Bubble Sort）

分类：              内部比较排序
最差时间复杂度：    O(n^2)
最优时间复杂度：    O(n)
稳定性：            稳定

1. 依次比较相领的两个元素，当顺序错误时，把两者位置调换。
2. 重复步骤 1, 除去上一轮排到最后位置的元素不作比较。直到没有任何元素需要比较。
"""


def bubble_sort(s):
    n = len(s)
    while n > 1:
        for i in range(n):
            if i + 1 < n and s[i] > s[i+1]:
                s[i], s[i+1] = s[i+1], s[i]

        n -= 1

    return s


if __name__ == "__main__":
    s = [6, 5, 3, 1, 8, 7, 4]
    print('Before:', s)
    s = bubble_sort(s)
    print('After:', s)
