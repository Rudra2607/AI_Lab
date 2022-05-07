n,m = map(int, input("Enter the capacities of jugs : ").split())
k = int(input("Enter the amount you want to measure : "))

Jugs = [n,m]
C = [0,0]

print("1. Fill Jug 1")
print("2. Fill Jug 2")
print("3. Empty Jug 1")
print("4. Empty Jug 2")
print("5. Transfer from Jug 1 to Jug 2")
print("6. Transfer from Jug 2 to Jug 1")
print("7. Transfer from Jug 1 to Jug 2 and empty Jug 1")
print("8. Transfer from Jug 2 to Jug 1 and empty Jug 2")

while True:
	print(C)
	if C[0]==k or C[1]==k:
		print("Reached goal state.")
		break
	
	a = int(input())
	if a==1:
		C[0] = Jugs[0]
	elif a==2:
		C[1] = Jugs[1]
	elif a==3:
		C[0] = 0
	elif a==4:
		C[1] = 0
	elif a==5:
		C[1] += C[0]
		C[0] = max(0, C[1]-Jugs[1])
		C[1] = min(Jugs[1], C[1])
	elif a==6:
		C[0] += C[1]
		C[1] = max(0, C[0]-Jugs[0])
		C[0] = min(Jugs[0], C[0])
	elif a==7:
		C[1] += C[0]
		C[0] = 0
		C[1] = min(Jugs[1], C[1])
	elif a==8:
		C[0] += C[1]
		C[1] = 0
		C[0] = min(Jugs[0], C[0])
	else:
		pass
