mport random


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

   	__shape1 = [[(200,  -50, 100), (0, 0), (50, 0), (0, 50), (50, 50)]]
	__shape2 = [[(200, -150, 50), (0, 0), (0, 50), (0, 100), (0, 150)], [(200, 0, 200), (0, 0), (50, 0), (100, 0), (150, 0)]]	
	__shape3 = [[(200, -50, 150), (0, 0), (50, 0), (50, 50), (100, 50)], [(200, -100, 100), (50, 0), (0, 50), (50, 50), (0, 100)]]
	__shape4 = [[(200, -50, 150), (50, 0), (100, 0), (0, 50), (50, 50)], [(200, -100, 100), (0, 0), (0, 50), (50, 50), (50, 100)]]
	__shape5 = [[(200, -100, 100), (0, 0), (0, 50), (50, 50), (0, 100)], [(200, -50, 150), (0, 0), (50, 0), (100, 0), (50, 50)],
	[(200, -100, 100), (50, 0), (0, 50), (50, 50), (50, 100)], [(200, -50, 150), (50, 0), (0, 50), (50, 50), (100, 50)]]
	__shape6 = [[(200, -100, 100), (0, 0), (0, 50), (0, 100), (50, 100)], [(200, -50, 150), (0, 0), (50, 0), (100, 0), (0, 50)],
	[(200, -100, 100), (0, 0), (50, 0), (50, 50), (50, 100)], [(200, -50, 150), (100, 0), (0, 50), (50, 50), (100, 50)]]
	__shape7 = [[(200, -100, 100), (50, 0), (50, 50), (0, 100), (50, 100)], [(200, -50, 150), (0, 0), (0, 50), (50, 50), (100, 50)],
	[(200, -100, 100), (0, 0), (50, 0), (0, 50), (0, 100)], [(200, -50, 150), (0, 0), (50, 0), (100, 0), (100, 50)]] 
	__shapes = [shape1, shape2, shape3, shape4, shape5, shape6, shape7]
	general_shape_1 = random.choice(shapes)
	shape_1 = random.choice(general_shape_1)
	general_shape_2 = random.choice(shapes)
	shape_2 = random.choice(general_shape_2)
	general_shape_3 = random.choice(shapes)
	shape_3 = random.choice(general_shape_3)
	succeeding_shapes = (shape_1, shape_2, shape_3)



    def __init__(self, lst):
        self.__objects_list = lst
        self.__falling_objects = []
        self.__general_shape = random.choice(__shapes)
        self.__current_shape = random.choice(self.__general_shape)

        self.__x_coordinate = self.__current_shape[0][0]
        self.__y_coordinate = self.__current_shape[0][1]

        for i in range(1, 5):
            self.__falling_objects.append(Brick(self.__current_shape[i][0], self.__current_shape[i][1], 0)

    def CanFall(self):
		'''Checks falling shape's possibility to fall'''
		
		for obj in self.__objects_list:
			for fall_obj in self.__falling_objects:
				if obj.x == fall_obj.x and obj.y == fall_obj.y + 50:
                    return False			
		for obj in self.falling_objects:			
			if obj.y == 700:
				return False
				
		return True
    
    def SFall(self):
        for obj in self.__falling_objects:
			obj.y = obj.y + 50
		self.__y_coordinate = self.__y_coordinate + 50        

class Manager():
	
	
	def __init__(self):
        self.__objects_list = []
		
			
	def Fall(self):
		'''The main method used by controller to order falling shapes to fall. The
		method also calls NewShape and RomoveRow methods when needed'''
		
		if len(self.falling_objects) == 0:
			self.shape = Shape(self.__objects_list)
			
		if self.shape.CanFall():
            self.shape.SFall()

		else:
			for obj in self.falling_objects:
				self.AddToRow(obj)
			if len(self.falling_objects) != 0:
				for i in range(4):
					obj = self.falling_objects.pop()
					self.objects_list.append(obj)
			self.RemoveRow()
			self.NewShape()
			
			
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
