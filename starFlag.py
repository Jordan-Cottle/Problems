
def checkSolution(a, b, n, iterative=True):
    if (a < b):
        print("Put the larger number first")
        return False

    if (abs(a - b) > 1):
        print("A and B cannot differ by more than 1")
        return False

    if(not iterative):
        sum = a + b

        rem = n % sum

        return rem == 0 or rem == a
    
    evenRow = True

    total = 0

    while(total < n):
        if(evenRow):
            total += a
        else:
            total += b
        
        evenRow = not evenRow
    
    return total == n


def generateSolutions(n):
    solutions = []
    for i in range(3, n+1):
        rem = n % i

        if rem == 0 or rem == (i+1)//2:
            solutions.append(((i+1)//2, i//2))
    
    return solutions

stars = int(input())

print(f'{stars}:')
solutions = generateSolutions(stars)

for solution in solutions:
    a = solution[0]
    b = solution[1]

    # use both methods of checking solution
    solA = checkSolution(a, b, stars, False)
    solB = checkSolution(a, b, stars, True)

    #output solution
    if solA and solB:
        print(a, b, sep=',')
    else: # if solution checks don't agree, notify
        print(f'A: {solA}, B: {solB}')