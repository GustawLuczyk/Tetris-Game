from abc import *
from typing import Iterable

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
		remains unchanged. Otherwise the list is being updated and contains positionings
		allowing removing rows'''
		
		positions_removing_rows = self.FindPossibilities(request)

		counter = 0
		for shape in positions_removing_rows:
			if len(shape[1]) != 0:
				counter += len(shape[1])

		if counter == 1:
			pass			#end the chain
		elif counter > 1:
			request.possible_positions = positions_removing_rows 

		
	def FindPossibilities(self, request: object):
		'''The algorithm of finding positions allowing removing shapes'''

		rows, row_y_coordinates = self.CountObjsRows(request)
		positions_removing_rows = [(shape[0], []) for shape in request.possible_positions]
		rows_copy = rows.copy()

		for shape in request.possible_positions:
			
			for shape_pos in shape[1]:	
				counter = 0			
				objs_positions = [shape_pos[1] + shape[0][i][1] for i in range(1, 5)]
				
				for pos in objs_positions:
					rows_copy[row_y_coordinates.index(pos)] += 1
					if rows_copy[row_y_coordinates.index(pos)] == 10:
						counter += 1
				
				rows_copy = rows.copy()
				if counter > 0:
					shape_to_append = (shape_pos[0], shape_pos[1], counter)
					positions_removing_rows[request.possible_positions.index(shape)][1].append(shape_to_append)			

		return positions_removing_rows

		
	def CountObjsRows(self, request: object) -> list:
		'''Count in rows objs from obj_lst'''

		rows = [0 for n in range(15)] 
		row_y_coordinates = [700 - n * 50 for n in range(15)]

		for obj in request.obj_lst[:-4]:
			rows[row_y_coordinates.index(obj.y)] += 1

		return rows, row_y_coordinates
