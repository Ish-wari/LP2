n = int(input("Enter number of vertices: "))
e = int(input("Enter number of edges: "))
graph = {} # Create empty graph
#for i in range(1,n+1):   # or for i in range(1,n+1)
 #   graph[i] = []
print("Enter edges and weights:")
for i in range(e):
    u, v, w =  input().split()
    w=int(w)
    if u not in graph:
        graph[u] = []
    if v not in graph:
        graph[v] = []
    graph[u].append((v, w))
    graph[v].append((u, w))
print("\nGraph = ")
print(graph)
start = (input("\nEnter starting vertex: "))
selected = []  ## Start from vertex 0
selected.append(start)
total = 0
print("\nEdge \tWeight")
while len(selected) < len(graph):
    minimum = 999
    x = " "
    y = " "
    for i in selected:   # # Check selected vertices
        for j, weight in graph[i]:   # Check neighbours
            if j not in selected:     # Vertex should not already be selected
                if weight < minimum:   ## Find minimum edge
                    minimum = weight
                    x = i
                    y = j
    print(x, "-", y, "\t", minimum)
    total += minimum
    selected.append(y)
print("\nTotal Cost =", total)

















# # Prim's Minimum Spanning Tree - Simple Version

# n = int(input("Enter number of vertices: "))

# # Input graph
# graph = []

# print("Enter adjacency matrix:")

# for i in range(n):
#     row = list(map(int, input().split()))
#     graph.append(row)

# # Track selected vertices
# selected = [False] * n

# # Start from vertex 0
# selected[0] = True

# print("\nEdges in MST:")

# total = 0

# # MST needs n-1 edges
# for k in range(n - 1):

#     minimum = 999
#     a = 0
#     b = 0

#     # Find minimum edge
#     for i in range(n):

#         if selected[i]:

#             for j in range(n):

#                 if not selected[j] and graph[i][j] != 0:

#                     if graph[i][j] < minimum:

#                         minimum = graph[i][j]
#                         a = i
#                         b = j

#     print(a, "-", b, "=", minimum)

#     total = total + minimum

#     selected[b] = True

# print("\nTotal Cost =", total)