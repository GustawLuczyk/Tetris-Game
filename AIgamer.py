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
		remains unchanged. Otherwise the list is being updated and contains positionings
		allowing removing rows'''
		
		positions_removing_rows = self.FindPossibilities(request)

		max = 1
		positions = []
		for shape in positions_removing_rows:
			if len(shape[1]) == 0:
				positions_removing_rows.remove(shape)
			else:
				app_in_shape = []
				for pos in shape[1]:
					if pos[2] == max:
						app = (pos[0], pos[1])
						app_in_shape.append(app)
				if len(app_in_shape) > 0:
					app = (shape[0], app_in_shape)
					positions.append(app)


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

		max = 1
		for shape in request.possible_positions:
			
			can_remove_row = False
			for shape_pos in shape[1]:	
				counter = 0			
				objs_positions = [shape_pos[1] + shape[0][i][1] for i in range(1, 5)]
				
				for pos in objs_positions:
					rows_copy[row_y_coordinates.index(pos)] += 1
					if rows_copy[row_y_coordinates.index(pos)] == 10:
						counter += 1
						can_remove_row = True
				
				rows_copy = rows.copy()
				if counter == max:
					for shape1 in positions_removing_rows:
						if shape1[0] == shape[0]:
							shape1[1].append(shape_pos)

				elif counter > max:
					max = counter					
					index = 0
					for shape1 in positions_removing_rows:
						if shape1[0] != shape[0]:
							index += 1
						elif shape1[0] == shape[0]:
							break
					for i in range(index):
						positions_removing_rows.remove(positions_removing_rows[0])
					positions_removing_rows[0][1] = [shape_pos]

			if not can_remove_row:										
				for shape1 in positions_removing_rows:
					if shape1[0] == shape[0]:
						positions_removing_rows.remove(shape1)

		return positions_removing_rows

		
	def CountObjsRows(self, request: object) -> list:
		'''Count in rows objs from obj_lst'''

		rows = [0 for n in range(15)] 
		row_y_coordinates = [700 - n * 50 for n in range(15)]

		for obj in request.obj_lst[:-4]:
			rows[row_y_coordinates.index(obj.y)] += 1

		return rows, row_y_coordinates



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

	

		


