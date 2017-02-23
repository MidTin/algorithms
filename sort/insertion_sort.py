"""
插入排序（Insertion Sort）

分类：              内部比较排序
最差时间复杂度：    最坏情况为输入序列是降序排列的,此时时间复杂度O(n^2)
最优时间复杂度：    最好情况为输入序列是升序排列的,此时时间复杂度O(n)
稳定性：            稳定

1. 从第一个元素开始，该元素可以认为已经被排序
2. 取出下一个元素，在已经排序的元素序列中从后向前扫描
3. 如果该元素（已排序）大于新元素，将该元素移到下一位置
4. 重复步骤3，直到找到已排序的元素小于或者等于新元素的位置
5. 将新元素插入到该位置后
6. 重复步骤2~5
"""


def insertion_sort(s):
    n = len(s)
    for i in range(0, n):
        for j in range(i, -1, -1):
            if j != 0:
                if s[j] < s[j-1]:
                    s[j], s[j-1] = s[j-1], s[j]
                else:
                    break

    return s


if __name__ == "__main__":
    s = [3, 5, 1, 2, 4, 7, 6, 8]
    print("Before:", s)
    insertion_sort(s)
    print("After:", s)
