# Lösung 1 - Zeit O(n), Speicher O(n)
def dest_city(paths):
    departures = {path[0] for path in paths}

    for path in paths:
        destination = path[1]
        if destination not in departures:
            return destination

    return None


# print(dest_city([["London", "New York"], ["New York", "Lima"], ["Lima", "Sao Paulo"]]))
# print(dest_city([["B", "C"], ["D", "B"], ["C", "A"]]))
# print(dest_city([["A", "Z"]]))


# Lösung 2 - Zeit O(n²), Speicher O(1)
def dest_city_quadratic(paths):
    for i in range(len(paths)):
        candidate = paths[i][1]
        good = True
        for j in range(len(paths)):
            if paths[j][0] == candidate:
                good = False
                break
        if good:
            return candidate

    return None


# print(
#     dest_city_quadratic(
#         [["London", "New York"], ["New York", "Lima"], ["Lima", "Sao Paulo"]]
#     )
# )
# print(dest_city_quadratic([["B", "C"], ["D", "B"], ["C", "A"]]))
# print(dest_city_quadratic([["A", "Z"]]))


# Lösung 3 - Zeit O(n), Speicher O(n)
def dest_city_sets(paths):
    starts = {path[0] for path in paths}
    destinations = {path[1] for path in paths}

    return (destinations - starts).pop()


# print(
#     dest_city_sets(
#         [["London", "New York"], ["New York", "Lima"], ["Lima", "Sao Paulo"]]
#     )
# )
# print(dest_city_sets([["B", "C"], ["D", "B"], ["C", "A"]]))
# print(dest_city_sets([["A", "Z"]]))
