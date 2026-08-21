# Lösung 1 - Zeit O(n²), Speicher O(1)


def can_attend_meetings(intervals):
    def overlap(interval1, interval2):
        return (
            interval1[0] >= interval2[0]
            and interval1[0] < interval2[1]
            or interval2[0] >= interval1[0]
            and interval2[0] < interval1[1]
        )

    for i in range(len(intervals)):
        for j in range(i + 1, len(intervals)):
            if overlap(intervals[i], intervals[j]):
                return False

    return True


print(can_attend_meetings([[0, 30], [5, 10], [15, 20]]))  # False
# overlap([0,30], [5,10]): ist 5 >= 0 und 5 < 30? Ja → gibt sofort False zurück

print(can_attend_meetings([[7, 10], [2, 4]]))  # True
# overlap([7,10], [2,4]): ist 7 >= 2 und 7 < 4? Nein. Ist 2 >= 7? Nein → keine Überschneidung
# → gibt True zurück

print()

# Lösung 2 - Zeit O(n log n), Speicher O(1)


def can_attend_meetings_range_sort(intervals):
    intervals.sort(key=lambda x: x[0])

    for i in range(len(intervals) - 1):
        if intervals[i][1] > intervals[i + 1][0]:
            return False

    return True


print(can_attend_meetings_range_sort([[0, 30], [5, 10], [15, 20]]))  # False

print(can_attend_meetings_range_sort([[7, 10], [2, 4]]))  # True

print()

# Lösung 2 (alternativ)

from itertools import pairwise


def can_attend_meetings_sort(intervals):
    intervals.sort(key=lambda x: x[0])

    for prev, curr in pairwise(intervals):
        if prev[1] > curr[0]:
            return False

    return True


print(can_attend_meetings_sort([[0, 30], [5, 10], [15, 20]]))  # False

print(can_attend_meetings_sort([[7, 10], [2, 4]]))  # True
