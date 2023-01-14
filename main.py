import board_setup
import game_play
import print_board


def main():
    # board_size = int(input('Enter size of board: '))
    board_size = 10
    moves = 0
    board = board_setup.create_board(board_size)
    while True:
        print_board.create_image(board)
        moves += 1
        game_play.player(board, board_size)
        if board_setup.check_finish(board):
            break
    print_board.create_image(board)
    print(f'You completed the game in {moves} moves!')


if __name__ == '__main__':
    main()