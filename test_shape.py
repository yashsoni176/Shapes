import Shape

def test_perirectangle():
    x = 10
    y = 10
    r = Shape.perirectangle(x,y)
    assert x+x+y+y == r

def test_areaofrectangle():
    x = 10
    y = 10
    r = Shape.areaofrectangle(x,y)
    assert x*y == r

def test_areaofsquare():
    x = 10
    r = Shape.areaofsquare(x)
    assert x**2 == r
