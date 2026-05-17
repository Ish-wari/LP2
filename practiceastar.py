goal=[[1,2,3],
      [8,0,4],
      [7,6,5]]
def print_puzzle(state):
    for row in state:
        for value in row:
            if value==0:
                print("-",end=" ")
            else:
                print(value,end=" ")
        print()
def heuristic(state):
    count=0
    for i in range(3):
        for j in range(3):
            if state[i][j]!=0 and state[i][j]!=goal[i][j]:
                count+=1
    return count
def find_blank(state):
    for i in range(3):
        for j in range(3):
            if state[i][j]==0:
                return i,j
def generate_moves(state):
    moves=[]
    x,y=find_blank(state)
    direction=[(-1,0),(1,0),(0,-1),(0,1)]
    for dx,dy in direction:
        new_x=x+dx
        new_y=y+dy
        if 0<=new_x < 3 and 0<= new_y <3:
            new_state=[]
            for row in state:
                new_state.append(row[:])
            new_state[x][y]=new_state[new_x][new_y]
            new_state[new_x][new_y]=0
            moves.append(new_state)
    return moves
def astar(start):
    open_list=[]
    visited=[]
    open_list.append((start,0))
    while open_list:
        open_list.sort(key=lambda x: x[1]+heuristic(x[0]))
        current_state,level=open_list.pop(0)
        print("Current state")
        print_puzzle(current_state)
        if(current_state==goal):
            print("Goal reached")
            return
        visited.append(current_state)
        next_moves=generate_moves(current_state)
        for move in next_moves:
            if move not in visited:
                open_list.append((move,level+1))
print("enter the initial state")
print(" //0 means blank space ")
start=[]
for i in range(3):
    row=list(map(int,input().split()))
    start.append(row)
print("Initial state:")
print_puzzle(start)
astar(start)

