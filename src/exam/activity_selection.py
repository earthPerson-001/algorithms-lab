import unittest


def greedy_iterative_activity_selection(start_times, finish_times):
    activities_sorted_finish_time = sorted(
        zip(start_times, finish_times, [i for i in range(len(start_times))]),
        key=lambda x: x[1],
    )

    selected = []
    n_selected = 0
    selected.append(activities_sorted_finish_time[0])
    n_selected += 1

    for start_time, finish_time, idx in activities_sorted_finish_time[1:]:
        if start_time >= selected[n_selected - 1][1]:
            selected.append((start_time, finish_time, idx))
            n_selected += 1

    return [idx for _, _, idx in selected]


def greedy_recursive_activity_selection(start_times, finish_times, indices: list[int] | None = None, last_selected: int | None= None):
    if last_selected is None:
        # sorting the provided activities
        activities_sorted_finish_time = sorted(
            zip(start_times, finish_times, [i for i in range(len(start_times))]),
            key=lambda x: x[1],
        )

        sorted_start_times = []
        sorted_finish_times = []
        sorted_indices = []

        for start_time, finish_time, idx in activities_sorted_finish_time:
            sorted_start_times.append(start_time)
            sorted_finish_times.append(finish_time)
            sorted_indices.append(idx)

        return [sorted_indices[0]] + greedy_recursive_activity_selection(sorted_start_times, sorted_finish_times, sorted_indices, last_selected=0)
    
    m = last_selected + 1
    n = len(start_times)
    while m < n and  start_times[m] < finish_times[last_selected]:
        m += 1

    if m < n:
        return [indices[m]] + greedy_recursive_activity_selection(start_times, finish_times, indices, last_selected=m)
    else:
        return []


class TextActivitySelectionGreedyIterative(unittest.TestCase):

    def test_general(self):
        start_times = [1, 3, 0, 5, 3, 5, 6, 8, 8, 2, 12]
        finish_times = [4, 5, 6, 7, 9, 9, 10, 11, 12, 14, 16]

        expected = [0, 3, 7, 10]

        self.assertListEqual(
            greedy_iterative_activity_selection(start_times, finish_times), expected
        )

class TextActivitySelectionGreedyRecursive(unittest.TestCase):

    def test_general(self):
        start_times = [1, 3, 0, 5, 3, 5, 6, 8, 8, 2, 12]
        finish_times = [4, 5, 6, 7, 9, 9, 10, 11, 12, 14, 16]

        expected = [0, 3, 7, 10]

        self.assertListEqual(
            greedy_recursive_activity_selection(start_times, finish_times), expected
        )


if __name__ == "__main__":
    unittest.main()
