class ConnectFour:
    def __init__(self):
        self.row = 6
        self.column = 7
        self.board = [[" " for _ in range(self.column)]
                      for _ in range(self.row)]
        self.count = 0
        self.moves = [[-1, -1]]

    def display_board(self):
        # Print the slots of the game board
        board = ''
        for r in range(self.row):
            board += '|'
            for c in range(self.column):
                board += f"{self.board[r][c]}|"
            board += "\n"
            board += "-" * 15 + "\n"
        return board

    def players(self):
        players = ['X', 'O']
        return players[self.count % 2]

    def add_piece(self, column):
        if column > 6 or column < 0:
            raise ValueError("Out of board")
        if self.is_game_over() is True:
            raise ValueError("Game Over")
        if self.board[0][column] != " ":
            raise ValueError("The column is full")
        for r in range(self.row - 1, -1, -1):
            if self.board[r][column] == ' ':
                self.board[r][column] = self.players()
                self.count += 1
                self.moves.append([r, column])
                break
            if r == 0 and self.board[r][column] != ' ':
                raise ValueError
        return

    def is_game_over(self):
        if len(self.moves) == 42:
            return True

        # check for horizontal wins
        for c in range(0, 4):
            for r in range(0, 6):
                if self.board[r][c] == self.board[r][c + 1] == \
                        self.board[r][c + 2] == \
                        self.board[r][c + 3] and self.board[r][c] != ' ':
                    return True

        # check for vertical win for X
        for r in range(0, 3):
            for c in range(0, 7):
                if self.board[r][c] == self.board[r + 1][c] == \
                        self.board[r + 2][c] == \
                        self.board[r + 3][c] and self.board[r][c] != ' ':
                    return True

        # check for diagonal wins for X
        for c in range(0, 4):
            for r in range(0, 3):
                if self.board[r][c] == self.board[r + 1][c + 1] == \
                        self.board[r + 2][c + 2] == \
                        self.board[r + 3][c + 3] and self.board[r][c] != ' ':
                    return True

        for c in range(3, 7):
            for r in range(0, 3):
                if self.board[r][c] == self.board[r + 1][c - 1] == \
                        self.board[r + 2][c - 2] == \
                        self.board[r + 3][c - 3] and self.board[r][c] != ' ':
                    return True
        return False

    def get_winner(self):
        if self.is_game_over() is True:
            last_row, last_col = self.moves[-1][0], self.moves[-1][1]
            winner = self.board[last_row][last_col]
            return winner
        else:
            return None

    def undo(self):
        if len(self.moves) <= 1:
            raise ValueError('Cannot undo')
        last_move = self.moves.pop()
        self.board[last_move[0]][last_move[1]] = ' '
        self.count -= 1
        return True

    def __str__(self):
        return self.display_board()