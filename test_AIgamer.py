import AIgamer, new_model
model = new_model


def test_LowestInShape():
	'''Checks if the method returns correct list'''

	ai = AIgamer.PosPlaceHandler()
	lst = ai.LowestInShape([(200, -50, 150), (0, 0), (50, 0), (50, 50), (100, 50)], 150)
	assert lst == [0, 50, 50]


def test_MaxInColumns2():
	'''Checks if the method returns correct list'''

	ai = AIgamer.PosPlaceHandler()
	lst = ai.MaxInColumns(150, 0, [model.Brick(0, 400, (0,0,0)), model.Brick(0, 450, (0,0,0)), model.Brick(50, 700, (0,0,0)), model.Brick(50, 0, (0,0,0)), model.Brick(50, 0, (0,0,0)), model.Brick(50, 0, (0,0,0)), model.Brick(50, 0, (0,0,0))])
	assert lst == [400, 700, 750] 


def test_PossiblePositions():
	'''Checks if the method returns possible positions'''

	ai = AIgamer.PosPlaceHandler()
	low_shape = ai.LowestInShape([(200, -100, 100), (0, 0), (0, 50), (50, 50), (50, 100)], 100)
	lst = ai.PossiblePositions(low_shape, 100, [model.Brick(0, 650, (0,0,0)), model.Brick(50, 700, (0,0,0)), model.Brick(0, 400, (0,0,0)), model.Brick(0, 450, (0,0,0)), model.Brick(50, 700, (0,0,0)), model.Brick(50, 0, (0,0,0))])
	assert lst == [(0, 550), (50, 600)]