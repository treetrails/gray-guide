def insertion_sort(arr):
    """
    sort the provided list `arr` using insertion-sort sorting algorithm
    :param arr:
    :return:
    """
    ls = [*arr]
    n = len(arr)
    comparison_count = 0
    for i in range(1, n):
        ci = i
        # current index

        while ci and ls[ci] < ls[ci-1]:
            ls[ci-1], ls[ci] = ls[ci], ls[ci-1]
            comparison_count += 1

    return ls, comparison_count
