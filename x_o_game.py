plane = [
    ['*','*','*'], #0
    ['*','*','*'], #1
    ['*','*','*']  #2

]

win_templates = [
    [(0,0),(1,1),(2,2)],
    [(0,0),(0,1),(0,2)],
    [(1,0),(1,1),(1,2)],
    [(2,0),(2,1),(2,2)],
    [(0,2),(1,1),(2,0)],
    [(0,0),(1,0),(2,0)],
    [(0,1),(1,1),(2,1)],
    [(0,2),(1,2),(2,2)]
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

        player_x = int(input())
        player_y = int(input())
        plane[player_x][player_y] = player
        print_plane(plane)

        for templ in win_templates:
            first = templ[0]
            second = templ[1]
            third = templ[2]
            if plane[first[0]][first[1]] == plane[second[0]][second[1]] == plane[third[0]][third[1]] != "*":
                print(f'{player} won')
                exit()
        if i == 8:
            print("draw")

main()

