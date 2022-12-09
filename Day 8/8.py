import os

local_file = os.path.join(os.path.dirname(__file__), 'input_1.txt')

file = open(local_file,  "r")

data = file.read().splitlines()

def f_vis_grid():

    trees = [list(line) for line in data]
    vis = [[False for _ in r_vis] for r_vis in trees]

    for _ in range(4):

        # reverse matrix
        trees = [[trees[k][n] for k in range(len(trees))] for n in range(len(trees[0]) - 1, - 1, - 1)]
        vis = [[vis[k][n] for k in range(len(vis))] for n in range(len(vis[0]) - 1, - 1, - 1)]

        for n, r_tree in enumerate(trees):

            high = r_tree[0]
            vis[n][0] = True

            for k, tree in enumerate(r_tree[1:], start=1):
                if tree > high:
                    vis[n][k] = True
                    high = tree

    flat_vis = []
    for sub in vis:
        for item in sub:
            flat_vis.append(item)
    return sum(flat_vis)

print(f_vis_grid())
