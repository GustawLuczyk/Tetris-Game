import pygame, view, time, random
from game_model import Manage
pygame.init()
view.window_generator()

surface = pygame.Surface((250, 750))
surface.fill((80,220,100))

if __name__ == "__main__":
	while True:
		t0 = time.time()
		Manage.Fall()
		
		t1 = time.time()
		while t1 - t0 < 1:
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
						Manage.FallFaster()
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
						b2 = view.button(view.window, (570, 150), "Continue")
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
			positions = Manage.GetPositions()						
			view.squares(0, positions, 50)
			view.squares((0,0,0), positions, 50, 2)
			view.line()
			pygame.display.flip()
			t1 = time.time()
		
		
