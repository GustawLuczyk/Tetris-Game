import AIgamer, new_model
model = new_model


def test_LowestInShape():
	'''Checks if the method returns correct list'''

	ai = AIgamer.PosPlaceHandler()
	lst = ai.LowestInShape([(200, -50, 150), (0, 0), (50, 0), (50, 50), (100, 50)], 150)
	assert lst == [0, 50, 50]


def test_MaxInColumns2():
	'''Checks if the method returns correct list.'''
	
	ai = AIgamer.PosPlaceHandler()
	obj_lst = [model.Brick(0, 400, (0,0,0)), model.Brick(0, 450, (0,0,0)), model.Brick(50, 700, (0,0,0)), 
	model.Brick(50, 0, (0,0,0)), model.Brick(50, 0, (0,0,0)), model.Brick(50, 0, (0,0,0)), model.Brick(50, 0, (0,0,0))] #last four provided in order to cover [:-4] requirenment
	lst = ai.MaxInColumns(150, 0, obj_lst)
	assert lst == [400, 700, 750] 


def test_PossiblePositions():
	'''Checks if the method returns possible positions'''

	ai = AIgamer.PosPlaceHandler()
	obj_lst = [model.Brick(0, 650, (0,0,0)), model.Brick(50, 700, (0,0,0)), model.Brick(400, 700, (0,0,0)),
	model.Brick(0, 0, (0,0,0)), model.Brick(0, 0, (0,0,0)), model.Brick(0, 0, (0,0,0)), model.Brick(0, 0, (0,0,0))]
	low_shape = ai.LowestInShape([(200, -100, 100), (0, 0), (0, 50), (50, 50), (50, 100)], 100)
	lst = ai.PossiblePositions(low_shape, 100, obj_lst)
	assert lst == [(0, 550), (50, 600), (400, 600)]


def test_PosPos_Handle():
	'''Check if PosPlaceHandler's Handle method correctly changes the list in the request'''

	obj_lst = [model.Brick(0, 650, (0,0,0)), model.Brick(50, 700, (0,0,0)), model.Brick(400, 700, (0,0,0)), 
	model.Brick(0, 0, (0,0,0)), model.Brick(0, 0, (0,0,0)), model.Brick(0, 0, (0,0,0)), model.Brick(0, 0, (0,0,0))]
	patt = [[(200, -150, 50), (0, 0), (0, 50), (0, 100), (0, 150)], [(200, 0, 200), (0, 0), (50, 0), (100, 0), (150, 0)]]
	ai = AIgamer.PosPlaceHandler()
	request = AIgamer.Request(obj_lst, patt, 0)
	ai.Handle(request)
	assert request.possible_positions == [(patt[0], [(0, 450), (50, 500), (100, 550), (150, 550), (200, 550), (250, 550), (300, 550), (350, 550), (400, 500), (450, 550)]),
	(patt[1], [(100, 700), (150, 700), (200, 700)])]

	obj_lst = [model.Brick(i * 50, 700, (0,0,0)) for i in range(10)]
	patt = [[(200, -150, 50), (0, 0), (0, 50), (0, 100), (0, 150)], [(200, 0, 200), (0, 0), (50, 0), (100, 0), (150, 0)]]
	ai = AIgamer.RowsHandler()
	request = AIgamer.Request(obj_lst, patt, 0)
	b = AIgamer.PosPlaceHandler()
	b.Handle(request)
	assert request.possible_positions == [([(200, -150, 50), (0, 0), (0, 50), (0, 100), (0, 150)], [(0, 500), (50, 500), (100, 500), (150, 500), (200, 500), (250, 500), (300, 550), (350, 550), (400, 550), (450, 550)]), ([(200, 0, 200), (0, 0), (50, 0), (100, 0), (150, 0)], [(0, 650), (50, 650), (100, 650), (300, 700)])]


	# [(0, 450), (50, 500), (100, 550), (150, 550), (200, 550), (250, 550), (300, 550), (350, 550), (400, 550), (450, 550)]
	# [(0, 500), (50, 500), (100, 550), (150, 550), (200, 550), (250, 550), (300, 550), (350, 550), (400, 550), (450, 550)]
	# [(0, 500), (50, 500), (100, 500), (150, 500), (200, 500), (250, 500), (300, 550), (350, 550), (400, 550), (450, 550)]


def test_CountObjsRows():
	'''Check if the method properly counts number of objects in obj_lst[:-4]'''

	obj_lst = [model.Brick(i * 50, 700, (0,0,0)) for i in range(10)]
	obj_lst.insert(0, model.Brick(0, 600, (0,0,0)))
	ai = AIgamer.RowsHandler()
	request = AIgamer.Request(obj_lst, [], 0)
	rows, y_coor = ai.CountObjsRows(request)
	row_y_coordinates = [700 - n * 50 for n in range(15)]
	assert rows == [6, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
	assert y_coor == row_y_coordinates


def test_RowsHandler_FindPossibilities():
	'''Check if the method FindPossibilities returns correctly modified list'''

	obj_lst = [model.Brick(200 + i * 50, 700, (0,0,0)) for i in range(10)]
	patt = [[(200, -150, 50), (0, 0), (0, 50), (0, 100), (0, 150)], [(200, 0, 200), (0, 0), (50, 0), (100, 0), (150, 0)]]
	ai = AIgamer.RowsHandler()
	request = AIgamer.Request(obj_lst, patt, 0)
	Pos = AIgamer.PosPlaceHandler()
	Pos.Handle(request)
	ret = ai.FindPossibilities(request)
	assert ret == [(patt[0], []), (patt[1], [(0, 700, 1)])]
