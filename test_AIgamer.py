import AIgamer, new_model
model = new_model


def test_LowestInShape():
	'''Checks if the method returns correct list'''

	ai = AIgamer.BestPlace([[(200, -50, 150), (0, 0), (50, 0), (50, 50), (100, 50)], [(200, -100, 100), (50, 0), (0, 50), (50, 50), (0, 100)]], [])
	lst = ai.LowestInShape([(200, -50, 150), (0, 0), (50, 0), (50, 50), (100, 50)], 150)
	assert lst == [0, 50, 50]


def test_MaxInColumns():
	'''Checks if the method returns correct list'''

	ai = AIgamer.BestPlace([], [model.Brick(0, 400, (0,0,0)), model.Brick(0, 450, (0,0,0)), model.Brick(50, 700, (0,0,0)), model.Brick(50, 0, (0,0,0)), model.Brick(50, 0, (0,0,0)), model.Brick(50, 0, (0,0,0)), model.Brick(50, 0, (0,0,0))])
	lst = ai.MaxInColumns(150, 0)
	assert lst == [400, 700, 750] 