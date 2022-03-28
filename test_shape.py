import Shape

def test_perirectangle():
    x = 10
    y = 10
    result = Shape.perirectangle(x,y)
    assert x+x+y+y == result

def test_arearectangle():
    x = 10
    y = 10
    result = Shape.areaofrectangle(x,y)
    assert x*y == result

def test_areasquare():
    x = 10
    result = Shape.areaofsquare(x)
    assert x**2 == result
