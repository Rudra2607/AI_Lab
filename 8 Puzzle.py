import copy

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
# IS = [[1,2,3],[0,4,6],[7,5,8]]
# IS = [[1,2,3],[8,0,4],[7,6,5]]
# FS = [[2,8,1],[0,4,3],[7,6,5]]

Processed = list()
Queue = list()

Queue.append(IS)
c=0
while len(Queue)!=0:
    c+=1
    P = copy.deepcopy(Queue.pop())
    
    for i in P:
        print(i)
    print()
    
    if P==FS:
        print('Final State : ')
        print(P)
        break
    elif P in Processed:
        pass
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
            Queue.insert(0,L)
        
        if y!=2:
            R = copy.deepcopy(P)
            R[x][y+1] = P[x][y]
            R[x][y] = P[x][y+1]
            Queue.insert(0,R)
        
        if x!=0:
            U = copy.deepcopy(P)
            U[x-1][y] = P[x][y]
            U[x][y] = P[x-1][y]
            Queue.insert(0,U)
        
        if x!=2:
            D = copy.deepcopy(P)
            D[x+1][y] = P[x][y]
            D[x][y] = P[x+1][y]
            Queue.insert(0,D)

print("Total states traversed :",c)