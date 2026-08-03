from backend.app.chess.board import Board
from backend.app.chess.pieces import Color, PieceType


def test_initial_board_has_white_king_on_e1():
    board = Board()

    piece = board.squares["e1"]

    assert piece.color == Color.WHITE
    assert piece.type == PieceType.KING


def test_initial_board_has_black_king_on_e8():
    board = Board()

    piece = board.squares["e8"]

    assert piece.color == Color.BLACK
    assert piece.type == PieceType.KING


def test_initial_board_has_white_pawns():
    board = Board()

    for file in "abcdefgh":
        piece = board.squares[f"{file}2"]

        assert piece.color == Color.WHITE
        assert piece.type == PieceType.PAWN


def test_initial_board_has_black_pawns():
    board = Board()

    for file in "abcdefgh":
        piece = board.squares[f"{file}7"]

        assert piece.color == Color.BLACK
        assert piece.type == PieceType.PAWN


def test_initial_board_has_empty_square():
    board = Board()

    assert board.squares.get("e4") is None