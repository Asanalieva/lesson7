plane = [
    ['*','*','*'], #0
    ['*','*','*'], #1
    ['*','*','*']  #2

]

def print_plane(plane):
    for i in plane:
        print(f"{i[0]} | {i[1]} | {i[2]}")



def main():
    print_plane(plane)
    for i in range(9):
        if i % 2 == 0:
            player = "X"
        else:
            player = "0"

        if plane[0][0] == plane[0][1] == plane[0][2] == 'X':
            print('X won')
            exit()
        elif plane[1][0] == plane[1][1] == plane[1][2] == 'X':
            print('X won')
            exit()
        elif plane[2][0] == plane[2][1] == plane[2][2] == 'X':
            print('X won')
            exit()
        elif plane[0][0] == plane[1][1] == plane[2][2] == 'X':
            print('X won')
            exit()
        elif plane[0][2] == plane[1][1] == plane[2][0] == 'X':
            print('X won')
            exit()
        elif plane[0][0] == plane[1][0] == plane[2][0] == 'X':
            print('X won')
            exit()
        elif plane[0][1] == plane[1][1] == plane[2][1] == 'X':
            print('X won')
            exit()
        elif plane[0][2] == plane[1][2] == plane[2][2] == 'X':
            print('X won')
            exit()
        elif plane[0][0] == plane[0][1] == plane[0][2] == '0':
            print('0 won')
            exit()
        elif plane[1][0] == plane[1][1] == plane[1][2] == '0':
            print('0 won')
            exit()
        elif plane[2][0] == plane[2][1] == plane[2][2] == '0':
            print('0 won')
            exit()
        elif plane[0][0] == plane[1][1] == plane[2][2] == '0':
            print('0 won')
            exit()
        elif plane[0][2] == plane[1][1] == plane[2][0] == '0':
            print('0 won')
            exit()
        elif plane[0][0] == plane[1][0] == plane[2][0] == '0':
            print('0 won')
            exit()
        elif plane[0][1] == plane[1][1] == plane[2][1] == '0':
            print('0 won')
            exit()
        elif plane[0][2] == plane[1][2] == plane[2][2] == '0':
            print('0 won')
            exit()

        player_x = int(input())
        player_y = int(input())
        plane[player_x][player_y] = player
        print_plane(plane)
main()
#Standup
#Что сделала:
# Д\З № 7
# План:Нет
# Проблемы:Не смогла сделать ничью
