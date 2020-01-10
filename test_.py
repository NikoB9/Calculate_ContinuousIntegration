def test_addition():
	assert addition(1,1) == 2
	assert addition(40,2) == 42
	assert addition(100,addition(100,100)) == 300

def test_soustraction():
	assert soustraction(2,1) == 1
	assert soustraction(100,200) == -100
	assert soustraction(soustraction(100,10),1) == 89

def test_multiplication():
	assert multiplication(3,3) == 9
	assert multiplication(-3,3) == -9
	assert multiplication(-3,-3) == 9

def test_division():
	assert division(10,10) == 1
	assert division(10,2) == 5
	assert division(-100,10) == -10

def test_multipleOperations():
	assert division(10,addition(4,1)) == 2 
	assert multiplication(10,soustraction(10,9)) == 10)

