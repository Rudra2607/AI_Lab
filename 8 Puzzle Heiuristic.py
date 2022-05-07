import copy

def heuristic(CS,FS):
    h=0
    for i in range(3):
        for j in range(3):
            if CS[i][j]!=FS[i][j]:
                h+=1
    return h

# print("Enter initial state : ")
# IS = list()
# for i in range(3):
#     row = list(map(int, input().split()))
#     IS.append(row)

# print("Enter final state : ")
# FS = list()
# for i in range(3):
#     row = list(map(int, input().split()))
#     FS.append(row)

FS = [[1,2,3],[4,5,6],[7,8,0]]
IS = [[1,2,3],[5,0,6],[4,7,8]]
#IS = [[1,2,3],[0,4,6],[7,5,8]]
# IS = [[1,2,3],[8,0,4],[7,6,5]]
# FS = [[2,8,1],[0,4,3],[7,6,5]]

Processed = list()
Stack = dict()
for i in range(10):
    Stack[i] = list()

Stack[heuristic(IS,FS)].append(IS)
print(Stack)

c=0
while True:
    c+=1
    for i in range(9):
        print(Stack[i])
    for i in range(9):
        try:
            P = copy.deepcopy(Stack[i].pop())
            break
        except:
            pass
    
    for i in P:
        print(i)
    print()
    
    if P==FS:
        print('Final State : ')
        print(P)
        break
    else:
        Processed.insert(0,P)
        x=-1
        y=-1
        for i in P:
            x+=1
            if 0 in i:
                for j in i:
                    y+=1
                    if j==0:
                        break
                break
        
        if y!=0:
            L = copy.deepcopy(P)
            L[x][y-1] = P[x][y]
            L[x][y] = P[x][y-1]
            if L not in Processed:
                Stack[heuristic(L,FS)].append(L)
        
        if y!=2:
            R = copy.deepcopy(P)
            R[x][y+1] = P[x][y]
            R[x][y] = P[x][y+1]
            if R not in Processed:
                Stack[heuristic(R,FS)].append(R)
        
        if x!=0:
            U = copy.deepcopy(P)
            U[x-1][y] = P[x][y]
            U[x][y] = P[x-1][y]
            if U not in Processed:
                Stack[heuristic(U,FS)].append(U)
        
        if x!=2:
            D = copy.deepcopy(P)
            D[x+1][y] = P[x][y]
            D[x][y] = P[x+1][y]
            if D not in Processed:
                Stack[heuristic(D,FS)].append(D)

print("Total states traversed :",c)