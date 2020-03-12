# Recursive Python function to solve tower of hanoi

def TowerOfHanoi(n , from_rod, to_rod, aux_rod):
    global moves
    moves += 1
    if n == 1:
        print("Move disk 1 from rod",from_rod,"to rod",to_rod)
        return
    TowerOfHanoi(n-1, from_rod, aux_rod, to_rod)
    print("Move disk",n,"from rod",from_rod,"to rod",to_rod)
    TowerOfHanoi(n-1, aux_rod, to_rod, from_rod)

def DrawTowers(a, b, c):
    #init all on A rod
    print(a, b, c)


# Driver code
n = 3
moves = 0
#draw first towers
DrawTowers(n, 0, 0)
TowerOfHanoi(n, 'A', 'C', 'B')
# A, C, B are the name of rods
print("Number of moves: "+ str(moves))
# Contributed By Harshit Agrawal
#
#
