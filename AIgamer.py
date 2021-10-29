#from tetris import Game
#game = Game

class BestPlace:
	'''An instance of this class finds best place
	for current falling shape'''

	def __init__(self, patterns, obj_lst):
		self.__shapes_patterns = patterns
		self.__obj_lst = obj_lst


	def FindPlace(self):
		'''Main method to find best place. Iterates over 
		shape's patterns'''

		good_places = []

		for shape_patt in self.__shapes_patterns:
			shape_length = shape_patt[0][2]
			low_shape = self.LowestInShape(shape_patt, shape_length)
			good_places = self.PossiblePositions(low_shape, shape_length)
			
		#	x = 0
		#	while x + shape_length < 500:
		#		max_in_columns = self.MaxInColumns(shape_length, x)							
		#		self.PossiblePosition(max_shape, shape_length)
		#		x += 50


	def PossiblePositions(self, low_shape, shape_length):
		'''Returns posible shape's positions [(x, y) ... n] excluding those that 
		create free spaces below the shape.'''

		lst = []
		x = 0
		while x + shape_length < 500:
			max_in_columns = self.MaxInColumns(shape_length, x)							
			a = [max_in_columns[i] - 50 - low_shape[i] for i in range(len(low_shape))]
			if max(a) == min(a):
				lst.append((x, a[0]))
			x += 50
		
		return lst


	def LowestInShape(self, shape_patt, shape_length):
		'''Saves lowest parts of a shape in the list [y0, ... yn]'''

		lst = []

		for i in range(shape_length // 50):
			lst.append(max([coordinates[1] for coordinates in shape_patt[1:] if coordinates[0] == i*50]))
		
		return lst


	def MaxInColumns(self, shape_length, x):
		'''Finds highest brick objects in columns that are considered and returns
		them in a list [y0, ... yn]'''

		lst = []

		for i in range(shape_length // 50):
			a = [obj.y for obj in self.__obj_lst[:-4] if obj.x == x + i*50]
			if len(a) != 0:
				lst.append(min(a))
			else:
				lst.append(750)
				
		return lst