import precio

def test_1():
    assert precio.descuento(100,20) == 80



def test_2():
    assert precio.descuento(50,0) == 50
