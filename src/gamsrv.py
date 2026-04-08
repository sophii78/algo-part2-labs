import heapq


def dijkstra(n, adj, start):
    dist = [float("inf")] * (n + 1)
    dist[start] = 0
    pq = [(0, start)]
    while pq:
        d, u = heapq.heappop(pq)
        if d > dist[u]:
            continue
        for v, w in adj[u]:
            nd = d + w
            if nd < dist[v]:
                dist[v] = nd
                heapq.heappush(pq, (nd, v))
    return dist


def solve(n, clients, edges):
    adj = [[] for _ in range(n + 1)]
    for u, v, w in edges:
        adj[u].append((v, w))
        adj[v].append((u, w))

    client_set = set(clients)
    ans = float("inf")

    for s in range(1, n + 1):
        if s in client_set:
            continue

        dist = dijkstra(n, adj, s)
        cur_max = max(dist[c] for c in clients)

        if cur_max < ans:
            ans = cur_max

    return ans


def main():
    print("1 - Файл, 2 - Консоль")
    mode = input("Вибір: ").strip()

    if mode == "1":
        with open("gamsrv.in", "r") as f:
            data = [line.split() for line in f if line.strip()]
        n, m = map(int, data[0])
        clients = list(map(int, data[1]))
        edges = [(int(u), int(v), int(w)) for u, v, w in data[2:]]
    else:
        n, m = map(int, input("N M: ").split())
        clients = list(map(int, input("Клієнти: ").split()))
        edges = []
        for i in range(m):
            u, v, w = map(int, input(f"З'єднання {i+1}: ").split())
            edges.append((u, v, w))

    result = solve(n, clients, edges)

    if mode == "1":
        with open("gamsrv.out", "w") as f:
            f.write(str(result))
    else:
        print("Результат:", result)


if __name__ == "__main__":
    main()
