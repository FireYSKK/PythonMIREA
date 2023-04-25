import tttm


def make_model(game, start_state):
    states = dict()

    def iterate(current_state):
        nonlocal states
        if current_state in states:
            return

        states[current_state] = set()
        active_player_ind = 1 if current_state[0] == 'alice' else 2
        options = game[current_state[active_player_ind]].copy()
        for option in options:
            next_states = options[option](current_state)
            for next_state in next_states:
                states[current_state].add(next_state)
                iterate(next_state)

    iterate(start_state)

    dest = []
    for state in states:
        if tttm.is_goal_state(state):
            dest.append(state)

    return states, dest


def BFS(adj, src, dest, v, pred, dist):
    queue = []

    visited = [False for _ in range(v)]

    visited[src] = True
    dist[src] = 0
    queue.append(src)

    while len(queue) != 0:
        u = queue[0]
        queue.pop(0)
        for i in adj[u]:
            if not visited[i]:
                visited[i] = True
                dist[i] = dist[u] + 1
                pred[i] = u
                queue.append(i)

                if i == dest:
                    return True

    return False


def print_shortest_path(adj, s, dest):
    v = len(adj)
    pred = [-1 for _ in range(v)]
    dist = [1000000 for _ in range(v)]

    if not BFS(adj, s, dest, v, pred, dist):
        print("Given source and destination are not connected")

    crawl = dest
    path = [crawl]

    while pred[crawl] != -1:
        path.append(pred[crawl])
        crawl = pred[crawl]

    return dist[dest], path


states, goals = make_model(tttm.game, tttm.START_STATE)

enum = dict((v, k) for k, v in dict(enumerate(states)).items())
adj = [[] for _ in range(len(states))]

for state in states:
    for conn in states[state]:
        adj[enum[state]].append(enum[conn])

paths = []
dmin = 100000
for i in goals:
    path = print_shortest_path(adj, 0, list(states.keys()).index(i))
    if path[0] < dmin:
        paths = [path]
        dmin = path[0]
    elif path[0] == dmin:
        paths.append(path)

print("The shortest path length:", paths[0][0])
print("Route(s):")
for path in paths:
    print(*reversed(path[1]), sep=' -> ')
