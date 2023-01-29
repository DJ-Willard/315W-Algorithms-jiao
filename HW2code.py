import heapq
import sys

def find_longest_path(n, m, edges):
    # Initialize the distance and count arrays
    distance = [float("-inf")] * (n + 1)
    count = [1] * (n + 1)
    distance[1] = 0
    current_max = 0
    adj_list = [[] for i in range(n+1)]
    for u, v, w in edges:
        adj_list[u].append((v, w))

    # Run Dijkstra algorithm
    visited = [False] * (n + 1)
    heap = [(0, 1)]
    while heap:
        (dist, node) = heapq.heappop(heap)
        if visited[node]:
            continue
        visited[node] = True
        distance[node] = dist
        for v, w in adj_list[node]:
            if dist + w >= current_max:
                heapq.heappush(heap, (dist + w, v))
                if dist + w > current_max:
                    current_max = dist + w
                    count[v] = count[node]
                elif dist + w == current_max:
                    count[v] += count[node]

    # Find the longest path
    longest_path = distance[n]
    num_longest_paths = count[distance.index(longest_path)]
    return longest_path, num_longest_paths

def main():
    n, m = map(int, input().strip().split())
    edges = [tuple(map(int, line.strip().split())) for line in sys.stdin]
    longest_path, num_longest_paths = find_longest_path(n, m, edges)
    print("longest path:", longest_path)
    print("number of longest paths:", num_longest_paths)

if __name__ == "__main__":
    main()
