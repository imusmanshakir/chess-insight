from backend.app.chess.pieces import Color, Piece, PieceType


def test_white_knight():
    knight = Piece(Color.WHITE, PieceType.KNIGHT)

    assert knight.color == Color.WHITE
    assert knight.type == PieceType.KNIGHT
