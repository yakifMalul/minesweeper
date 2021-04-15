# Setup
import random
from colorama import Fore, Back, Style

# easy 8 - 10: 10
# medium 14 - 18: 40
# hard 19 - 24: 99
X = 10
Y = 10
NUM_OF_BOMBS = 10
VALUES = False
GAME = True
status = ""
board = []
num_board = []
ravid = []

level = input("Easy, Medium or Hard? ")
if level == "easy":
    X = 10
    Y = 8
    NUM_OF_BOMBS = 10
elif level == "medium":
    X = 18
    Y = 14
    NUM_OF_BOMBS = 40
elif level == "hard":
    X = 24
    Y = 19
    NUM_OF_BOMBS = 99
elif level == "yakiller":
    X = 20
    Y = 15
    NUM_OF_BOMBS = 10
else:
    X = 10
    Y = 10
    NUM_OF_BOMBS = 10


for i in range(Y + 2):
    board.append([])
    for j in range(X + 2):
        board[i].append(VALUES)

# Define num_board
for i in range(Y + 2):
    num_board.append([])
    for j in range(X + 2):
        if j == 0 or j == X + 1 or i == 0 or i == Y + 1:
            num_board[i].append('#')
        else:
            num_board[i].append(0)

# Define ravid
for i in range(Y + 2):
    ravid.append([])
    for j in range(X + 2):
        if j == 0 or j == X + 1 or i == 0 or i == Y + 1:
            ravid[i].append('#')
        else:
            ravid[i].append('∎')


# Fill the bord
def mine():
    x = random.randrange(1, X + 1)
    y = random.randrange(1, Y + 1)

    while board[y][x]:
        x = random.randrange(1, X + 1)
        y = random.randrange(1, Y + 1)
    board[y][x] = "  *  "


def find_mines(x, y):
    count = 0
    for num1 in range(x-1, x+2):
        for num2 in range(y-1, y+2):
            if num1 == x and num2 == y:
                pass
            elif board[num2][num1] == "  *  ":
                count += 1
    return count


for i in range(NUM_OF_BOMBS):
    mine()

for i in range(1, X + 1):
    for j in range(1, Y + 1):
        if board[j][i] == "  *  ":
            num_board[j][i] = "*"
        else:
            num_board[j][i] = find_mines(i, j)


def print_ravid():
    for num1 in range(Y + 2):
        for num2 in range(X + 2):
            if (num1 == 0 or num1 == Y + 1) and (num2 == 0 or num2 == X + 1):
                print("#", end="\t")
            elif num1 == 0 or num1 == Y + 1:
                print(Fore.CYAN + str(num2) + Style.RESET_ALL, end="\t")
            elif num2 == 0 or num2 == X + 1:
                print(Fore.CYAN + str(num1) + Style.RESET_ALL, end="\t")
            else:
                item = ravid[num1][num2]
                if item == 0:
                    print("", end="\t")
                elif item == "∎":
                    print(Fore.GREEN + str(item) + Style.RESET_ALL, end="\t")
                elif item == "╒":
                    print(Fore.RED + str(item) + Style.RESET_ALL,  end="\t")
                else:
                    print(Fore.LIGHTMAGENTA_EX + str(item) + Style.RESET_ALL, end="\t")
        print()


def flag(y, x):
    item = ravid[x][y]
    if item == 0:
        pass
    elif item == '╒':
        ravid[x][y] = '∎'
    else:
        ravid[x][y] = '╒'


def show(y, x):
    sign = num_board[x][y]
    if ravid[x][y] == '╒':
        pass
    elif sign == "*":
        global GAME
        GAME = False
    elif sign == 0:
        board[x][y] = "check"
        find_neighbor(x, y)
    else:
        ravid[x][y] = num_board[x][y]


def find_neighbor(y, x):
    for num1 in range(x - 1, x + 2):
        for num2 in range(y-1, y+2):
            ravid[num2][num1] = num_board[num2][num1]
            if num_board[num2][num1] == 0 and board[num2][num1] != "check":
                show(num1, num2)


def end_game():
    global status
    global GAME
    count = 0
    squares = []
    for num2 in range(X + 2):
        for num1 in range(Y + 2):
            if ravid[num1][num2] == '∎' or ravid[num1][num2] == '╒':
                count += 1
                squares.append([num1, num2])
    if count == NUM_OF_BOMBS:
        for square in squares:
            if num_board[square[0]][square[1]] == "*":
                status = "victory"
                GAME = False


while GAME:
    print_ravid()
    action = input("Enter an action (S- for Show, F- for Flag. A X Y): ")
    action_list = action.split(' ')
    if action_list[0] == 'S' or action_list[0] == 's':
        show(int(action_list[1]), int(action_list[2]))
    elif action_list[0] == 'F' or action_list[0] == 'f':
        flag(int(action_list[1]), int(action_list[2]))
    end_game()

if not GAME:
    for num1 in range(Y + 2):
        for num2 in range(X + 2):
            if (num1 == 0 or num1 == Y + 1) and (num2 == 0 or num2 == X + 1):
                print("#", end="\t")
            elif num1 == 0 or num1 == Y + 1:
                print(Fore.CYAN + str(num2) + Style.RESET_ALL, end="\t")
            elif num2 == 0 or num2 == X + 1:
                print(Fore.CYAN + str(num1) + Style.RESET_ALL, end="\t")
            else:
                item1 = ravid[num1][num2]
                item2 = num_board[num1][num2]
                if item2 == "*":
                    if item1 == 0:
                        print("", end="\t")
                    elif item1 == "∎":
                        print(Fore.BLUE + str(item1) + Style.RESET_ALL, end="\t")
                    elif item1 == "╒":
                        print(Fore.LIGHTBLUE_EX + "F" + Style.RESET_ALL, end="\t")
                    else:
                        print(Fore.LIGHTMAGENTA_EX + str(item1) + Style.RESET_ALL, end="\t")
                else:
                    if item1 == 0:
                        print("", end="\t")
                    elif item1 == "∎":
                        print(Fore.GREEN + str(item1) + Style.RESET_ALL, end="\t")
                    elif item1 == "╒":
                        print(Fore.RED + "F" + Style.RESET_ALL, end="\t")
                    else:
                        print(Fore.LIGHTMAGENTA_EX + str(item1) + Style.RESET_ALL, end="\t")

        print()
    if status == "victory":
        print("Congratulation!")
    else:
        print("GAME OVER!")
