from abc import *
from typing import Iterable
import random



class AIprocessor:
	'''Used by client to create logic chains'''

	def __init__(self, obj_lst, patt, position, ev_queue):
		pass


class Request:
	'''Creates request objects'''
	
	def __init__(self, obj_lst: Iterable, patt: Iterable, position: Iterable):
		self.__obj_lst = obj_lst
		self.__pattern = patt
		self.__position = position
		self.__possible_positions = []	
		self.__final_position = None	


	@property
	def obj_lst(self):
		return self.__obj_lst


	@obj_lst.setter
	def obj_lst(self, obj_lst):
		self.__obj_lst = obj_lst


	@property
	def pattern(self):
		return self.__pattern


	@pattern.setter
	def pattern(self, pattern):
		self.__pattern = pattern


	@property
	def position(self):
		return self.__position


	@position.setter
	def position(self, position):
		self.__position = position


	@property
	def possible_positions(self):
		return self.__possible_positions


	@possible_positions.setter
	def possible_positions(self, pos):
		self.__possible_positions = pos


	@property
	def final_position(self):
		return self.__final_position


	@final_position.setter
	def final_position(self, pos):
		self.__final_position = pos



class BaseHandler(metaclass=ABCMeta):
	'''Abstract class declaring an interface for handlers'''
	

	@classmethod
	def __subclasshook__(cls, subclass):
		return (hasattr(subclass, 'Handle') and 
				callable(subclass.Handle) or 
				NotImplemented)


	@abstractmethod
	def Handle(self, path: str, file_name: str):
		'''Handle the request'''
		raise NotImplementedError



class PosPlaceHandler(BaseHandler):
	'''Find best place for current falling shape'''


	def __init__(self):
		pass


	def Handle(self, request: object):
		'''Main method to find best place. Iterates over 
		shape's patterns. Returns list: [(shape_patt, [(x, y), ... n]) ... n]'''

		possible_positions = []
		obj_lst = request.obj_lst

		for shape_patt in request.pattern:			
			shape_length = shape_patt[0][2]
			low_shape = self.LowestInShape(shape_patt, shape_length)
			positions = self.PossiblePositions(low_shape, shape_length, obj_lst)
			pos = (shape_patt, positions)
			possible_positions.append(pos)
		return request.possible_positions.extend(possible_positions)


	def PossiblePositions(self, low_shape, shape_length, obj_lst):
		'''Returns posible shape's positions [(x, y) ... n] excluding those that 
		create empty spaces below the shape.'''

		lst = []
		x = 0
		while x + shape_length <= 500:
			max_in_columns = self.MaxInColumns(shape_length, x, obj_lst)							
			a = [max_in_columns[i] - 50 - low_shape[i] for i in range(len(low_shape))]
			if max(a) == min(a):
				lst.append((x, a[0]))
			x += 50
		
		return lst


	def LowestInShape(self, shape_patt: Iterable, shape_length: int):
		'''Saves lowest parts of a shape in the list [y0, ... yn]'''

		lst = []

		for i in range(shape_length // 50):
			lst.append(max([coordinates[1] for coordinates in shape_patt[1:] if coordinates[0] == i*50]))
		
		return lst


	def MaxInColumns(self, shape_length, x, obj_lst):
		'''Finds highest brick objects in columns that are being considered and returns
		them in a list [y0, ... yn]'''

		lst = []

		for i in range(shape_length // 50):
			a = [obj.y for obj in obj_lst[:-4] if obj.x == x + i*50]
			if len(a) != 0:
				lst.append(min(a))
			else:
				lst.append(750)
				
		return lst



class RowsHandler(BaseHandler):
	'''Find positionings that allow deleting a row; discard the rest of
	positionings'''


	def __init__(self):
		pass


	def Handle(self, request: object):
		'''Check the possibility of removing rows. If no possibility, possible_positions list
		remains unchanged. Otherwise the list containing positions allowing removing rows
		is being updated'''
		
		positions_removing_rows = self.FindPossibilities(request)
		length = len(positions_removing_rows)

		if length > 1:
			request.possible_positions = positions_removing_rows
		elif length == 1:
			if len(positions_removing_rows[0][1]) > 1:
				request.possible_positions = positions_removing_rows
			elif len(positions_removing_rows[0][1]) == 1:
				request.final_position = positions_removing_rows[0]

		
	def FindPossibilities(self, request: object):
		'''Create list with positions, that allow removing the highest number of rows'''

		max = 1
		positions_removing_rows = []
		for shape in request.possible_positions:
			positions = []
			for shape_pos in shape[1]:			
				counter = self.CountRowsSupposition(request, shape[0], shape_pos)			
				if counter == max:
					positions.append(shape_pos)
				elif counter > max:
					positions.clear()
					positions.append(shape_pos)
			
			if len(positions) > 0:
				positions_removing_rows.append((shape[0], positions))

		return positions_removing_rows


	def CountRowsSupposition(self, request, patt, shape_pos):
		'''Count how many there would be objects in rows if shape was placed
		in shape_pos position'''

		rows, row_y_coordinates = self.CountObjsRows(request)
		rows_copy = rows.copy()
		objs_positions = [shape_pos[1] + patt[i][1] for i in range(1, 5)]

		counter = 0
		for pos in objs_positions:
			rows_copy[row_y_coordinates.index(pos)] += 1
			if rows_copy[row_y_coordinates.index(pos)] == 10:
				counter += 1		

		return counter



class LevelHandler(BaseHandler):
	'''Check which position is the lowest and choose final position'''


	def __init__(self):
		pass


	def Handle(self, request: object):
		'''Find lowest positions and choose one of them randomly - that is the
		final position'''

		min, patts = self.FindMinPatt(request)

		patt = random.choice(patts)
		min_positions = []

		for shape in request.possible_positions:
			if patt == shape[0]:
				for pos in shape[1]:
					if pos[1] == min:
						min_positions.append(pos)

		min_pos = random.choice(min_positions)
		request.final_position = (patt, min_pos)


	def FindMinPatt(self, request: object):
		'''Find lowest positions (highest y coordinate value) and shape patterns
		in which they occur'''

		min = 0
		patts = []

		for shape in request.possible_positions:
			for pos in shape[1]:
				if pos[1] == min and shape[0] not in patts:
					patts.append(shape[0])
				elif pos[1] > min:
					min = pos[1]
					patts.clear()
					patts.append(shape[0])

		return min, patts

	

		


