# Returns a tuple (changed, new_board)
# where:
#  changed - a boolean indicating if
#            the board has changed.
#  new_board - the board after the user
#              presses the 'Up' key.
def doKeyUp(board):
    changed = False
    new_board = [[] for x in range(len(board))]
    counter = 0
    temp = []
    lst = []
    count = 0

    while counter < len(board[0]):
        for i in range(len(board)):
            lst.append(board[i][counter])
            if len(lst) == len(board):
                temp = lst

                n = len(temp)
                for n, x in enumerate(temp):
                    if x == " ":
                        temp[n] = 0
                        count = count + 1
                temp[:] = filter(None, temp)
                temp.extend([" "] * (count))
                count = 0

                for i in range(len(temp)-1):
                    if temp[i] == " ":
                        continue
                    if temp[i] == temp[i+1]:
                        temp[i] = int(temp[i]) + int(temp[i+1])
                        temp[i] = str(temp[i])
                        temp[i+1] = " "

                n = len(temp)
                for n, x in enumerate(temp):
                    if x == " ":
                        temp[n] = 0
                        count = count + 1
                temp[:] = filter(None, temp)
                temp.extend([" "] * (count))
                count = 0

                for i in range(len(new_board)):
                    new_board[i].append(temp[i])

                lst = []
        counter = counter + 1

    if board != new_board:
        changed = True
    return changed, new_board

# Returns a tuple (changed, new_board)
# where:
#  changed - a boolean indicating if
#            the board has changed.
#  new_board - the board after the user
#              presses the 'Down' key.
def doKeyDown(board):
    changed = False
    new_board = [[] for x in range(len(board))]
    counter = 0
    temp = []
    lst = []
    count = 0

    while counter < len(board[0]):
        for i in range(len(board)):
            lst.append(board[i][counter])
            if len(lst) == len(board):
                temp = lst

                n = len(temp)
                for n, x in enumerate(temp):
                    if x == " ":
                        temp[n] = 0
                        count = count + 1
                temp[:] = filter(None, temp)
                empty = [" "] * count
                temp = empty + temp
                count = 0
                print("before ", temp)
                for i in reversed(range(len(temp)-1)):
                    if temp[i] == " ":
                        continue
                    if temp[i] == temp[i+1]:
                        temp[i+1] = int(temp[i]) + int(temp[i+1])
                        temp[i+1] = str(temp[i+1])
                        temp[i] = " "

                        print(temp)
                n = len(temp)
                for n, x in enumerate(temp):
                    if x == " ":
                        temp[n] = 0
                        count = count + 1
                temp[:] = filter(None, temp)
                empty = [" "] * count
                temp = empty + temp
                count = 0

                for i in range(len(new_board)):
                    new_board[i].append(temp[i])

                lst = []
        counter = counter + 1

    if board != new_board:
        changed = True
    return changed, new_board

# Returns a tuple (changed, new_board)
# where:
#  changed - a boolean indicating if
#            the board has changed.
#  new_board - the board after the user
#              presses the 'Left' key.
def doKeyLeft(board):
    changed = False
    new_board = [list(x) for x in board]
    for i in range(len(board)):
        temp = board[i]
        count = 0
        n = len(temp)
        for n, x in enumerate(temp):
            if x == " ":
                temp[n] = 0
                count = count + 1
        temp[:] = filter(None, temp)
        temp.extend([" "] * (count))

    for i in range(len(board)):
        temp = board[i]
        for i in range(len(temp)-1):
            if temp[i] == " ":
                continue
            if temp[i] == temp[i+1]:
                temp[i] = int(temp[i]) + int(temp[i+1])
                temp[i] = str(temp[i])
                temp[i+1] = " "

    for i in range(len(board)):
        temp = board[i]
        n = len(temp)
        count = 0
        for n, x in enumerate(temp):
            if x == " ":
                temp[n] = 0
                count = count + 1
        temp[:] = filter(None, temp)
        temp.extend([" "] * (count))

    if board != new_board:
        new_board = board
        changed = True
    return changed, new_board

# Returns a tuple (changed, new_board)
# where:
#  changed - a boolean indicating if
#            the board has changed.
#  new_board - the board after the user
#              presses the 'Right' key.
def doKeyRight(board):
    changed = False
    new_board = [list(x) for x in board]
    for i in range(len(board)):
        temp = board[i]
        count = 0
        n = len(temp)
        for n, x in enumerate(temp):
            if x == " ":
                temp[n] = 0
                count = count + 1
        temp[:] = filter(None, temp)
        empty = [" "] * count
        temp = empty + temp
        board[i] = temp

    for i in range(len(board)):
        temp = board[i]
        for i in reversed(range(len(temp)-1)):
            if temp[i] == " ":
                continue
            if temp[i] == temp[i+1]:
                temp[i+1] = int(temp[i]) + int(temp[i+1])
                temp[i+1] = str(temp[i+1])
                temp[i] = " "

    for i in range(len(board)):
        temp = board[i]
        n = len(temp)
        count = 0
        for n, x in enumerate(temp):
            if x == " ":
                temp[n] = 0
                count = count + 1
        temp[:] = filter(None, temp)
        empty = [" "] * count
        temp = empty + temp
        board[i] = temp

    if board != new_board:
        new_board = board
        changed = True
    return changed, new_board

# Checks whether a given board has any
# possible move left. If no more moves,
# return True. Otherwise return False.
def isGameOver(board):
    Full = True
    Void = True
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == " ":
                Full= False

    for i in range(len(board)):
        for j in range(len(board[i])-1):
            if board[i][j] == board[i][j+1] or board[i][j] == board[i][j-1]:
                Void = False
            break

    if Full == True and Void == True:
        return True
    else:
        return False

# Returns a list of tuples (row, col)
# indicating where the empty spots are
def emptyPos(board):
    output = []
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == " ":
                output.append((i,j))
    return output

# Returns a dictionary mapping each tile
# value on the board to its count (i.e.,
# how many times it appears on the board)
def hist(board):
    dictionary = {}

    for i in range(len(board)):
        for j in range(len(board)+1):
            if board[i][j] == " ":
                continue
            if int(board[i][j]) in dictionary:
                dictionary[int(board[i][j])] = dictionary[int(board[i][j])] + 1
            else:
                dictionary[int(board[i][j])] = 1
    return dictionary
