def bubble_sort(arr):
    """
    sort the provided list `arr` using bubble-sort sorting algorithm
    :param arr:
    :return:
    """
    comparison_count = 0
    ls = [*arr]
    n = len(ls)
    for i in range(n-1):
        for j in range(n-i-1):
            if ls[j] > ls[j+1]:
                ls[j], ls[j+1] = ls[j+1], ls[j]
            comparison_count += 1
    return ls, comparison_count