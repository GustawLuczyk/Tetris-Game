from tetris import Game
game = Game

class BestPlace:
	'''An instance of this class finds best place
	for current falling shape'''

	def __init__(self):
		self.__shapes_pattern, self.__obj_lst = game.GetPositions
		self.__good_places = []


	def FindPlace(self):
		'''Main method to find best place. Iterates over 
		shape's patterns'''

		for shape_patt in self.__shapes_pattern:
			shape_length = shape_patt[0][2]
			max_shape = self.LowestInShape(shape_patt, shape_length)
			
			x = 0
			while x + shape_length < 500:
				max_in_columns = self.MaxInColumns(shape_length, x)							
				self.PossiblePosition(max_shape, max_in_columns)
				x += 50


	def PossiblePosition(self, max_shape, max_in_columns):
		'''Provides shape's possible positioning'''
		
		#x = 0
		#while x + shape_length < 500:
			#x += 50

		return max([max_in_columns[i] - 50 - max_shape[i] for i in range(len(max_shape))])


	def LowestInShape(self, shape_patt, shape_length):
		'''Saves lowest parts of a shape in the list'''

		lst = []

		for i in range(shape_length // 50):
			lst.append(max([coordinates[1] for coordinates in shape_patt[1:] if coordinates[0] == i*50]))
		
		return lst


	def MaxInColumns(self, shape_length, x):
		'''Finds highest brick objects in columns that are considered'''

		lst = []

		for i in range(shape_length // 50):
			lst.append(max([obj.y for obj in self.__obj_lst[:-4] if obj.x == x + i*50]))

		return lst