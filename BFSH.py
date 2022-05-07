v = int(input('Enter No.of Vertices : '))
Vertices = dict()
Graph = dict()
for i in range(v):
    a,b = input('Enter vertex name and Heuristic value : ').split()
    V[str(a)] = int(b)
    G[str(a)] = list()

Vertices = dict(sorted(Vertices.items(), key = lambda V:(V[1], V[0])))

e = int(input('Enter No.of Edges    : '))
for i in range(e):
    a,b = input('Enter the edge points : ').split()
    Graph[str(a)].append(str(b))

Start = str(input('Enter initial vertex : '))
Goal = str(input('Enter goal vertex    : '))

Open = dict()
Closed = dict()

Open[S] = V[S]

while len(Open)!=0:
    Open = dict(sorted(Open.items(), key = lambda Open:(Open[1], Open[0])))
    Key = list(Open.keys())[0]
    Closed[Key] = Open[Key]
    Open.pop(Key)
    if Key==Goal:
        break
    else:
        for i in Graph[Key]:
            Open[i] = Vertices[i]

print(*list(Closed.keys()),sep=" ---> ")