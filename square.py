class Square:

    def __init__(self, row, col, piece = 0):
        self.row = row
        self.col = col
        self.piece = piece

    def has_piece(self):
        return self.piece != 0

    def isEmpty(self):
        return not self.has_piece()

    def has_team_piece(self, color):
        return self.has_piece() and self.piece.color == color

    def has_rival_piece(self, color):
        return self.has_piece() and self.piece.color != color

    def isEmpty_or_rival(self, color):
        return self.isEmpty() or self.has_rival_piece(color)


    @staticmethod
    def in_range(*args):
        for arg in args:
            if arg<0 or arg>7:
                return False
        return True


        
