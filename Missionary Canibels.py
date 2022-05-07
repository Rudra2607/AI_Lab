class MissionaryCanibels():
    def __init__(self, canibels_left, missionary_left, boat, canibels_right, missionary_right):
        self.canibels_left = canibels_left
        self.missionary_left = missionary_left
        self.boat = boat
        self.canibels_right = canibels_right
        self.missionary_right = missionary_right
        self.parent = None
    
    def isGoal(self):
        return self.canibels_left==0 and self.missionary_left==0
    
    def isValid(self):
        if self.canibels_left<0 or self.missionary_left<0 or self.canibels_right<0 or self.missionary_right<0:
            return False
        if self.missionary_left<self.canibels_left and self.missionary_left!=0:
            return False
        if self.missionary_right<self.canibels_right and self.missionary_right!=0:
            return False
        return True


def generateChild(S):
    Children = []
    if S.boat=='Left':
        for Case in [[2,0],[0,2],[1,1],[1,0],[0,1]]:
            Child = MissionaryCanibels(S.canibels_left-Case[0], S.missionary_left-Case[1], 'Right', S.canibels_right+Case[0], S.missionary_right+Case[1])
            Child.parent = S
            if Child.isValid():
                Children.append(Child)
    else:
        for Case in [[1,0],[0,1],[1,1],[2,0],[0,2]]:
            Child = MissionaryCanibels(S.canibels_left+Case[0], S.missionary_left+Case[1], 'Left', S.canibels_right-Case[0], S.missionary_right-Case[1])
            Child.parent = S
            if Child.isValid():
                Children.append(Child)
    return Children

IS = MissionaryCanibels(3, 3, 'Left', 0, 0)
Queue = list()
Processed = list()

Queue.append(IS)

while len(Queue)!=0:
    CS = Queue[0]
    Queue.remove(CS)
    
    if CS.isGoal():
        Solution = []
        Solution.append(CS)
        while CS.parent!=None:
            CS = CS.parent
            Solution.append(CS)
        for i in Solution[::-1]:
            print(i.canibels_left, i.missionary_left, i.boat, i.canibels_right, i.missionary_right)
        print()
        # break
    elif CS in Processed:
        pass
    else:
        Processed.append(CS)
        Children = generateChild(CS)
        for Child in Children:
            if Child not in Queue and Child not in Processed:
                Queue.append(Child)

print('Done')