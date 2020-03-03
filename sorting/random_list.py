import random
from .algorithms import bubble_sort, insertion_sort, selection_sort, merge_sort, quick_sort


class RandomList(object):
    """
    """
    ALGO_CHOICES = (
        'bubble-sort',
        'insertion-sort',
        'selection-sort',
        'merge-sort',
        'quick-sort',
    )
    ALGO_CONFIG = {
        'bubble-sort': bubble_sort,
        'insertion-sort': insertion_sort,
        'selection-sort': selection_sort,
        'merge-sort': merge_sort,
        'quick-sort': quick_sort,
    }

    def __init__(self, max_range=1000, list_size_min=6, list_size_max=9):
        self.max_range = max_range
        self.list_size_min = list_size_min
        self.list_size_max = list_size_max
        self.arr = self.prepare_list()

    def _validate_algo(self, algo):
        assert algo in self.ALGO_CHOICES, f'invalid algo \'{algo}\' provided, allowed values {self.ALGO_CHOICES}'

    def prepare_list(self):
        return random.choices(
            range(self.max_range),
            k=random.randint(
                self.list_size_min,
                self.list_size_max
            )
        )

    def get_handler(self, algo='bubble-sort'):
        """
        return respective sorting function as per algo provided
        :param algo: ALGO_CHOICES
        :return:
        """
        self._validate_algo(algo=algo)
        return self.ALGO_CONFIG.get(algo)

    def sorted_list(self, algo='bubble-sort'):
        """
        :param algo: ALGO_CHOICES
        :return:
        """
        self._validate_algo(algo=algo)
        handler = self.get_handler(algo=algo)
        return handler(self.arr)
