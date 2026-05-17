# Kruskal's Minimum Spanning Tree Algorithm

# Function to find parent
def find(parent, vertex):

    if parent[vertex] == vertex:
        return vertex

    return find(parent, parent[vertex])


# Function to join two sets
def union(parent, u, v):

    root_u = find(parent, u)
    root_v = find(parent, v)

    parent[root_v] = root_u


# Input number of edges
e = int(input("Enter number of edges: "))

edges = []

print("Enter edges and weights:")

# Example:
# A B 2
# 1 2 5

for i in range(e):

    u, v, w = input().split()

    w = int(w)

    edges.append((w, u, v))

# Sort edges according to weight
edges.sort()

# Create parent dictionary
parent = {}

for w, u, v in edges:

    if u not in parent:
        parent[u] = u

    if v not in parent:
        parent[v] = v

print("\nSorted Edges:")
print(edges)

print("\nEdges in Minimum Spanning Tree:\n")

total = 0
mst_edges = 0

# Process edges
for w, u, v in edges:

    # Check if cycle forms
    if find(parent, u) != find(parent, v):

        # Add edge to MST
        print(u, "-", v, "=", w)

        total += w

        mst_edges += 1

        # Join sets
        union(parent, u, v)

    # Stop when MST complete
    if mst_edges == len(parent) - 1:
        break

print("\nTotal Cost =", total)