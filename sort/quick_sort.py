"""快速排序（Quick Sort）

快速排序采用分治法进行排序。

分治法的基本思想是：
    将原问题分解为若干个规模更小但结构与原问题相似的子问题。
    递归地解这些子问题，然后将这些子问题的解组合为原问题的解。


分类：              内部比较排序
最差时间复杂度：    每次选取的基准都是最大的元素（或者每次都是最小），导致每次只划分出了一个子序列，
                    需要进行n-1次划分才能结束递归，时间复杂度为O(n^2)
最优时间复杂度：    每次选取的基准都能使划分均匀，只需要logn次划分就能结束递归，时间复杂度为O(nlogn)
稳定性：            不稳定


1. 在数据集之中，选择一个元素作为”基准”（pivot）。
2. 所有小于”基准”的元素，都移到”基准”的左边；所有大于”基准”的元素，都移到”基准”的右边。
   这个操作称为分区 (partition) 操作，分区操作结束后，基准元素所处的位置就是最终排序后它的位置。
3. 对”基准”左边和右边的两个子集，不断重复第一步和第二步，直到所有子集只剩下一个元素为止
"""


def quick_sort(s, start, stop):
    if stop - start < 2:
        return s

    pivot = s[stop-1]
    k = start
    for i in range(start, stop):
        if s[i] <= pivot:
            s[i], s[k] = s[k], s[i]
            k += 1

    quick_sort(s, start, k-1)
    quick_sort(s, k, stop)
    return s

if __name__ == "__main__":
    s = [6, 5, 3, 1, 8, 7, 4]
    print('Before:', s)
    s = quick_sort(s, 0, len(s))
    print('After:', s)
