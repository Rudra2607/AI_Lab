v = int(input("Enter no.of nodes : "))
e = int(input("Enter no.of edges : "))
graph = [[0 for i in range(v)] for j in range(v)]

for i in range(e):
    a,b,w = map(int, input("Enter edge points and weight : ").split())
    graph[a][b] = w
    graph[b][a] = w

# graph = [[0,20,40,22],[20,0,13,30],[40,13,0,12],[22,30,12,0]]

print(graph)

start  = int(input("Start node : "))
key = start
Processed = []
select = -1

while True:
    if len(Processed)==v or select==start:
        break
    
    available = []
    mx = 1e9
    select = -1
    for i in range(v):
        if graph[key][i]!=0 and mx>graph[key][i] and i not in Processed:
            select = i
            mx = graph[key][i]
    
    Processed.append(select)
    key = select

print(*([start]+Processed), sep=" --> ")