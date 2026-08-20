# Lösung 1 - Zeit O(n²), Speicher O(n)


def two_sum_enumerate(nums, target):
    for i, num_i in enumerate(nums):
        for j, num_j in enumerate(nums[i + 1 :], start=i + 1):
            if num_i + num_j == target:
                results = [i, j]
                return results

    return None


print(two_sum_enumerate([2, 7, 11, 15], 9))  # [0, 1]
# i=0, num_i=2: Teilliste [7, 11, 15] wird erstellt. j=1, num_j=7 → 2+7=9 (Ziel erreicht!) return [0, 1]

print(two_sum_enumerate([3, 2, 4], 6))  # [1, 2]
# i=0, num_i=3: Teilliste [2, 4] wird erstellt. j=1, num_j=2 → 3+2=5; j=2, num_j=4 → 3+4=7
# i=1, num_i=2: Teilliste [4] wird erstellt. j=2, num_j=4 → 2+4=6 (Ziel erreicht!) return [1, 2]

print(two_sum_enumerate([3, 3], 6))  # [0, 1]
# i=0, num_i=3: Teilliste [3] wird erstellt. j=1, num_j=3 → 3+3=6 (Ziel erreicht!) return [0, 1]

print()

# Lösung 2 - Zeit O(n²), Speicher O(1)


def two_sum_range(nums, target):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                results = [i, j]
                return results

    return None


print(two_sum_range([2, 7, 11, 15], 9))  # [0, 1]
# i=0, nums[0]=2: j=1, nums[1]=7 → 2+7=9 (Ziel erreicht!) return [0, 1]

print(two_sum_range([3, 2, 4], 6))  # [1, 2]
# i=0, nums[0]=3: j=1, nums[1]=2 → 3+2=5; j=2, nums[2]=4 → 3+4=7
# i=1, nums[1]=2: j=2, nums[2]=4 → 2+4=6 (Ziel erreicht!) return [1, 2]

print(two_sum_range([3, 3], 6))  # [0, 1]
# i=0, nums[0]=3: j=1, nums[1]=3 → 3+3=6 (Ziel erreicht!) return [0, 1]

print()

# Lösung 3 - Zeit O(n), Speicher O(n)


def two_sum_efficient(nums, target):
    seen = {}

    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i

    return None


print(two_sum_efficient([2, 7, 11, 15], 9))  # [0, 1]
# i=0, num=2: Komplement=7, seen={} → nicht gefunden. seen={2:0}
# i=1, num=7: Komplement=2, seen={2:0} → gefunden! return [0,1]

print(two_sum_efficient([3, 2, 4], 6))  # [1, 2]
# i=0, num=3: Komplement=3, seen={} → nicht gefunden. seen={3:0}
# i=1, num=2: Komplement=4, seen={3:0} → nicht gefunden. seen={3:0, 2:1}
# i=2, num=4: Komplement=2, seen={3:0, 2:1} → gefunden! return [1,2]

print(two_sum_efficient([3, 3], 6))  # [0, 1]
# i=0, num=3: Komplement=3, seen={} → nicht gefunden. seen={3:0}
# i=1, num=3: Komplement=3, seen={3:0} → gefunden! return [0,1]
