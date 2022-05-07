n = int(input("Enter No.of nodes : "))
Graph = list()

# Using Adjacency matrix
print("Enter Adj Matrix : ")
for i in range(n):
	row = list(map(int, input().split()))
	Graph.append(row)

# Using Ajacency List
# Graph = [[1e9 for i in range(n)] for j in range(n)]
# e = int(input("Enter No.of edges : "))
# for i in range(e):
# 	a,b,w = map(int, input("Enter the edge points and weight : ").split())
# 	Graph[a][b] = w
# 	Graph[b][a] = w #iff bi-directional

# Custom Input
# Graph = [[0,2,0,0,10,0,0],[2,0,4,0,0,0,0],[0,4,0,3,0,0,6],[0,0,3,0,0,0,9],[10,0,0,0,0,7,0],[0,0,0,0,7,0,8],[0,0,6,9,0,8,0]]

for row in Graph:
	print(row)

Status = [0 for i in range(n)]
Queue = []
Processed = []

start = int(input("Enter starting node : "))
Status[start] = 1
Queue.append(start)

# key = int(input("Enter goal node : ")) # In case of searching

while len(Queue)!=0:
	start = Queue[0]
	Queue.remove(start)
	if start not in Processed:
		Processed.append(start)

	# In case of searching
# 	if start==key:
# 		print(start)
# 		break

	print(start," ==> ",end="")
	for i in range(n):
		if Graph[start][i]!=0 and Status[i]==0:
			Queue.append(i)
			Status[i]=1