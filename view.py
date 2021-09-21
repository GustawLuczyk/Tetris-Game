import pygame
pygame.init()
#print(pygame.font.get_fonts())
(width, height) = (750, 750)
window = pygame.display.set_mode((width, height))

def window_generator():
	"""generates window canvas"""
	background_collor = (180, 200, 255)
	pygame.display.set_caption("Tetris :-)")
	window.fill(background_collor)
	
	
def circle(a, b, c, d):
	"""drawes circle"""
	pygame.draw.circle(window, a, b, c, d)
	
def squares(col, poz, size, thi = 0):
	'''drawes rectangles'''
	if col == 0:
		for rect in poz:
			pygame.draw.rect(window, rect[2], pygame.Rect(rect[0], rect[1], size, size), thi)
	else:
		for rect in poz:
			pygame.draw.rect(window, col, pygame.Rect(rect[0], rect[1], size, size), thi)
			
def line(color = (0, 0, 0), xy1= (501, 0), xy2 = (501, 750), thickness = 3):
	pygame.draw.line(window,color,xy1,xy2,thickness)


def button(window, position, text, height = 30):
	font = pygame.font.SysFont('arial', height)
	text_render = font.render(text, 1, (50, 50, 200))
	x, y, w, h = text_render.get_rect()
	x, y = position
	#pygame.draw.rect(window, (250, 30, 20), (x, y, w, h))
	return window.blit(text_render, (x, y))

def combo_button(window, position, text):
	for height in range(2, 100):
		font = pygame.font.SysFont('arial', height)
		text_render = font.render(text, 1, (50, 50, 200))
		x, y, w, h = text_render.get_rect()
		x, y = position
		return window.blit(text_render, (x, y))
		pygame.display.flip()

