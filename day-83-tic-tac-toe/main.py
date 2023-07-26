def print_gameplay():
    gameplay_print = [" " if i in range(9) else i for i in gameplay]
    to_print = f"""\
                 a   b   c
               ------------
            1 ┆  {gameplay_print[0]} │ {gameplay_print[1]} │ {gameplay_print[2]}
              ┆ ───┼───┼───
            2 ┆  {gameplay_print[3]} │ {gameplay_print[4]} │ {gameplay_print[5]}
              ┆ ───┼───┼───
            3 ┆  {gameplay_print[6]} │ {gameplay_print[7]} │ {gameplay_print[8]}
        """

    print(to_print)


def if_win():
    is_win = (gameplay[0] == gameplay[1] == gameplay[2]) or \
             (gameplay[3] == gameplay[4] == gameplay[5]) or \
             (gameplay[6] == gameplay[7] == gameplay[8]) or \
             (gameplay[0] == gameplay[3] == gameplay[6]) or \
             (gameplay[1] == gameplay[4] == gameplay[7]) or \
             (gameplay[2] == gameplay[5] == gameplay[8]) or \
             (gameplay[0] == gameplay[4] == gameplay[8]) or \
             (gameplay[2] == gameplay[4] == gameplay[6])
    return is_win


gameplay = [i for i in range(9)]
player_turn = 0

players = ["Player 1", "Player 2"]
player_marks = ["X", "O"]

gameplay_dict = {
    "a1": 0,
    "b1": 1,
    "c1": 2,
    "a2": 3,
    "b2": 4,
    "c2": 5,
    "a3": 6,
    "b3": 7,
    "c3": 8,
}
#TODO: Validator for a legitimate move (a move that hasn't been played before)
def is_good_move(player_move):
    return gameplay[gameplay_dict[player_move]] not in player_marks

#TODO: Initial prints
print("Welcome to the tic-tac-toe game!")
print("You can play in turns by selecting the cell (e.g. 'a1')")
print("Type 'e' to exit")
print_gameplay()

turn_counter = 0
game_on = True

while turn_counter < 9:
    player_move = input(f"{players[player_turn]}, please enter your move: ").lower()
    if player_move == 'e':
        print('Thank you for playing and goodbye!')
        break
    else:
        try:
            if is_good_move(player_move):
                gameplay[gameplay_dict[player_move]] = player_marks[player_turn]
                print_gameplay()
                if if_win():
                    print(f"{players[player_turn]} won!")
                    break
                else:
                    player_turn = 1 - player_turn
                    turn_counter += 1

            else:
                print("This move has already been played. Try another move")
        except KeyError:
            print("Incorrect command. Try again")

if turn_counter == 8:
    print("It's a draw!")


