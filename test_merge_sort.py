
import merge_sort

def test_merge_sort():
    assert merge_sort.merge_sort([[11, 6, 4, 1, 48, 113, 3, 9, 17]]) == [1, 3, 4, 6, 9, 11, 17, 48, 113]

def test_merge_sort2():
    assert merge_sort.merge_sort([11, 6, 4, 1, 48, 113, 3, 9, 17]) == [1, 3, 4, 6, 9, 11, 17, 48, 113]
