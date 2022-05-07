from copy import deepcopy

def isFinal(CS):
	for S in CS:
		if CS[0]==1:
			return False
	return True

n = int(input("No.of rooms : "))
IS = [[0,0] for i in range(n)]
D = list(map(int, input("Enter dirty rooms : ").split()))
for r in D:
	IS[r-1][0]=1
IR = int(input("Initial room in which VC is present : "))
IS[IR-1][1] = 1

StackS = list()
StackS.append(IS)
StackR = list()
StackR.append(IR-1)
Processed = list()

while len(StackS)!=0:
    CS = StackS.pop()
    CR = StackR.pop()
    
    if CS in Processed:
        pass
    else:
        Processed.append(CS)
        if CS[CR][0]==1:
            A = deepcopy(CS)
            A[CR][0]=0
            StackS.append(A)
            StackR.append(CR)
        if CR!=0:
            A = deepcopy(CS)
            A[CR][1]=0
            A[CR-1][1]=1
            StackS.append(A)
            StackR.append(CR-1)
        if CR!=n-1:
            A = deepcopy(CS)
            A[CR][1]=0
            A[CR+1][1]=1
            StackS.append(A)
            StackR.append(CR+1)

for State in Processed:
    print(State)