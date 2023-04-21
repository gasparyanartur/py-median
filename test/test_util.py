from src.util import count_items, get_median


def test_get_counts():
    items = [1, 1, 1, 3, 3, 4, 5, 6, 8, 8]
    counts = count_items(items)
    assert counts == [0, 3, 0, 2, 1, 1, 1, 0, 2]


def test_count_items_empty():
    items = []
    counts = count_items(items)
    assert counts == []


def test_count_items_single():
    items = [1]
    counts = count_items(items)
    assert counts == [0, 1]


def test_median_single():
    counts = [3]
    median = get_median(counts)
    assert median == 0


def test_get_median_odd():
    items = [1, 1, 1, 3, 4, 5, 6, 8, 8]
    counts = count_items(items)
    median = get_median(counts)
    assert median == 4


def test_get_median_empty():
    counts = []
    median = get_median(counts)
    assert median == None


def test_get_median_even():
    items = [1, 1, 3, 3, 4, 5, 6, 8, 8, 9]
    counts = count_items(items)
    median = get_median(counts)
    assert median == 3.5


def test_get_median_even_double():
    items = [1, 1, 3, 3, 4, 4, 6, 7, 8, 8, 9]
    counts = count_items(items)
    median = get_median(counts)
    assert median == 4.0