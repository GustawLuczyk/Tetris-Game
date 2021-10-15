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
	s.SFall()
	y = s.__getattribute__('_Shape__y_coordinate')
	lst = s()
	
	assert y == 0
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
	s.MoveRight()
	x = s.__getattribute__('_Shape__x_coordinate')
	lst = s()

	assert x == 250
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
	s.MoveLeft()
	x = s.__getattribute__('_Shape__x_coordinate')
	lst = s()

	assert x == 150
	assert lst[0].x == 150 and lst[0].y == -50 and lst[0].color == (0,0,0) 
	assert lst[1].x == 200 and lst[1].y == -50 and lst[1].color == (0,0,0)
	assert lst[2].x == 150 and lst[2].y == 0 and lst[2].color == (0,0,0)
	assert lst[3].x == 200 and lst[3].y == 0 and lst[3].color == (0,0,0)


def test_Shape_Rotate():
	'''Tests if Rotate method changes "my_objects" coordinates correctly'''
	

	s = Shape([], [[(200, -150, 50), (0, 0), (0, 50), (0, 100), (0, 150)], [(200, 0, 200), (0, 0), (50, 0), (100, 0), (150, 0)]], [(200, -150, 50), (0, 0), (0, 50), (0, 100), (0, 150)], (0,0,0))
	lst = s()

	s.Rotate()
	index = s.__getattribute__('_Shape__shapes_index')
	assert lst[0].x == 200 and lst[0].y == -150
	assert lst[1].x == 250 and lst[1].y == -150
	assert lst[2].x == 300 and lst[2].y == -150
	assert lst[3].x == 350 and lst[3].y == -150
	assert index == 1

	s.Rotate()
	index = s.__getattribute__('_Shape__shapes_index')
	assert lst[0].x == 200 and lst[0].y == -150
	assert lst[1].x == 200 and lst[1].y == -100
	assert lst[2].x == 200 and lst[2].y == -50
	assert lst[3].x == 200 and lst[3].y == 0
	assert index == 0


def test_Shape_no_Rotate():
	'''Tests if Shapes Rotate method rotates in allowing circumstances'''

	s = Shape([Brick(250, -150, (0,0,0))], [[(200, -150, 50), (0, 0), (0, 50), (0, 100), (0, 150)], [(200, 0, 200), (0, 0), (50, 0), (100, 0), (150, 0)]], [(200, -150, 50), (0, 0), (0, 50), (0, 100), (0, 150)], (0,0,0))
	lst = s()

	s.Rotate()
	index = s.__getattribute__('_Shape__shapes_index')
	assert index == 0	

	s = Shape([], [[(400, -150, 50), (0, 0), (0, 50), (0, 100), (0, 150)], [(400, 0, 200), (0, 0), (50, 0), (100, 0), (150, 0)]], [(400, -150, 50), (0, 0), (0, 50), (0, 100), (0, 150)], (0,0,0))
	lst = s()

	s.Rotate()
	index = s.__getattribute__('_Shape__shapes_index')
	assert index == 0


def test_ShapesBase():
	'''Tests if ShapesBase obj properly passes attributes'''

	s = ShapesBase()
	gen_shape, shape, color = s.GetCurrentShape()
	shape1, shape2, shape3 = s.GetSucceedingShapes()

	s.Succeed()
	gen_shapeB, shapeB, colorB = s.GetCurrentShape()
	shape1B, shape2B, shape3B = s.GetSucceedingShapes()
	
	assert type(gen_shape) == list
	assert shape in gen_shape
	assert color in [(215,35,35), (255,179,26), (102,255,178), (76,153,0), (0,0,204), (153,0,76), (255,255,0)]
	assert type(gen_shapeB) == list
	assert colorB == shape1[1]
	assert shape1[0] == shapeB
	assert shape2 == shape1B
	assert shape3 == shape2B
	assert type(shape3B) == tuple
	

def test_Rows_attrs():
	'''Tests if Row creates attributes properly'''

	rows = Rows(5)
	r = rows.__getattribute__('_Rows__rows')
	y_coor = rows.__getattribute__('_Rows__row_y_coordinates')

	assert len(r) == 5
	assert y_coor == [700, 650, 600, 550, 500]


def test_adding_to_rows():
	'''Tests if Row's method AddToRows adds given objs to proper rows'''

	rows = Rows(5)
	rows.AddToRows([Brick(0, n * 50 + 500, (0,0,0)) for n in range(5)])

	r = rows.__getattribute__('_Rows__rows')
	for count, row in enumerate(r):
		assert row[0].y ==  700 - count * 50
	

def test_removing_rows():
	'''Tests the way Rows' method RemoveRows removes rows'''

	obj_lst = [Brick(n * 50, 700, (0,0,0)) for n in range(10)]
	obj_lst.extend([Brick(n * 50, 500, (0,0,0)) for n in range(10)])
	r = Rows(5)
	r.AddToRows(obj_lst)
	obj_lst = r.RemoveRows(obj_lst)
	
	assert len(obj_lst) == 0
