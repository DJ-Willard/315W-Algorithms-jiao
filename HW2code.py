import sys

def find_longest_path(n, m, edges):
    # Initialize the distance and count arrays
    distance = [float("-inf")] * (n + 1)
    count = [0] * (n + 1)
    distance[1] = 0
    count[1] = 1
    # Run Bellman-Ford algorithm
    for _ in range(n):
        updates = 0
        for i in range(m):
            u, v, w = edges[i]
            if distance[u] != float("-inf") and distance[v] < distance[u] + w:
                distance[v] = distance[u] + w
                count[v] = count[u]
                updates += 1
            elif distance[u] != float("-inf") and distance[v] == distance[u] + w:
                count[v] += count[u]
        if updates == 0:
            break
    if updates > 0:
        print("Negative cycle detected!")
        return None, None
        # Find the longest path
    longest_path = max(distance)
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