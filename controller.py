import pygame, view, time, random
from game_model import Manage
pygame.init()

pygame.mixer.init()
pygame.mixer.music.load("2019-11-17_-_Bold_Statement_-_David_Fesliyan.mp3")
pygame.mixer.music.set_volume(0.7)
pygame.mixer.music.play()

view.window_generator()
surface = pygame.Surface((250, 750))
surface.fill((80,220,100))
taudio = time.time()
if __name__ == "__main__":
	punkty = 0
	tim = 1
	while True:
		t0 = time.time()
		Manage.Fall()
		
		
		t1 = time.time()
		while t1 - t0 < tim:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
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
					elif event.key == pygame.K_a:
						variable = True
						while variable:
							for event in pygame.event.get():
								if event.type == pygame.QUIT:
									pygame.quit()
								if event.type == pygame.KEYDOWN:
									variable = False
				elif event.type == pygame.MOUSEBUTTONDOWN:
					if b1.collidepoint(pygame.mouse.get_pos()):
						variable = True
						b2 = view.button(view.window, (570, 150), "Kontynułuj")
						pygame.display.flip()
						while variable:
							for event in pygame.event.get():
								if event.type == pygame.QUIT:
									pygame.quit()
								if event.type == pygame.MOUSEBUTTONDOWN:
									if b2.collidepoint(pygame.mouse.get_pos()):
										variable = False
			
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
		punkty += 1
		if punkty == 15:
			tim = 0.8
		elif punkty == 24:
			tim = 0.6
		elif punkty == 36:
			tim = 0.5
		elif punkty == 48:
			tim = 0.4
		elif punkty == 60:
			tim = 0.3
		elif punkty == 100:
			tim = 0.2
