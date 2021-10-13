from new_model import *
import pytest

def test_brick_obj_storing_attributes():
	'''Checks if Brick instances store attributes in a proper way'''
	
	b = Brick(5, 10, (0,0,0))
	assert b.x == 5
	assert b.y == 10
	assert b.color == (0,0,0)

	with pytest.raises(AssertionError):
		c = Brick('a', 3, (0,0,0))

	with pytest.raises(AssertionError):
		c = Brick(1, 3, ["abc"])


def test_Shape_objects():
	'''Checks if Shape instance creates proper attributes storing
	references to objects'''

	s = Shape([], [[(200,  -50, 100), (0, 0), (50, 0), (0, 50), (50, 50)]], [(200,  -50, 100), (0, 0), (50, 0), (0, 50), (50, 50)], (0,0,0))
	lst = s()
	assert type(lst) == list and len(lst) == 4
	assert lst[0].x == 200 and lst[0].y == -50 and lst[0].color == (0,0,0) 
	assert lst[1].x == 250 and lst[1].y == -50 and lst[1].color == (0,0,0)
	assert lst[2].x == 200 and lst[2].y == 0 and lst[2].color == (0,0,0)
	assert lst[3].x == 250 and lst[3].y == 0 and lst[3].color == (0,0,0)

	s = Shape([0], [[(200,  -50, 100), (0, 0), (50, 0), (0, 50), (50, 50)]], [(200,  -50, 100), (0, 0), (50, 0), (0, 50), (50, 50)], (0,0,0))
	lst = s()
	assert type(lst) == list and len(lst) == 5

	with pytest.raises(AssertionError):
		s = Shape([], 0, [(200,  -50, 100), (0, 0), (50, 0), (0, 50), (50, 50)], (0,0,0))

	with pytest.raises(AssertionError):
		s = Shape([0], [[(200,  -50, 100), (0, 0), (50, 0), (0, 50), (50, 50)]], 'd', (0,0,0))


def test_CanFall():
	'''Checks if CanFall method prevents from falling in proper circumstances'''

	s = Shape([Brick(200, 50, (0,0,0))], [[(200,  -50, 100), (0, 0), (50, 0), (0, 50), (50, 50)]], [(200,  -50, 100), (0, 0), (50, 0), (0, 50), (50, 50)], (0,0,0))
	assert not s.CanFall()

	s = Shape([Brick(0, 0, (0,0,0))], [[(200,  650, 100), (0, 0), (50, 0), (0, 50), (50, 50)]], [(200,  650, 100), (0, 0), (50, 0), (0, 50), (50, 50)], (0,0,0))
	assert not s.CanFall()

	s = Shape([Brick(0, 0, (0,0,0))], [[(200,  -50, 100), (0, 0), (50, 0), (0, 50), (50, 50)]], [(200,  -50, 100), (0, 0), (50, 0), (0, 50), (50, 50)], (0,0,0))
	assert s.CanFall()


def test_SFall():
	'''Checks if SFall method properly changes object's y coordinates'''
	
	s = Shape([], [[(200,  -50, 100), (0, 0), (50, 0), (0, 50), (50, 50)]], [(200,  -50, 100), (0, 0), (50, 0), (0, 50), (50, 50)], (0,0,0))
	ret = s.SFall()
	lst = s()
	assert ret == 0
	assert lst[0].x == 200 and lst[0].y == 0 and lst[0].color == (0,0,0) 
	assert lst[1].x == 250 and lst[1].y == 0 and lst[1].color == (0,0,0)
	assert lst[2].x == 200 and lst[2].y == 50 and lst[2].color == (0,0,0)
	assert lst[3].x == 250 and lst[3].y == 50 and lst[3].color == (0,0,0)


def test_CanMoveRight():
	'''Checks if CanMoveRight method prevents from moving right in proper circumstances'''
	
	s = Shape([Brick(300, 0, (0,0,0))], [[(200,  -50, 100), (0, 0), (50, 0), (0, 50), (50, 50)]], [(200,  -50, 100), (0, 0), (50, 0), (0, 50), (50, 50)], (0,0,0))
	assert not s.CanMoveRight()

	s = Shape([Brick(0, 0, (0,0,0))], [[(450,  650, 100), (0, 0), (50, 0), (0, 50), (50, 50)]], [(450,  650, 100), (0, 0), (50, 0), (0, 50), (50, 50)], (0,0,0))
	assert not s.CanMoveRight()

	s = Shape([Brick(0, 0, (0,0,0))], [[(200,  -50, 100), (0, 0), (50, 0), (0, 50), (50, 50)]], [(200,  -50, 100), (0, 0), (50, 0), (0, 50), (50, 50)], (0,0,0))
	assert s.CanMoveRight()


def test_MoveRight():
	'''Checks if MoveRight method properly changes object's x coordinates'''
	
	s = Shape([], [[(200,  -50, 100), (0, 0), (50, 0), (0, 50), (50, 50)]], [(200,  -50, 100), (0, 0), (50, 0), (0, 50), (50, 50)], (0,0,0))
	ret = s.MoveRight()
	lst = s()
	assert ret == 250
	assert lst[0].x == 250 and lst[0].y == -50 and lst[0].color == (0,0,0) 
	assert lst[1].x == 300 and lst[1].y == -50 and lst[1].color == (0,0,0)
	assert lst[2].x == 250 and lst[2].y == 0 and lst[2].color == (0,0,0)
	assert lst[3].x == 300 and lst[3].y == 0 and lst[3].color == (0,0,0)


def test_CanMoveLeft():
	'''Checks if CanMoveLeft method prevents from moving left in proper circumstances'''
	
	s = Shape([Brick(150, 0, (0,0,0))], [[(200,  -50, 100), (0, 0), (50, 0), (0, 50), (50, 50)]], [(200,  -50, 100), (0, 0), (50, 0), (0, 50), (50, 50)], (0,0,0))
	assert not s.CanMoveLeft()

	s = Shape([Brick(500, 0, (0,0,0))], [[(0,  650, 100), (0, 0), (50, 0), (0, 50), (50, 50)]], [(0,  650, 100), (0, 0), (50, 0), (0, 50), (50, 50)], (0,0,0))
	assert not s.CanMoveLeft()

	s = Shape([Brick(500, 0, (0,0,0))], [[(200,  -50, 100), (0, 0), (50, 0), (0, 50), (50, 50)]], [(200,  -50, 100), (0, 0), (50, 0), (0, 50), (50, 50)], (0,0,0))
	assert s.CanMoveLeft()


def test_MoveLeft():
	'''Checks if MoveLeft method properly changes object's x coordinates'''
	
	s = Shape([], [[(200,  -50, 100), (0, 0), (50, 0), (0, 50), (50, 50)]], [(200,  -50, 100), (0, 0), (50, 0), (0, 50), (50, 50)], (0,0,0))
	ret = s.MoveLeft()
	lst = s()
	assert ret == 150
	assert lst[0].x == 150 and lst[0].y == -50 and lst[0].color == (0,0,0) 
	assert lst[1].x == 200 and lst[1].y == -50 and lst[1].color == (0,0,0)
	assert lst[2].x == 150 and lst[2].y == 0 and lst[2].color == (0,0,0)
	assert lst[3].x == 200 and lst[3].y == 0 and lst[3].color == (0,0,0)

