import random, math

dim = int(input("Enter the side length of the square: "))
num_of_arrows = int(input("Enter the number of arrows: "))

grid = [[0 for col in range(dim)] for row in range(dim)]

def check(place, direction, hits = 0, turned = False):

    p = place - 1
    
    row = math.floor(p/dim) 
    col = p-row*dim

    #print(row, col, direction, hits)

    if row == 0 and direction == 1 and (grid[row][col] == 0 or turned == True):
        return [col + 1, hits]
    if col == dim - 1 and direction == 2 and (grid[row][col] == 0 or turned == True):
        return [dim + row + 1, hits]
    if row == dim - 1 and direction == 3 and (grid[row][col] == 0 or turned == True):
        return [dim*3 - col, hits]
    if col == 0 and direction == 4 and (grid[row][col] == 0 or turned == True):
        return [dim*4 - row, hits]

    if (grid[row][col] == 0 or turned == True) and direction == 1:
        return check(place - dim, 1, hits)
    elif (grid[row][col] == 0 or turned == True) and direction == 2:
        return check(place + 1, 2, hits)
    elif (grid[row][col] == 0 or turned == True) and direction == 3:
        return check(place + dim, 3, hits)
    elif (grid[row][col] == 0 or turned == True) and direction == 4:
        return check(place - 1, 4, hits)
    else:
        d = grid[row][col]
        if hits + 1 <= num_of_arrows:
            return check(place, d, hits + 1, True)


def check_all():
    
    for i in range(dim):
        if check(i + 1, 3) == None:
            return False

    for i in range(dim):
        if check(dim + dim*i, 4) == None:
            return False

    for i in range(dim):
        if check(dim*dim - i, 1) == None:
            return False

    for i in range(dim):
        if check(dim*dim - (dim - 1) - dim*i, 2) == None:
            return False
        
    return True


def print_all():
    
    for i in range(dim):
        print ("In: ", i + 1,
               "   Out: ", check(i + 1, 3)[0],
               "   Hits: ", check(i + 1, 3)[1])

    for i in range(dim):
        print ("In: ", dim + i + 1,
               "   Out: ", check(dim + dim*i, 4)[0],
               "   Hits: ", check(dim + dim*i, 4)[1])
        
    for i in range(dim):
        print ("In: ", dim*2 + i + 1,
               "   Out: ", check(dim*dim - i, 1)[0],
               "   Hits: ", check(dim*dim - i, 1)[1])
        
    for i in range(dim):
        print ("In: ",dim*3 + i + 1,
               "   Out: ", check(dim*dim - (dim - 1) - dim*i, 2)[0],
               "   Hits: ", check(dim*dim - (dim - 1) - dim*i, 2)[1])

        
def new_arrow():

    place = random.randint(0, dim*dim - 1)
    prow = math.floor(place/dim)

    direc = random.randint(1,4)

    if grid[prow][place-prow*dim] == 0:
        grid[prow][place-prow*dim] = direc
    else:
        new_arrow()

while True: 

    for i in range(num_of_arrows):
        new_arrow()
    if check_all() == True:
        break

    grid = [[0 for col in range(dim)] for row in range(dim)]

for row in grid:
    print(row)

print_all()
        
