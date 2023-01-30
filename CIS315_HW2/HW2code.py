import sys

def find_longest_path(n, m, edges):
    # Initialize the distance and count arrays
    distance = [float("-inf")] * (n + 1)
    count = [1] * (n + 1)
    distance[1] = 0
    adj_list = [[] for i in range(n + 1)]
    for u, v, w in edges:
        adj_list[u].append((v, w))

    # Run Bellman-Ford algorithm
    for u in range(n):
        for v,w in adj_list[u]:
            if distance[u] != float("-inf") and distance[v] < distance[u] + w:
                distance[v] = distance[u] + w
                count[v] = count[u]
            elif distance[u] != float("-inf") and distance[v] == distance[u] + w:
                count[v] += count[u]
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