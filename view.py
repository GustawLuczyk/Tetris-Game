import pygame
pygame.init()
print(pygame.font.get_fonts())
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
	
def squares(color, poz, size, thi = 0):
	'''drawes rectangles'''
	for rect in poz:
		pygame.draw.rect(window, color, pygame.Rect(rect[0], rect[1], size, size), thi)

def line(color = (0, 0, 0), xy1= (501, 0), xy2 = (501, 750), thickness = 3):
	pygame.draw.line(window,color,xy1,xy2,thickness)


def button(window, position, text):
	font = pygame.font.SysFont('arial', 30)
	text_render = font.render(text, 1, (50, 50, 200))
	x, y, w, h = text_render.get_rect()
	x, y = position
	pygame.draw.rect(window, (250, 30, 20), (x, y, w, h))
	return window.blit(text_render, (x, y))
	

if __name__ == "__main__":
	b1 = button(window, (600, 100), "Quit")
	while True:
		for event in pygame.event.get():
			if (event.type == pygame.QUIT):
				pygame.quit()
			if event.type == pygame.MOUSEBUTTONDOWN:
				if b1.collidepoint(pygame.mouse.get_pos()):
					pygame.quit()
		pygame.display.flip()
'''
def button(window, position, text):
    font = pygame.font.SysFont('arial', 50)
    text_render = font.render(text, 1, (255, 0, 0))
    x, y, w , h = text_render.get_rect()
    x, y = position
    pygame.draw.line(window, (150, 150, 150), (x, y), (x + w , y), 5)
    pygame.draw.line(window, (150, 150, 150), (x, y - 2), (x, y + h), 5)
    pygame.draw.line(window, (50, 50, 50), (x, y + h), (x + w , y + h), 5)
    pygame.draw.line(window, (50, 50, 50), (x + w , y+h), [x + w , y], 5)
    pygame.draw.rect(window, (100, 100, 100), (x, y, w , h))
    return window.blit(text_render, (x, y))
 
def start():
    print("Ok, let's go")
 
def menu():
    """ This is the menu that waits you to click the s key to start """
    b1 = button(window, (400, 300), "Quit")
    b2 = button(window, (500, 300), "Start")
    while True:
        for event in pygame.event.get():
            if (event.type == pygame.QUIT):
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                key_to_start = event.key == pygame.K_s or event.key == pygame.K_RIGHT or event.key == pygame.K_UP
                if key_to_start:
                    start()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if b1.collidepoint(pygame.mouse.get_pos()):
                    pygame.quit()
                elif b2.collidepoint(pygame.mouse.get_pos()):
                    start()
        pygame.display.update()
    pygame.quit()
 
menu()
'''

