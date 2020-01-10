import fonction

def test_addition():
	assert fonction.addition(1,1) == 2
	assert fonction.addition(40,2) == 42
	assert fonction.addition(100,fonction.addition(100,100)) == 300

def test_soustraction():
	assert fonction.soustraction(2,1) == 1
	assert fonction.soustraction(100,200) == -100
	assert fonction.soustraction(fonction.soustraction(100,10),1) == 89

def test_multiplication():
	assert fonction.multiplication(3,3) == 9
	assert fonction.multiplication(-3,3) == -9
	assert fonction.multiplication(-3,-3) == 9

def test_division():
	assert fonction.division(10,10) == 1
	assert fonction.division(10,2) == 5
	assert fonction.division(-100,10) == -10

def test_multipleOperations():
	assert fonction.division(10,fonction.addition(4,1)) == 2 
	assert fonction.division(10,fonction.addition(4,6)) == 1 
	assert fonction.multiplication(10,fonction.soustraction(10,9)) == 10

