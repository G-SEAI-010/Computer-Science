# Lösung 1 - Zeit O(n x m), Speicher O(n)


from collections import deque


def time_required_to_buy(tickets, k):
    queue = deque((i, t) for i, t in enumerate(tickets))

    time = 0

    while queue:
        person, remaining = queue.popleft()

        time += 1
        remaining -= 1

        if person == k and remaining == 0:
            return time

        if remaining > 0:
            queue.append((person, remaining))

    return time


print(time_required_to_buy([2, 3, 2], 2))
# queue: [(0,2),(1,3),(2,2)]
# t=1: pop (0,2)→(0,1), nicht k=2, wieder einreihen → [(1,3),(2,2),(0,1)]
# t=2: pop (1,3)→(1,2), nicht k=2, wieder einreihen → [(2,2),(0,1),(1,2)]
# t=3: pop (2,2)→(2,1), noch nicht fertig, wieder einreihen → [(0,1),(1,2),(2,1)]
# t=4: pop (0,1)→(0,0), nicht k=2, fertig, geht → [(1,2),(2,1)]
# t=5: pop (1,2)→(1,1), nicht k=2, wieder einreihen → [(2,1),(1,1)]
# t=6: pop (2,1)→(2,0), person==k und remaining==0 → return 6 ✓

print(time_required_to_buy([5, 1, 1, 1], 0))

print()

# Lösung 2 - Time O(n), Space O(1)


def time_required_to_buy_efficient(tickets, k):
    # Wir nutzen tickets = [2, 3, 2], k = 2 als unser laufendes Beispiel.
    # tickets[k] = tickets[2] = 2, also läuft die Warteschlange über 2 Runden.
    #
    # Die Warteschlange nach Runde dargestellt:
    # Start:   [2, 3, 2]   ← Person 0 braucht 2, Person 1 braucht 3, Person 2 (k) braucht 2
    # Runde 1: [1, 2, 1]   ← jeder kauft einmal
    # Runde 2: [0, 1, 0]   ← jeder kauft einmal, Person 2 (k) erreicht 0 → STOPP
    #
    # Gesamtsekunden = 3 (Runde 1) + 3 (Runde 2) = 6

    time = 0

    for i in range(len(tickets)):
        # tickets = [2, 3, 2], k = 2, tickets[k] = 2
        if i <= k:
            # Person i steht vor oder bei k — sie kauft jede Runde vor k.
            #
            # i=0: Person 0 braucht 2 Tickets, k braucht 2 → min(2, 2) = 2
            #      Person 0 kauft in Runde 1 und Runde 2 → steuert 2 Sekunden bei ✓
            #
            # i=1: Person 1 braucht 3 Tickets, k braucht 2 → min(2, 3) = 2
            #      Person 1 möchte 3 Runden, aber Schlange stoppt nach 2 → steuert 2 Sekunden bei ✓
            #
            # i=2: Person 2 IST k, braucht 2 Tickets → min(2, 2) = 2
            #      k kauft in Runde 1 und Runde 2 → steuert 2 Sekunden bei ✓
            #
            time += min(tickets[k], tickets[i])
        else:
            # Person i steht hinter k — sie kauft jede Runde nach k.
            # In ks letzter Runde wird k fertig und die Schlange stoppt, bevor sie i erreicht.
            # Also bekommt Person i nur tickets[k] - 1 = 2 - 1 = 1 Runde.
            #
            # Beispiel mit tickets = [2, 3, 2, 5], k = 2:
            # i=3: Person 3 braucht 5 Tickets, bekommt aber nur 1 Runde → min(1, 5) = 1
            time += min(tickets[k] - 1, tickets[i])

    return time


print(time_required_to_buy_efficient([2, 3, 2], 2))
# tickets[k]=2, also 2 Runden
# i=0 (<=k): min(2, 2) = 2
# i=1 (<=k): min(2, 3) = 2  ← Person 1 will 3, aber Schlange stoppt nach 2 Runden
# i=2 (==k): min(2, 2) = 2
# Gesamt = 2 + 2 + 2 = 6 ✓


print(time_required_to_buy_efficient([5, 1, 1, 1], 0))
