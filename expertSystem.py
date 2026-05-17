
issues = {
    "internet not working": "Start",
    "slow internet": "Restart Router",
    "no connection": "Check Cable"
}


# -----------------------------------------------------
# GRAPH
# -----------------------------------------------------
# Stores troubleshooting steps

graph = {
    "Start": ["Check Cable", "Restart Router"],

    "Check Cable": ["Replace Cable", "Contact Support"],

    "Restart Router": ["Check Firmware", "Resolved"],

    "Check Firmware": ["Update Firmware", "Reset Router"],

    "Replace Cable": ["Resolved"],
    "Reset Router": ["Resolved"],
    "Update Firmware": ["Resolved"],
    "Contact Support": ["Resolved"],

    "Resolved": []
}


# -----------------------------------------------------
# COST FOR A* SEARCH
# -----------------------------------------------------
# Smaller cost = better option

costs = {
    "Start": 1,
    "Check Cable": 2,
    "Restart Router": 2,
    "Check Firmware": 3,
    "Replace Cable": 4,
    "Reset Router": 3,
    "Update Firmware": 4,
    "Contact Support": 5,
    "Resolved": 0
}


# =====================================================
# BFS ALGORITHM
# =====================================================

def bfs(start, goal):

    queue = [[start]]
    visited = []

    while queue:

        path = queue.pop(0)
        node = path[-1]

        if node == goal:
            return path

        if node not in visited:

            visited.append(node)

            for neighbor in graph[node]:

                new_path = path + [neighbor]
                queue.append(new_path)

    return None


# =====================================================
# DFS ALGORITHM
# =====================================================

def dfs(start, goal, path=[]):

    path = path + [start]

    if start == goal:
        return path

    for neighbor in graph[start]:

        if neighbor not in path:

            result = dfs(neighbor, goal, path)

            if result:
                return result

    return None


# =====================================================
# A* SEARCH
# =====================================================

def a_star(start, goal):

    open_list = [(start, [start], 0)]

    while open_list:

        # sort according to cost
        open_list.sort(key=lambda x: x[2])

        node, path, total_cost = open_list.pop(0)

        if node == goal:
            return path

        for neighbor in graph[node]:

            new_cost = total_cost + costs[neighbor]

            open_list.append(
                (neighbor, path + [neighbor], new_cost)
            )

    return None


# =====================================================
# SELECTION SORT
# =====================================================

def selection_sort(tickets):

    n = len(tickets)

    for i in range(n):

        min_index = i

        for j in range(i + 1, n):

            if tickets[j][1] < tickets[min_index][1]:
                min_index = j

        tickets[i], tickets[min_index] = \
            tickets[min_index], tickets[i]

    return tickets
def prim_mst(matrix):

    n = len(matrix)

    selected = [False] * n

    selected[0] = True

    edges = []

    for i in range(n - 1):

        minimum = 999
        x = 0
        y = 0

        for row in range(n):

            if selected[row]:

                for col in range(n):

                    if not selected[col] and matrix[row][col] != 0:

                        if matrix[row][col] < minimum:

                            minimum = matrix[row][col]
                            x = row
                            y = col

        edges.append((x, y, minimum))

        selected[y] = True

    return edges



# TICKET MANAGEMENT SYSTEM


def ticket_system():

    tickets = []

    n = int(input("\nEnter number of tickets: "))

    for i in range(n):

        ticket_id = input("Enter Ticket ID: ")

        priority = int(input(
            "Enter Priority (small number = urgent): "
        ))

        tickets.append((ticket_id, priority))

    sorted_tickets = selection_sort(tickets)

    print("\nSorted Tickets:")

    for ticket in sorted_tickets:
        print(ticket)



# NETWORK OPTIMIZATION SYSTEM


def network_system():

    matrix = [
        [0, 2, 0, 6],
        [2, 0, 3, 8],
        [0, 3, 0, 0],
        [6, 8, 0, 0]
    ]

    mst = prim_mst(matrix)

    print("\nMinimum Spanning Tree:")

    for edge in mst:
        print(edge)


# HELP DESK SYSTEM
def help_desk():

    issue = input("\nEnter issue: ").lower()

    if issue in issues:

        start = issues[issue]

        print("\n1. BFS Solution")
        bfs_path = bfs(start, "Resolved")
        print(bfs_path)

        print("\n2. DFS Solution")
        dfs_path = dfs(start, "Resolved")
        print(dfs_path)

        print("\n3. A* Solution")
        a_star_path = a_star(start, "Resolved")
        print(a_star_path)

    else:
        print("Issue not found!")



def main():

    while True:

        print("\n========== MAIN MENU ==========")
        print("1. Solve Issue")
        print("2. Manage Tickets")
        print("3. Network Setup")
        print("4. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            help_desk()

        elif choice == 2:
            ticket_system()

        elif choice == 3:
            network_system()

        elif choice == 4:
            print("Thank You")
            break

        else:
            print("Invalid Choice")


# =====================================================
# START PROGRAM
# =====================================================

main()


