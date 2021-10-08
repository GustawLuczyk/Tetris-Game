import random


class Brick():			
	def __init__(self, x, y, color):
		self.x = x
		self.y = y
		self.color = color
		
	@property
	def x(self):
		return self.__x
        
	@x.setter
	def x(self, x):
		self.__x = x
        
	@property
	def y(self):
		return self.__y
        
	@y.setter
	def y(self, y):
		self.__y = y
        
	@property
	def color(self):
		return self.__color
        
	@color.setter
	def color(self, color):
		self.__color = color
        		
	def __del__(self):
		pass


		
class Shape():
	
	def __init__(self, lst, gen_shape, shape, color):
		
		self.__objects_list = lst
		self.__my_objects = []
		self.__general_shape = gen_shape
		self.__my_shape = shape
		self.__shapes_index = self.__general_shape.index(self.__my_shape)
		
		self.__x_coordinate = self.__my_shape[0][0]
		self.__y_coordinate = self.__my_shape[0][1]
		
		for i in range(1, 5):
			self.__my_objects.append(Brick(self.__x_coordinate + self.__my_shape[i][0], self.__y_coordinate + self.__my_shape[i][1], color))
	
	
	def __call__(self):
		'''Returns updated objects list'''
		
		return self.__objects_list + self.__my_objects
		
		
	def CanFall(self):
		'''Checks falling shape's possibility to fall'''
		
		for obj in self.__objects_list:
			for my_obj in self.__my_objects:
				if obj.x == my_obj.x and obj.y == my_obj.y + 50:
					return False			
		for obj in self.__my_objects:			
			if obj.y == 700:
				return False
				
		return True
		
		  
	def SFall(self):
		'''Orders shape's objects to fall'''
		
		for obj in self.__my_objects:
			obj.y = obj.y + 50
		self.__y_coordinate = self.__y_coordinate + 50 
		
		
	def CanMoveRight(self):
		'''Checks shape's possiblity to move right'''
	
		for obj in self.__objects_list:
			for my_obj in self.__my_objects:
				if obj.x == my_obj.x + 50 and obj.y == my_obj.y:
						return False
																				
		if self.__x_coordinate + self.__my_shape[0][2] < 500:
			return True
		
		
	def MoveRight(self):
		'''Moves the shape to the left'''
				
		if self.CanMoveRight():
			self.__x_coordinate = self.__x_coordinate + 50 
			for my_obj in self.__my_objects:
				my_obj.x = my_obj.x + 50
		
		
	def CanMoveLeft(self):
		'''Checks shape's possiblity to move left'''
		
		for obj in self.__objects_list:
			for my_obj in self.__my_objects:
				if obj.x == my_obj.x - 50 and obj.y == my_obj.y:
					return False											
		if self.__x_coordinate > 0:
			return True
			
	
	def MoveLeft(self):
		'''Moves the shape to the left'''		
		
		if self.CanMoveLeft():
			self.__x_coordinate = self.__x_coordinate - 50
			for my_obj in self.__my_objects:
				my_obj.x = my_obj.x - 50
				
	
	def Rotate(self):
		'''Rotates falling shapes only if shape's position allowes to do so'''
		
		if self.__general_shape[self.__shapes_index] != self.__general_shape[-1]:
			self.__shapes_index = self.__shapes_index + 1
			self.__my_shape = self.__general_shape[self.__shapes_index]
		else:
			self.__shapes_index = 0
			self.__my_shape = self.__general_shape[self.__shapes_index]
			
		cannot_rotate = False
		for i in range(4):
			x = self.__x_coordinate + self.__my_shape[i + 1][0]
			y = self.__y_coordinate + self.__my_shape[i + 1][1]			
			self.__my_objects[i].x = x
			self.__my_objects[i].y = y	
			for obj in self.__objects_list:
				if x == obj.x and y == obj.y:
					cannot_rotate = True
			if x > 450 or y > 700:
				cannot_rotate = True
				
		if cannot_rotate:
			self.__shapes_index = self.__shapes_index - 1
			self.__my_shape = self.__general_shape[self.__shapes_index]
			for i in range(4):
				self.__my_objects[i].x = self.__x_coordinate + self.__my_shape[i + 1][0]
				self.__my_objects[i].y = self.__y_coordinate + self.__my_shape[i + 1][1]



class ShapesBase():
	
	def __init__(self):
		self.__shape1 = [[(200,  -50, 100), (0, 0), (50, 0), (0, 50), (50, 50)]]
		self.__shape2 = [[(200, -150, 50), (0, 0), (0, 50), (0, 100), (0, 150)], [(200, 0, 200), (0, 0), (50, 0), (100, 0), (150, 0)]]
		self.__shape3 = [[(200, -50, 150), (0, 0), (50, 0), (50, 50), (100, 50)], [(200, -100, 100), (50, 0), (0, 50), (50, 50), (0, 100)]]
		self.__shape4 = [[(200, -50, 150), (50, 0), (100, 0), (0, 50), (50, 50)], [(200, -100, 100), (0, 0), (0, 50), (50, 50), (50, 100)]]
		self.__shape5 = [[(200, -100, 100), (0, 0), (0, 50), (50, 50), (0, 100)], [(200, -50, 150), (0, 0), (50, 0), (100, 0), (50, 50)],
		[(200, -100, 100), (50, 0), (0, 50), (50, 50), (50, 100)], [(200, -50, 150), (50, 0), (0, 50), (50, 50), (100, 50)]]
		self.__shape6 = [[(200, -100, 100), (0, 0), (0, 50), (0, 100), (50, 100)], [(200, -50, 150), (0, 0), (50, 0), (100, 0), (0, 50)],
		[(200, -100, 100), (0, 0), (50, 0), (50, 50), (50, 100)], [(200, -50, 150), (100, 0), (0, 50), (50, 50), (100, 50)]]
		self.__shape7 = [[(200, -100, 100), (50, 0), (50, 50), (0, 100), (50, 100)], [(200, -50, 150), (0, 0), (0, 50), (50, 50), (100, 50)],
		[(200, -100, 100), (0, 0), (50, 0), (0, 50), (0, 100)], [(200, -50, 150), (0, 0), (50, 0), (100, 0), (100, 50)]] 
		self.__shapes = [self.__shape1, self.__shape2, self.__shape3, self.__shape4, self.__shape5, self.__shape6, self.__shape7]
		self.__colors = [(215,35,35), (255,179,26), (102,255,178), (76,153,0), (0,0,204), (153,0,76), (255,255,0)]
		
		
		
		self.__gen_shape = random.choice(self.__shapes)
		self.__shape = random.choice(self.__gen_shape)
		self.__color = random.choice(self.__colors)
		self.__gen_shape1 = random.choice(self.__shapes)
		self.__shape1 = random.choice(self.__gen_shape1)
		self.__color1 = random.choice(self.__colors)
		self.__gen_shape2 = random.choice(self.__shapes)
		self.__shape2 = random.choice(self.__gen_shape2)
		self.__color2 = random.choice(self.__colors)
		self.__gen_shape3 = random.choice(self.__shapes)
		self.__shape3 = random.choice(self.__gen_shape3)
		self.__color3 = random.choice(self.__colors)
		
	
	def Succeed(self):
		'''Generates new shape and changes succeeding shapes'  references'''
		
		self.__gen_shape = self.__gen_shape1
		self.__shape = self.__shape1
		self.__color = self.__color1
		self.__gen_shape1 = self.__gen_shape2
		self.__shape1 = random.choice(self.__gen_shape1)
		self.__color1 = self.__color2
		self.__gen_shape2 = self.__gen_shape3
		self.__shape2 = random.choice(self.__gen_shape2)
		self.__color2 = self.__color3
		self.__gen_shape3 = random.choice(self.__shapes)
		self.__shape3 = random.choice(self.__gen_shape3)
		self.__color3 = random.choice(self.__colors)
		
	
	def GetCurrentShape(self):
		'''Returns shape pattern and color of current falling shape'''
		
		return self.__gen_shape, self.__shape, self.__color
	
	
	def GetSucceedingShapes(self):
		'''Returns shape patterns and colors of succeeding shapes in a list'''
		
		return [(self.__shape1, self.__color1), (self.__shape2, self.__color2), (self.__shape3, self.__color3)]
		
					
				
class Rows():
	
	
	def __init__(self, row_num):
		self.__rows = [[] for n in range(row_num)] 
		self.__row_y_coordinates = [700 - n * 50 for n in range(row_num)]
			
			
	def AddToRows(self, objs):
		'''Adds objects to a proper row list'''
		
		for obj in objs:
			self.__rows[self.__row_y_coordinates.index(obj.y)].append(obj)	
			

	def RemoveRows(self, obj_lst):
		'''Removes full rows and orders objects located above the deleted rows to fall'''
		
		repeat = True
		while repeat:
			repeat = False
			for row in self.__rows:			
				if len(row) == 10:
					repeat = True
					for i in range(10):
						obj_lst.remove(row[0])
						del row[0]					
					for row2 in self.__rows[self.__rows.index(row):]:
						for obj in row2:
							obj.y = obj.y + 50
						self.AddToRows(row2)
						row2.clear()
						
		return obj_lst



class Manager():
	
	
	def __init__(self):
		self.__objects_list = []
		self.__Rows = Rows(15)
		self.__Shapes = ShapesBase()

		
	def NewShape(self):
		'''Creates new shape'''
		
		gen_shape, shape, color = self.__Shapes.GetCurrentShape()
		self.__shape = Shape(self.__objects_list, gen_shape, shape, color)		
		self.__objects_list = self.__shape()
		
			
	def Fall(self):
		'''The main method used by the client to order falling shapes to fall. The
		method also calls NewShape and RomoveRow methods when needed'''
		
		if len(self.__objects_list) == 0:
			self.NewShape()
			
		if self.__shape.CanFall():
			self.__shape.SFall()

		else:
			self.__Rows.AddToRows(self.__objects_list[-4:])
			self.__objects_list = self.__Rows.RemoveRows(self.__objects_list)
			self.__Shapes.Succeed()
			self.NewShape()
			
			
	def MoveRight(self):
		'''Allowes user to move to the right falling objects'''
		
		self.__shape.MoveRight()
			

	def MoveLeft(self):
		'''Allowes user to move to the left falling objects'''
		
		self.__shape.MoveLeft()
		
		
	def Rotate(self):
		'''Method used by client to rotate falling snape'''
		
		self.__shape.Rotate()
			

	def GetPositions(self):
		'''Client uses the method to get positions (x, y, colour) of all objects,
		except for succeeding objects (the method below)'''
		
		return [(obj.x, obj.y, obj.color) for obj in self.__objects_list]
		
		
	def GetSucceedingShapes(self, size, pos1, pos2, pos3):
		'''Client uses the method to get positions (x, y, colour) of succeeding shapes,
		that are going to be displayed on the right side of the window. Controller provides
		arguments: size, and positions (x, y) of the 3 shapes'''
		
		to_return = []
		positions = (pos1, pos2, pos3)
		succeeding_shapes = self.__Shapes.GetSucceedingShapes()
		for shape in succeeding_shapes:
			for i in range(1, 5):
				to_return.append((positions[succeeding_shapes.index(shape)][0] + shape[0][i][0]//50 * size, positions[succeeding_shapes.index(shape)][1] +  shape[0][i][1]//50 * size, shape[1]))					
		
		return to_return
