# Task 6: More on Classes
class TictactoeException(Exception):
    def __init__(self, message):
        self.message = message 
        super().__init__(message)

class Board:
    valid_moves=["upper left", "upper center", "upper right", "middle left", "center", "middle right", "lower left", "lower center", "lower right"]
    def __init__(self):
        self.board_array = [[" " for _ in range(3)] for _ in range(3)]
        self.turn = "X"
        self.last_move = None
    def __str__(self):
        rows = []
        for r in self.board_array:
            rows.append(" | ".join(r))
        return "\n------\n".join(rows)
    def move(self, move_string):
        if move_string not in Board.valid_moves:
            raise TictactoeException("That's not a valid move.")
        row_map = {
            "upper": 0,
            "middle": 1,
            "lower": 2
        }
        col_map = {
            "left": 0,
            "center": 1,
            "right": 2
        }
        row_str, col_str = move_string.split()
        row = row_map[row_str]
        col = col_map[col_str]
        if self.board_array[row][col] != " ":
            raise TictactoeException("That spot is taken.")
        self.board_array[row][col] = self.turn 
        self.last_move = (row, col)
        self.turn = "0" if self.turn == "X" else "X"

    def whats_next(self):
        lines = []
        for i in range(3):
            lines.append(self.board_array[i])
            lines.append([self.board_array[0][i], self.board_array[1][i], self.board_array[2][i]])

        lines.append([self.board_array[0][0], self.board_array[1][1], self.board_array[2][2]])
        lines.append([self.board_array[0][2], self.board_array[1][1], self.board_array[2][0]])

        for line in lines:
            if line == ["X", "X", "X"]:
                return (True, "X has won")
            elif line == ["0", "0", "0"]:
                return (True, "0 has won")
            
        if all(cell != " " for row in self.board_array for cell in row):
            return (True, "Cat's Game")
        return (False, f"{self.turn}'s turn")

def main():
    board = Board()
    print("Welcome")
    print(board)

    while True:
        _, message = board.whats_next()
        if "turn" in message:
            print(f"\n{message}")
        else:
            print(f"\nGame over: {message}")
            break 

        move_input = input("Enter your move: ").strip().lower()
        try:
            board.move(move_input)
        except TictactoeException as e:
            print(f"Error: {e.message}")
            continue 
        print("\n" + str(board))

if __name__ == "__main__":
    main()


