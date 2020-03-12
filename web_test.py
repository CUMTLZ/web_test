from webHomework import  test
class TestClass:
    def test_one(self):
        black = "2H 3D 5S 9C KD"
        white = "2C 3H 4S 8C AH"
        assert test(black,white) == "white win"
    def test_two(self):
        black = "2H 4S 4C 2D 4H"
        white = "2S 8S AS QS 3S"
        assert test(black, white) == "black win"
    def test_three(self):
        black = "2H 3D 5S 9C KD"
        white = "2C 3H 4S 8C KH"
        assert test(black, white) == "black win"
    def test_four(self):
        black = "TD TS JD QD KD"
        white = "2D 3S 2H 2C 3H"
        assert test(black, white) == "white win"
    def test_five(self):
        black = "TD 6H 7H 8C 9C"
        white = "2D 3C 4H 5C 6C"
        assert test(black, white) == "white win"
    def test_six(self):
        black = "TD TD JQ 2D 3C"
        white = "2C 3C 5D 5H 6H"
        assert test(black, white) == "black win"
    def test_seven(self):
        black = "2C 3C 5D 5H 6H"
        white = "2C 3C 5D 5H 6H"
        assert test(black,white) == "Tie"

