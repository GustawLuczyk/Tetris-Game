import random


class Brick():			
	def __init__(self, x, y, colour):
		self.x = x
		self.y = y
		self.colour = colour
		
	def Falling(self):
		self.y = self.y + 50
	
	def MoveLeft(self):
		self.x = self.x - 50
		
	def MoveRight(self):
		self.x = self.x + 50
		
	def __del__(self):
		pass
		
		

class Manager():
	
	
	def __init__(self):
		self.objects_list = []
		self.falling_objects = []
		self.shape1 = [[(200,  -50, 100), (0, 0), (50, 0), (0, 50), (50, 50)]]
		self.shape2 = [[(200, -150, 50), (0, 0), (0, 50), (0, 100), (0, 150)], [(200, 0, 200), (0, 0), (50, 0), (100, 0), (150, 0)]]	
		self.shape3 = [[(200, -50, 150), (0, 0), (50, 0), (50, 50), (100, 50)], [(200, -100, 100), (50, 0), (0, 50), (50, 50), (0, 100)]]
		self.shape4 = [[(200, -50, 150), (50, 0), (100, 0), (0, 50), (50, 50)], [(200, -100, 100), (0, 0), (0, 50), (50, 50), (50, 100)]]
		self.shape5 = [[(200, -100, 100), (0, 0), (0, 50), (50, 50), (0, 100)], [(200, -50, 150), (0, 0), (50, 0), (100, 0), (50, 50)],
		[(200, -100, 100), (50, 0), (0, 50), (50, 50), (50, 100)], [(200, -50, 150), (50, 0), (0, 50), (50, 50), (100, 50)]]
		self.shape6 = [[(200, -100, 100), (0, 0), (0, 50), (0, 100), (50, 100)], [(200, -50, 150), (0, 0), (50, 0), (100, 0), (0, 50)],
		[(200, -100, 100), (0, 0), (50, 0), (50, 50), (50, 100)], [(200, -50, 150), (100, 0), (0, 50), (50, 50), (100, 50)]]
		self.shape7 = [[(200, -100, 100), (50, 0), (50, 50), (0, 100), (50, 100)], [(200, -50, 150), (0, 0), (0, 50), (50, 50), (100, 50)],
		[(200, -100, 100), (0, 0), (50, 0), (0, 50), (0, 100)], [(200, -50, 150), (0, 0), (50, 0), (100, 0), (100, 50)]] 
		self.shapes = [self.shape1, self.shape2, self.shape3, self.shape4, self.shape5, self.shape6, self.shape7]
		self.general_shape_1 = random.choice(self.shapes)
		self.shape_1 = random.choice(self.general_shape_1)
		self.general_shape_2 = random.choice(self.shapes)
		self.shape_2 = random.choice(self.general_shape_2)
		self.general_shape_3 = random.choice(self.shapes)
		self.shape_3 = random.choice(self.general_shape_3)
		self.succeeding_shapes = (self.shape_1, self.shape_2, self.shape_3)
		
		self.colours = [(215,35,35), (255,179,26), (102,255,178), (76,153,0), (0,0,204), (153,0,76), (255,255,0)]
		self.last_colour = (255,255,0)
		
		self.reference_coordinate_x = 0
		self.reference_coordinate_y = 0

		self.rows = [[] for n in range(15)] 
		self.row_y_coordinates = (700, 650, 600, 550, 500, 450, 400, 350, 300, 250, 200, 150, 100, 50, 0)
		
	
	def NewShape(self):
		'''Creates new shape every time shape stops falling. The method
		is called by Fall method'''
		
		self.current_shape = self.shape_1
		self.general_shape = self.general_shape_1		
		self.shapes_index = self.general_shape.index(self.current_shape)
		self.shape_1 = self.shape_2
		self.general_shape_1 = self.general_shape_2
		self.shape_2 = self.shape_3
		self.general_shape_2 = self.general_shape_3
		self.general_shape_3 = random.choice(self.shapes) 
		self.shape_3 = random.choice(self.general_shape_3)
		self.succeeding_shapes = (self.shape_1, self.shape_2, self.shape_3)
		
		self.colours.remove(self.last_colour)
		self.colour = random.choice(self.colours)
		self.colours.append(self.last_colour)
		self.last_colour = self.colour
				
		for i in range(1, 5):
			self.reference_coordinate_x = self.current_shape[0][0]
			self.reference_coordinate_y = self.current_shape[0][1]
			self.x = self.reference_coordinate_x + self.current_shape[i][0]
			self.y = self.reference_coordinate_y + self.current_shape[i][1]
			self.falling_objects.append(Brick(self.x, self.y, self.colour))
			
			
	def AddToRow(self, obj):
		'''Adds an object to a proper row list'''
		self.rows[self.row_y_coordinates.index(obj.y)].append(obj)	
			

	def RemoveRow(self):
		'''removes full rows and orders objects located above the deleted rows to fall.
		The method is called by Fall method'''
		
		repeat = True
		while repeat:
			repeat = False
			for row in self.rows:			
				if len(row) == 10:
					repeat = True
					for i in range(10):
						self.objects_list.remove(row[0])
						del row[0]					
					for row2 in self.rows[self.rows.index(row):]:
						for obj in row2:
							obj.y = obj.y + 50
							self.AddToRow(obj)
						row2.clear()
						
											
	def ShouldFall(self):
		'''Checks falling shape's possibility to fall'''
		
		for obj in self.objects_list:
			for fall_obj in self.falling_objects:
				if obj.x == fall_obj.x and obj.y == fall_obj.y + 50:
					return False			
		for obj in self.falling_objects:			
			if obj.y == 700:
				return False
				
		return True
		
			
	def Fall(self):
		'''The main method used by controller to order falling shapes to fall. The
		method also calls NewShape and RomoveRow methods when needed'''
		
		if len(self.falling_objects) == 0:
			self.NewShape()
			
		if self.ShouldFall():
			for obj in self.falling_objects:
				obj.Falling()
			self.reference_coordinate_y = self.reference_coordinate_y + 50
		else:
			for obj in self.falling_objects:
				self.AddToRow(obj)
			if len(self.falling_objects) != 0:
				for i in range(4):
					obj = self.falling_objects.pop()
					self.objects_list.append(obj)
			self.RemoveRow()
			self.NewShape()
			
	
	def FallFaster(self):
		'''Allowes user to speed up falling of falling shapes after 
		checking the possibility to fall'''
		
		if self.ShouldFall():
			for obj in self.falling_objects:
				obj.Falling()
			self.reference_coordinate_y = self.reference_coordinate_y + 50
			
	
	def CanMoveRight(self):
		'''Called by the method MoveRight checks if the position 
		of falling shape allowes it to move to the right'''
		
		for obj in self.objects_list:
			for fall_obj in self.falling_objects:
				if obj.x == fall_obj.x + 50 and obj.y == fall_obj.y:
						return False														
		if self.reference_coordinate_x + self.current_shape[0][2] < 500:
			return True
			

	def CanMoveLeft(self):
		'''Called by the method MoveLeft checks if the position 
		of falling shape allowes it to move to the left'''
		
		for obj in self.objects_list:
			for fall_obj in self.falling_objects:
				if obj.x == fall_obj.x - 50 and obj.y == fall_obj.y:
					return False							
		if self.reference_coordinate_x > 0:
			return True
			
			
	def MoveRight(self):
		'''Allowes user to move to the right falling objects'''
		
		if self.CanMoveRight():
			for obj in self.falling_objects:
				obj.MoveRight()
			self.reference_coordinate_x = self.reference_coordinate_x + 50
			

	def MoveLeft(self):
		'''Allowes user to move to the left falling objects'''
		
		if self.CanMoveLeft():
			for obj in self.falling_objects:
				obj.MoveLeft()
			self.reference_coordinate_x = self.reference_coordinate_x - 50
			

	def Rotate(self):
		'''Rotates falling shapes only if shape's position allowes to do so'''
		
		if self.general_shape[self.shapes_index] != self.general_shape[-1]:
			self.shapes_index = self.shapes_index + 1
			self.current_shape = self.general_shape[self.shapes_index]
		else:
			self.shapes_index = 0
			self.current_shape = self.general_shape[self.shapes_index]
			
		self.cannot_rotate = False
		for i in range(4):
			self.x = self.reference_coordinate_x + self.current_shape[i + 1][0]
			self.y = self.reference_coordinate_y + self.current_shape[i + 1][1]			
			self.falling_objects[i].x = self.x
			self.falling_objects[i].y = self.y	
			for obj in self.objects_list:
				if self.x == obj.x and self.y == obj.y:
					self.cannot_rotate = True
			if self.x > 450 or self.y > 700:
				self.cannot_rotate = True
				
		if self.cannot_rotate:
			self.shapes_index = self.shapes_index - 1
			self.current_shape = self.general_shape[self.shapes_index]
			for i in range(4):
				self.x = self.reference_coordinate_x + self.current_shape[i + 1][0]
				self.y = self.reference_coordinate_y + self.current_shape[i + 1][1]
				self.falling_objects[i].x = self.x
				self.falling_objects[i].y = self.y	
							

	def GetPositions(self):
		'''Controller uses the method to get positions (x, y, colour) of all objects,
		except for succeeding objects (the method below)'''
		
		return [(obj.x, obj.y, obj.colour) for obj in self.objects_list + self.falling_objects]
		
		
	def GetSucceedingShapes(self, size, position1, position2, position3):
		'''Controller uses the method to get positions (x, y, colour) of succeeding shapes,
		that are going to be displayed on the right side of the window. Controller provides
		arguments: size, and positions (x, y) of the 3 shapes'''
		
		self.to_return = []
		self.positions = (position1, position2, position3)
		for shape in self.succeeding_shapes:
			for i in range(1, 5):
				self.to_return.append((self.positions[self.succeeding_shapes.index(shape)][0] + shape[i][0]//50 * size, self.positions[self.succeeding_shapes.index(shape)][1] +  shape[i][1]//50 * size, 0))					
		return self.to_return

Manage = Manager() #This object is to be imported

