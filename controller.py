import pygame, view, time, random

from game_model import Manage
pygame.init()

pygame.mixer.init()
pygame.mixer.music.load("2019-11-17_-_Bold_Statement_-_David_Fesliyan.mp3")
pygame.mixer.music.set_volume(0.7)



surface = pygame.Surface((250, 750))
surface.fill((80,220,100))
taudio = time.time()
if __name__ == "__main__":
	view.window_generator()
	pygame.mixer.music.play()
	punkty = 0
	tim = 1
	startbutton0 = view.button(view.window, (10, 10), "Wybierz poziom trudności")
	startbutton1 = view.button(view.window, (10, 50), "Poziom 1")
	startbutton2 = view.button(view.window, (10, 100), "Poziom 2 ")
	startbutton3 = view.button(view.window, (10, 150), "Poziom 3 ")
	startbutton4 = view.button(view.window, (10, 200), "Poziom 4 ")
	startbutton5 = view.button(view.window, (10, 250), "Poziom 5 ")
	startbutton6 = view.button(view.window, (10, 300), "Poziom 6 ")
	pygame.display.flip()
	should_continue = True
	while should_continue:
		for event in pygame.event.get():
			if event.type == pygame.MOUSEBUTTONDOWN:
				if startbutton1.collidepoint(pygame.mouse.get_pos()):
					should_continue = False
					level = 1
				if startbutton2.collidepoint(pygame.mouse.get_pos()):
					should_continue = False
					level = 2
				if startbutton3.collidepoint(pygame.mouse.get_pos()):
					should_continue = False
					level = 3
				elif startbutton4.collidepoint(pygame.mouse.get_pos()):
					should_continue = False	
					level = 4
				elif startbutton5.collidepoint(pygame.mouse.get_pos()):
					should_continue = False	
					level = 5
				elif startbutton6.collidepoint(pygame.mouse.get_pos()):
					should_continue = False	
					level = 6
			elif event.type == pygame.QUIT:
				pygame.quit()
				exit(0)
	while True:
		'''for height in range(2, 100, 2):
			view.window_generator()
			view.window.blit(surface, (500, 0))
			b1 = view.button(view.window, (600, 100), "Stop")
			b_punkty = view.button(view.window, (520, 400), "Zdobyte punkty: " + str(punkty), 23)							
			positions = Manage.GetPositions()						
			view.squares(0, positions, 50)
			view.squares((0,0,0), positions, 50, 2)
			view.line()
			bonus = view.button(view.window, (50, 200), "Combo 2", height)
			pygame.display.flip()
		t1 = time.time()
		t2 = time.time()'''
		while t2 - t1 < 1:
			t2 = time.time()
		Manage.Fall()
		t0 = time.time()
		t1 = time.time()
		while t1 - t0 < tim:
			view.window_generator()
			view.window.blit(surface, (500, 0))
			b1 = view.button(view.window, (600, 100), "Stop")
			b_punkty = view.button(view.window, (520, 400), "Zdobyte punkty: " + str(punkty), 23)							
			positions = Manage.GetPositions()						
			view.squares(0, positions, 50)
			view.squares((0,0,0), positions, 50, 2)
			view.line()
			pygame.display.flip()
			t1 = time.time()
			taudio1 = time.time()
			if int(taudio1 - taudio) % 26 == 0:
				pygame.mixer.music.play()
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					exit(0)
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_RIGHT:
						Manage.MoveRight()
					elif event.key == pygame.K_LEFT:
						Manage.MoveLeft()
					elif event.key == pygame.K_UP:
						Manage.Rotate()
					elif event.key == pygame.K_DOWN:
						go_down = True
						while go_down:
							positionsA = positions
							t0 = time.time()
							Manage.FallFaster()
							view.window_generator()
							view.window.blit(surface, (500, 0))
							b1 = view.button(view.window, (600, 100), "Stop")
							b_punkty = view.button(view.window, (520, 400), "Zdobyte punkty: " + str(punkty), 23)							
							positions = Manage.GetPositions()						
							view.squares(0, positions, 50)
							view.squares((0,0,0), positions, 50, 2)
							view.line()
							pygame.display.flip()		
							while t1 - t0 < 0.1:
								t1 =time.time()
							for event in pygame.event.get():
								if event.type == pygame.KEYUP:
									if event.key == pygame.K_DOWN:
										go_down = False
							if positionsA == positions:
								go_down = False
								
					elif event.key == pygame.K_x:
						pygame.quit()
						exit(0)
				elif event.type == pygame.MOUSEBUTTONDOWN:
					if b1.collidepoint(pygame.mouse.get_pos()):
						variable = True
						b2 = view.button(view.window, (570, 150), "Kontynułuj")
						pygame.display.flip()
						while variable:
							for event in pygame.event.get():
								if event.type == pygame.QUIT:
									pygame.quit()
									exit(0)
								if event.type == pygame.MOUSEBUTTONDOWN:
									if b2.collidepoint(pygame.mouse.get_pos()):
										variable = False
			
			
		punkty += 1
		if level == 2:
			tim = 0.8
		elif level == 3:
			tim = 0.6
		elif level == 4:
			tim = 0.5
		elif level == 5:
			tim = 0.4
		elif level == 6:
			tim = 0.3
		
