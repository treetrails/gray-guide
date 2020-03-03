from sorting import RandomList


def main():
    """
    :return:
    """
    # prepare unsorted list
    rls = RandomList()
    print(f'initial: {rls.arr}')

    # sort the list
    # algo = 'bubble-sort'
    algo = 'insertion-sort'
    sorted_rls, comparison_count = rls.sorted_list(algo=algo)

    # print the list
    print(f'sorted: {sorted_rls}')
    print(f'comparisons: {comparison_count}')


if __name__ == '__main__':
    main()
