# Recursive Python function to solve tower of hanoi

def TowerOfHanoi(n , from_rod, to_rod, aux_rod):
    global a, b, c
    global moves
    moves += 1
    if n == 1:
        print("Move disk 1 from rod",from_rod,"to rod",to_rod)
        if from_rod == 'A' and to_rod == 'B':
            a -= 1
            b += 1
            DrawTowers(a, b, c)
        elif from_rod == 'A' and to_rod == 'C':
            a -= 1
            c += 1
            DrawTowers(a, b, c)
        elif from_rod == 'B' and to_rod == 'A':
            a += 1
            b -= 1
            DrawTowers(a, b, c)
        elif from_rod == 'B' and to_rod == 'C':
            c += 1
            b -= 1
            DrawTowers(a, b, c)
        elif from_rod == 'C' and to_rod == 'A':
            a += 1
            c -= 1
            DrawTowers(a, b, c)
        elif from_rod == 'C' and to_rod == 'B':
            b += 1
            c -= 1
            DrawTowers(a, b, c)
        return
    TowerOfHanoi(n-1, from_rod, aux_rod, to_rod)
    print("Move disk",n,"from rod",from_rod,"to rod",to_rod)
    if from_rod == 'A' and to_rod == 'B':
        a -= 1
        b += 1
        DrawTowers(a, b, c)
    elif from_rod == 'A' and to_rod == 'C':
        a -= 1
        c += 1
        DrawTowers(a, b, c)
    elif from_rod == 'B' and to_rod == 'A':
        a += 1
        b -= 1
        DrawTowers(a, b, c)
    elif from_rod == 'B' and to_rod == 'C':
        c += 1
        b -= 1
        DrawTowers(a, b, c)
    elif from_rod == 'C' and to_rod == 'A':
        a += 1
        c -= 1
        DrawTowers(a, b, c)
    elif from_rod == 'C' and to_rod == 'B':
        b += 1
        c -= 1
        DrawTowers(a, b, c)
    TowerOfHanoi(n-1, aux_rod, to_rod, from_rod)

def DrawTowers(a, b, c):
    #init all on A rod
    print(a, b, c)


# Driver code
n = 5
moves = 0
#draw first towers
a = n
b = 0
c = 0
DrawTowers(a, b, c)
TowerOfHanoi(n, 'A', 'C', 'B')
# A, C, B are the name of rods
print("Number of moves: "+ str(moves))
# Contributed By Harshit Agrawal
#
#
