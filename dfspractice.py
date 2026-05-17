from collections import deque
graph={}
def add_edge(u,v):
    if u not in graph:
        graph[u]=[]
    if v not in graph:
        graph[v]=[]
    graph[u].append(v)
    graph[v].append(u)
def dfs(vertex,visited):
    visited.add(vertex)
    print(vertex,end=" ")
    for neighbour in graph[vertex]:
        if neighbour not in visited:
            dfs(neighbour,visited)
def bfs(start):
    visited=set()
    queue=deque()
    queue.append(start)
    visited.add(start)
    while queue:
        vertex=queue.popleft()
        print(vertex,end=" ")
        for neighbour in graph[vertex]:
            if neighbour not in visited:
                queue.append(neighbour)
                visited.add(neighbour)
def display_graph():
    print("Adjacency matrix of graph")
    for vertex in graph:
        print(vertex,"-> ", graph[vertex])
while True:
    print("\n===== MENU =====")
    print("1. Create Graph")
    print("2. Display Graph")
    print("3. Depth First Search (DFS)")
    print("4. Breadth First Search (BFS)")
    print("5. Exit")
    print("Enter your choice: ")
    ch=int(input("Enter your choice"))
    if ch==1:
        n=int(input("enter number of edges"))
        for i in range (n):
            print("  \n enter edge",i+1)
            u=input("enter first vertex : ")
            v=input("Enetr second vertex: ")
            add_edge(u,v)
    elif ch==2:
        display_graph()
    elif ch==3:
        start=input("enter starting vertex: ")
        if start not in graph:
            print("Vertex not found!")

        else:
            visited = set()
            print("Dfs traversal")
            dfs(start,visited)
            print()
    elif ch==4:
        start=input("enter strting vertex of bfs:")
        if start not in graph:
            print("Vertex not found!")

        else:
            print("Bfs traversal")
            bfs(start)
            print()
    elif ch==5:
        print(" program ended")
        break
    else:
        print("invalid choice")


