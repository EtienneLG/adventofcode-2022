trees = [[int(x) for x in t] for t in open("day08.txt").read().split("\n")]

visible = []
for i in range(len(trees[0])):
    last_up = -1
    for j in range(len(trees)):
        if trees[j][i] > last_up:
            visible.append((j, i))
            last_up = trees[j][i]

    last_down = -1
    for j in range(len(trees)):
        if trees[-j-1][i] > last_down:
            visible.append((len(trees) - j - 1, i))
            last_down = trees[-j-1][i]

for i in range(len(trees)):
    last_left = -1
    for j in range(len(trees[0])):
        if trees[i][j] > last_left:
            visible.append((i, j))
            last_left = trees[i][j]

    last_right = -1
    for j in range(len(trees[0])):
        if trees[i][-j-1] > last_right:
            visible.append((i, len(trees) - j - 1))
            last_right = trees[i][-j-1]

def search_vision(r, step_x, step_y, tree):
    see = 0
    for d in range(r):
        see += 1
        if trees[i + step_x * (d + 1)][j + step_y * (d + 1)] >= tree: break
    return see

scores = []
for i in range(len(trees)):
    for j in range(len(trees[i])):
        tree = trees[i][j]

        up = search_vision(i, -1, 0, tree)
        down = search_vision(len(trees) - i - 1, 1, 0, tree)
        left = search_vision(j, 0, -1, tree)
        right = search_vision(len(trees[i]) - j - 1, 0, 1, tree)

        scores.append(up * down * left * right)

print(len(set(visible)))
print(max(scores))