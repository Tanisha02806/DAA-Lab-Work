# Floyd-Warshall Algorithm

'''
Time Complexity: O(V^3)
Space Complexity: O(V^2)

where,
V = number of vertices
'''

from itertools import product

INF = 9999


def floyd_warshall(graph, n):
    # Floyd-Warshall Algorithm
    for k, i, j in product(range(n), repeat=3):
        if graph[i][k] != INF and graph[k][j] != INF:
            distance = graph[i][k] + graph[k][j]
            if distance < graph[i][j]:
                graph[i][j] = distance


def main():
    n = int(input("Enter number of vertices: "))

    print("Enter Cost Matrix (Enter 9999 for Infinity):")

    graph = []

    for _ in range(n):
        row = list(map(int, input().split()))
        graph.append(row)

    floyd_warshall(graph, n)

    print("\nShortest Distance Matrix:")

    for i in range(n):
        for j in range(n):
            if graph[i][j] == INF:
                print("INF".ljust(5), end="")
            else:
                print(f"{graph[i][j]:4}", end=" ")
        print()


if __name__ == "__main__":
    main()