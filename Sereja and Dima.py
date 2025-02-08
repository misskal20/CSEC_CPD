n = int(input())
cards = list(map(int, input().split()))

sereja, dima, left, right = 0, 0, 0, n - 1
for turn in range(n):
    card = cards[left] if cards[left] > cards[right] else cards[right]
    if turn % 2 == 0: sereja += card
    else: dima += card
    left, right = (left + 1, right) if card == cards[left] else (left, right - 1)

print(sereja, dima)
