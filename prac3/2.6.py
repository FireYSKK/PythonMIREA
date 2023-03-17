import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection
import numpy as np

WIDTH = 640
HEIGHT = 360
MAX_DIST = 100
MIN_DIST = 10

leaves = []
branches = []


class Leaf:
    def __init__(self):
        self.pos = np.array([np.random.randint(WIDTH), np.random.randint(HEIGHT - 100)])
        self.reached = False

    def show(self):
        global leaves
        leaves.append(self.pos)


class Branch:
    def __init__(self, parent, pos, dir):
        self.pos = pos
        self.parent = parent
        self.dir = dir
        self.origDir = self.dir.copy()
        self.count = 0
        self.len = 5

    def reset(self):
        self.dir = self.origDir.copy()
        self.count = 0

    def next(self):
        nextDir = self.dir * self.len
        nextPos = self.pos + nextDir
        nextBranch = Branch(self, nextPos, self.dir.copy())
        return nextBranch

    def show(self):
        global branches
        if self.parent is not None:
            branches.append(np.array([self.pos, self.parent.pos]))


class Tree:
    def __init__(self):
        self.leaves = []
        self.branches = []

        for i in range(200):
            self.leaves.append(Leaf())

        pos = np.array([WIDTH / 2, HEIGHT])
        dir = np.array([0, -1])
        root = Branch(None, pos, dir)
        self.branches.append(root)

        current = root
        found = False
        while not found:
            for i in self.leaves:
                d = np.linalg.norm(current.pos - i.pos)
                if d < MAX_DIST:
                    found = True

            if not found:
                branch = current.next()
                current = branch
                self.branches.append(current)

    def grow(self):
        for leaf in self.leaves:
            closestBranch = None
            record = MAX_DIST + 1
            for branch in self.branches:
                d = np.linalg.norm(leaf.pos - branch.pos)
                if d < MIN_DIST:
                    leaf.reached = True
                    closestBranch = None
                    break
                elif d > MAX_DIST:
                    continue
                elif d < record or closestBranch is None:
                    closestBranch = branch
                    record = d

            if closestBranch is not None:
                newDir = leaf.pos - closestBranch.pos
                newDir /= np.linalg.norm(newDir)
                closestBranch.dir = closestBranch.dir + newDir
                closestBranch.count += 1

        for i in range(len(self.leaves) - 1, -1, -1):
            if self.leaves[i].reached:
                self.leaves.pop(i)

        for i in range(len(self.branches) - 1, -1, -1):
            branch = self.branches[i]
            if branch.count > 0:
                branch.dir /= branch.count + 1
                self.branches.append(branch.next())
                branch.reset()

    def show(self):
        for leaf in self.leaves:
            leaf.show()

        for branch in self.branches:
            branch.show()


tree = Tree()

tree.grow()
tree.show()

leaves_collection = np.array(leaves)

for i in range(300):
    tree.grow()

tree.show()

branches_collection = np.array(branches)

fig, ax = plt.subplots()
# Coords are messed up, so invert y-axis to make tree root in the bottom
ax.invert_yaxis()
# Lines don't display properly without scatter points
# Placing root and 2 more dots, so lines are within plot borders
# Though it shouldn't be a problem when leaves are present
ax.scatter(WIDTH / 2, HEIGHT)
ax.scatter(0, 0, alpha=0)
ax.scatter(WIDTH, 0, alpha=0)
# Drawing line for each branch object
line_segments = LineCollection(branches_collection, linewidths=(4),
                               colors="#A52A2A", linestyle='solid')

ax.add_collection(line_segments)
# Plot leaves
ax.scatter(leaves_collection[:, 0], leaves_collection[:, 1], s=100, color='g')
plt.show()
