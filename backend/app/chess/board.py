from backend.app.chess.pieces import Color, Piece, PieceType


class Board:
    def __init__(self):
        self.squares = {}
        self._setup_initial_position()

    def _setup_initial_position(self):
        # White pieces
        self.squares["a1"] = Piece(Color.WHITE, PieceType.ROOK)
        self.squares["b1"] = Piece(Color.WHITE, PieceType.KNIGHT)
        self.squares["c1"] = Piece(Color.WHITE, PieceType.BISHOP)
        self.squares["d1"] = Piece(Color.WHITE, PieceType.QUEEN)
        self.squares["e1"] = Piece(Color.WHITE, PieceType.KING)
        self.squares["f1"] = Piece(Color.WHITE, PieceType.BISHOP)
        self.squares["g1"] = Piece(Color.WHITE, PieceType.KNIGHT)
        self.squares["h1"] = Piece(Color.WHITE, PieceType.ROOK)

        for file in "abcdefgh":
            self.squares[f"{file}2"] = Piece(Color.WHITE, PieceType.PAWN)

        # Black pieces
        self.squares["a8"] = Piece(Color.BLACK, PieceType.ROOK)
        self.squares["b8"] = Piece(Color.BLACK, PieceType.KNIGHT)
        self.squares["c8"] = Piece(Color.BLACK, PieceType.BISHOP)
        self.squares["d8"] = Piece(Color.BLACK, PieceType.QUEEN)
        self.squares["e8"] = Piece(Color.BLACK, PieceType.KING)
        self.squares["f8"] = Piece(Color.BLACK, PieceType.BISHOP)
        self.squares["g8"] = Piece(Color.BLACK, PieceType.KNIGHT)
        self.squares["h8"] = Piece(Color.BLACK, PieceType.ROOK)

        for file in "abcdefgh":
            self.squares[f"{file}7"] = Piece(Color.BLACK, PieceType.PAWN)
