DEAD = -float('inf')


def calc(scores, r, you, counts):
    player_count = sum(x != DEAD for x in scores)
    if player_count % 2:
        killed_player = scores.index(max(scores))
        if killed_player == you:
            return 0
        scores[killed_player] = DEAD

    key = tuple(scores)
    if key in counts:
        return counts[key]

    night_count = 1
    for killed_player in range(n):
        if killed_player == you or scores[killed_player] == DEAD:
            continue
        new_scores = [x + y for x, y in zip(scores, r[killed_player])]
        new_scores[killed_player] = DEAD
        night_count = max(night_count,
                          1 + calc(new_scores, r, you, counts))
    counts[key] = night_count
    return night_count


n = int(input())
scores = list(map(int, input().split()))
r = [list(map(int, input().split())) for i in range(n)]
you = int(input())

print(calc(scores, r, you, {}))