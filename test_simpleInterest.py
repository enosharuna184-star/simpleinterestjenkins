from simpleInterest import simInt

def test_simpleInt_pos():
    assert simInt(20000, 9, 12) == 19200

def test_simpleInt_zer():
    assert simInt(10000, 7, 0) == 0 
    
def test_simpleInt_neg():
    assert simInt(30000, 5, 2) == 3000

