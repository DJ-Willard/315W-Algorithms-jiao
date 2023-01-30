import sys

def find_longest_path(n, m, edges):
    # Initialize the distance and count arrays
    distance = [float("-inf")] * (n + 1)
    count = [0] * (n + 1)
    distance[1] = 0
    count[1] = 1

    # Run Bellman-Ford algorithm
    for _ in range(n - 1):
        for i in range(m):
            u, v, w = edges[i]
            if distance[u] != float("-inf") and distance[v] < distance[u] + w:
                distance[v] = distance[u] + w
                count[v] = count[u]
            elif distance[u] != float("-inf") and distance[v] == distance[u] + w:
                count[v] += count[u]

    # Find the longest path
    longest_path = max(distance)
    num_longest_paths = count[distance.index(longest_path)]
    return longest_path, num_longest_paths

def main(input_file):
    with open(input_file, "r") as f:
        n, m = map(int, f.readline().strip().split())
        edges = [tuple(map(int, line.strip().split())) for line in f]
        longest_path, num_longest_paths = find_longest_path(n, m, edges)
        print("longest path:", longest_path)
        print("number of longest paths:", num_longest_paths)

if __name__ == "__main__":
    input_file = sys.argv[1]
    main(input_file)
