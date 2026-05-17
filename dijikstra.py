e = int(input("Enter number of edges: "))
graph = {}
print("Enter edges and weights:")
for i in range(e):
    u, v, w = input().split()
    w = int(w)
    if u not in graph:
        graph[u] = []
    if v not in graph:
        graph[v] = []
    graph[u].append((v, w))
    graph[v].append((u, w))
print("\nGraph = ")
print(graph)
start = input("\nEnter source vertex: ")
distance = {}
for vertex in graph:
    distance[vertex] = 999
distance[start] = 0
visited = []
while len(visited) < len(graph):
    minimum = 999
    u = ""
    for vertex in distance: # Find minimum distance vertex
        if vertex not in visited and distance[vertex] < minimum:
            minimum = distance[vertex]
            u = vertex
    visited.append(u)
    for neighbour, weight in graph[u]:   # Update neighbours
        if neighbour not in visited:
            new_distance = distance[u] + weight
            if new_distance < distance[neighbour]:
                distance[neighbour] = new_distance
print("\nShortest Distances:")
for vertex in distance:
    print(start, "->", vertex, "=", distance[vertex])


    