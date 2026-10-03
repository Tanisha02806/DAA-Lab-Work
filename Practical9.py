# Prim's Algorithm

'''
Time Complexity: O(V^2)
Space Complexity: O(V)

where,
V = Number of Vertices
'''

INF = float('inf')


def prim_mst(graph, n):
    selected = [False] * n
    selected[0] = True  # Start from vertex 0

    edge = 0
    cost = 0

    print("\nEdges in Minimum Spanning Tree:")

    while edge < n - 1:
        minimum = INF
        x = y = -1

        for i in range(n):
            if selected[i]:
                for j in range(n):
                    if not selected[j] and graph[i][j] < minimum:
                        minimum = graph[i][j]
                        x = i
                        y = j

        print(f"{x} --> {y}  Cost = {graph[x][y]}")
        cost += graph[x][y]
        selected[y] = True
        edge += 1

    print(f"\nMinimum Cost = {cost}")


# ======================= Main =======================
def main():
    n = int(input("Enter number of vertices: "))

    print("Enter Cost Adjacency Matrix:")

    graph = []

    for _ in range(n):
        row = list(map(int, input().split()))

        # Replace 0 (no edge) with INF except for diagonal
        for j in range(n):
            if row[j] == 0:
                row[j] = INF

        graph.append(row)

    prim_mst(graph, n)


if __name__ == "__main__":
    main()
