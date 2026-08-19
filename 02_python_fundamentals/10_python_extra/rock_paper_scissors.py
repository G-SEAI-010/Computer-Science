# ____________________________________________
# _________________ Lösung 1 _________________
# ____________________________________________

import sys
import random

valid_moves = ["Schere", "Stein", "Papier"]

if len(sys.argv) < 2:
    print(f"Bitte gib deinen Zug an: {', '.join(valid_moves)}")
    sys.exit(1)

player_move = sys.argv[1].capitalize()
if player_move not in valid_moves:
    print(f"Ungültiger Zug. Wähle aus: {', '.join(valid_moves)}")
    sys.exit(1)

computer_move = random.choice(valid_moves)

if player_move == computer_move:
    result = "Unentschieden!"
elif (
    (player_move == "Stein" and computer_move == "Schere")
    or (player_move == "Schere" and computer_move == "Papier")
    or (player_move == "Papier" and computer_move == "Stein")
):
    result = "Du gewinnst!"
else:
    result = "Du verlierst!"

print(f"Du hast {player_move} gewählt. Der Computer wählte {computer_move}. {result}")

# ____________________________________________
# _________________ Lösung 2 _________________
# ____________________________________________

# import random

# print("Willkommen bei Schere, Stein, Papier!")
# print("Tippe 'Ende', um das Spiel zu beenden.")
# print("-" * 30)

# valid_moves = ["Schere", "Stein", "Papier"]

# while True:
#     player_move = (
#         input(f"\nBitte gib deinen Zug ein ({', '.join(valid_moves)}): ")
#         .strip()
#         .capitalize()
#     )

#     if player_move == "Ende":
#         print("Danke fürs Spielen! Bis zum nächsten Mal.")
#         break

#     if player_move not in valid_moves:
#         print(f"Ungültiger Zug. Bitte wähle aus: {', '.join(valid_moves)} oder 'Ende'.")
#         continue

#     computer_move = random.choice(valid_moves)

#     if player_move == computer_move:
#         result = "Unentschieden!"
#     elif (
#         (player_move == "Stein" and computer_move == "Schere")
#         or (player_move == "Schere" and computer_move == "Papier")
#         or (player_move == "Papier" and computer_move == "Stein")
#     ):
#         result = "Du gewinnst!"
#     else:
#         result = "Du verlierst!"

#     print(
#         f"Du hast {player_move} gewählt. Der Computer wählte {computer_move}. {result}"
#     )

# ____________________________________________
# _________________ Lösung 3 _________________
# ____________________________________________

# import sys
# import random

# valid_moves = ("Schere", "Stein", "Papier")
# wins = {
#     "Stein": "Schere",
#     "Schere": "Papier",
#     "Papier": "Stein",
# }

# if len(sys.argv) < 2:
#     print(f"Bitte gib deinen Zug an: {', '.join(valid_moves)}")
#     sys.exit(1)

# player_move = sys.argv[1].capitalize()

# if player_move not in valid_moves:
#     print(f"Ungültiger Zug. Wähle aus: {', '.join(valid_moves)}")
#     sys.exit(1)

# computer_move = random.choice(valid_moves)

# if player_move == computer_move:
#     result = "Unentschieden!"
# elif wins[player_move] == computer_move:
#     result = "Du gewinnst!"
# else:
#     result = "Du verlierst!"

# print(f"Du hast {player_move} gewählt. Der Computer wählte {computer_move}. {result}")
