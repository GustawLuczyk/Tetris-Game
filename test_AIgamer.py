import AIgamer, new_model
model = new_model


def test_PosPlaceHandler_LowestInShape():
	'''Checks if the method returns correct list'''

	request = AIgamer.Request([], [], 0)
	ai = AIgamer.PosPlaceHandler(request)
	lst = ai.LowestInShape([(200, -50, 150), (0, 0), (50, 0), (50, 50), (100, 50)], 150)
	
	assert lst == [0, 50, 50]


def test_PosPlaceHandler_MaxInColumns2():
	'''Checks if the method returns correct list.'''
	
	request = AIgamer.Request([], [], 0)
	ai = AIgamer.PosPlaceHandler(request)
	obj_lst = [model.Brick(0, 400, (0,0,0)), model.Brick(0, 450, (0,0,0)), model.Brick(50, 700, (0,0,0)), 
	model.Brick(50, 0, (0,0,0)), model.Brick(50, 0, (0,0,0)), model.Brick(50, 0, (0,0,0)), model.Brick(50, 0, (0,0,0))] #last four provided in order to cover [:-4] requirenment
	lst = ai.MaxInColumns(150, 0, obj_lst)
	
	assert lst == [400, 700, 750] 


def test_PosPlaceHandler_PossiblePositions():
	'''Checks if the method returns possible positions'''
	
	request = AIgamer.Request([], [], 0)
	ai = AIgamer.PosPlaceHandler(request)
	obj_lst = [model.Brick(0, 650, (0,0,0)), model.Brick(50, 700, (0,0,0)), model.Brick(400, 700, (0,0,0)),
	model.Brick(0, 0, (0,0,0)), model.Brick(0, 0, (0,0,0)), model.Brick(0, 0, (0,0,0)), model.Brick(0, 0, (0,0,0))]
	low_shape = ai.LowestInShape([(200, -100, 100), (0, 0), (0, 50), (50, 50), (50, 100)], 100)
	lst = ai.PossiblePositions(low_shape, 100, obj_lst)
	
	assert lst == [(0, 550), (50, 600), (400, 600)]


def test_PosPlaceHandler_Handle():
	'''Check if PosPlaceHandler's Handle method correctly changes the list in the request'''

	obj_lst = [model.Brick(0, 650, (0,0,0)), model.Brick(50, 700, (0,0,0)), model.Brick(400, 700, (0,0,0)), 
	model.Brick(0, 0, (0,0,0)), model.Brick(0, 0, (0,0,0)), model.Brick(0, 0, (0,0,0)), model.Brick(0, 0, (0,0,0))]
	patt = [[(200, -150, 50), (0, 0), (0, 50), (0, 100), (0, 150)], [(200, 0, 200), (0, 0), (50, 0), (100, 0), (150, 0)]]
	request = AIgamer.Request(obj_lst, patt, 0)
	ai = AIgamer.PosPlaceHandler(request)
	ai.Handle()
	
	assert request.possible_positions == [(patt[0], 
	[(0, 450), (50, 500), (100, 550), (150, 550), (200, 550), (250, 550), (300, 550), (350, 550), (400, 500), (450, 550)]),
	(patt[1], [(100, 700), (150, 700), (200, 700)])]

	obj_lst = [model.Brick(i * 50, 700, (0,0,0)) for i in range(10)]
	patt = [[(200, -150, 50), (0, 0), (0, 50), (0, 100), (0, 150)], [(200, 0, 200), (0, 0), (50, 0), (100, 0), (150, 0)]]
	request = AIgamer.Request(obj_lst, patt, 0)
	ai = AIgamer.PosPlaceHandler(request)
	ai.Handle()

	assert request.possible_positions == [([(200, -150, 50), (0, 0), (0, 50), (0, 100), (0, 150)], 
	[(0, 500), (50, 500), (100, 500), (150, 500), (200, 500), (250, 500), (300, 550), (350, 550), (400, 550), (450, 550)]), 
	([(200, 0, 200), (0, 0), (50, 0), (100, 0), (150, 0)], [(0, 650), (50, 650), (100, 650), (300, 700)])]


def test_RowsHandler_CountObjsRows():
	'''Check if the method properly counts number of objects in obj_lst[:-4] 
	(exclude shapes objects)'''

	obj_lst = [model.Brick(50 + i * 50, 700, (0,0,0)) for i in range(9)] 
	obj_lst.extend([model.Brick(50 + i * 50, 650, (0,0,0)) for i in range(9)])
	obj_lst.extend([model.Brick(200 + i * 50, 600, (0,0,0)) for i in range(10)])
	request = AIgamer.Request(obj_lst, [], 0)
	ai = AIgamer.RowsHandler(request)	
	rows, y_coor = ai.CountObjsRows()
	row_y_coordinates = [700 - n * 50 for n in range(15)]
	
	assert rows == [9, 9, 6, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
	assert y_coor == row_y_coordinates


def test_RowsHandler_CountRowsSupposition():
	'''Check if the method correctly counts number of rows that could be removed'''

	obj_lst = [model.Brick(50 + i * 50, 700, (0,0,0)) for i in range(9)] 
	obj_lst.extend([model.Brick(50 + i * 50, 650, (0,0,0)) for i in range(9)])
	obj_lst.extend([model.Brick(200 + i * 50, 600, (0,0,0)) for i in range(10)])
	patt = [(200, -150, 50), (0, 0), (0, 50), (0, 100), (0, 150)]
	request = AIgamer.Request(obj_lst, [], 0)
	ai = AIgamer.RowsHandler(request)
	counter = ai.CountRowsSupposition(request, patt, (0, 550))
	assert counter == 2


def test_RowsHandler_Handle():
	'''Check if the method saves proper positions according to the established
	data structure'''

	obj_lst = [model.Brick(50 + i * 50, 700, (0,0,0)) for i in range(9)] 
	obj_lst.extend([model.Brick(50 + i * 50, 650, (0,0,0)) for i in range(9)])
	obj_lst.extend([model.Brick(200 + i * 50, 700, (0,0,0)) for i in range(10)])
	patt = [[(200, -150, 50), (0, 0), (0, 50), (0, 100), (0, 150)], [(200, 0, 200), (0, 0), (50, 0), (100, 0), (150, 0)]]
	request = AIgamer.Request(obj_lst, patt, 0)
	ai = AIgamer.RowsHandler(request)	
	request.possible_positions = [(patt[0], [(50, 400), (0, 550), (450, 350)]), (patt[1], [(0, 550), (300, 500)])]
	ai.Handle()

	assert request.possible_positions == [(patt[0], [(0, 550)])]


def test_LevelHandler_FindMinPatt():
	'''Check if the method finds the lowest position's value and if it records
	patterns that contain that position'''

	patt = [[(200, -100, 100), (0, 0), (0, 50), (50, 50), (0, 100)], [(200, -50, 150), (0, 0), (50, 0), (100, 0), (50, 50)],
	[(200, -100, 100), (50, 0), (0, 50), (50, 50), (50, 100)], [(200, -50, 150), (50, 0), (0, 50), (50, 50), (100, 50)]]	
	request = AIgamer.Request([], patt, 0)
	ai = AIgamer.LevelHandler(request)
	request.possible_positions = [(patt[0], []), (patt[1], []), (patt[2], [(0, 500), (0, 550), (50, 550)]), (patt[3], [(0, 550)])]
	min, patts = ai.FindMinPatt()

	assert min == 550
	assert patts == [patt[2], patt[3]]


def test_LevelHandler_Handle():
	'''Check if the method chooses the lowest random position and
	if saves it correctly'''

	patt = [[(200, -100, 100), (0, 0), (0, 50), (50, 50), (0, 100)], [(200, -50, 150), (0, 0), (50, 0), (100, 0), (50, 50)],
	[(200, -100, 100), (50, 0), (0, 50), (50, 50), (50, 100)], [(200, -50, 150), (50, 0), (0, 50), (50, 50), (100, 50)]]
	request = AIgamer.Request([], patt, 0)
	ai = AIgamer.LevelHandler(request)
	request.possible_positions = [(patt[0], []), (patt[1], []), (patt[2], [(0, 500), (0, 550), (50, 550)]), (patt[3], [(0, 550)])]
	ai.Handle()

	assert request.final_position[0] in [patt[2], patt[3]]
	assert request.final_position[1] in [(0, 550), (50, 550)]


def test_BaseHandler():
	'''Check if the handler invokes next handler when there is more than
	one possible position'''

	next = AIgamer.BaseHandler(None, None, None)
	base = AIgamer.BaseHandler(AIgamer.PosPlaceHandler, request, next)
