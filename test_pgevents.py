import pygame, view
from keyevents import *
from pgevents import *
import pytest

def test_pygame_process(capsys):
    
    pygame.init()
    surface = pygame.Surface((250, 750))
    surface.fill((80,220,100))
    view.window_generator()
    pygame.display.flip()
    
    pgprocess = PygameProcess()
    events = EventsQueue()
    
    quit = False
    while not quit:
        pgprocess.process(events)
        if isinstance(events.event, PygameEvent):
            if events.event.pgevent.type == pygame.QUIT:
                quit = True
            events.remove()
            #print(events.event.pgevent, quit, events._EventsQueue__queue)
            #assert capsys.readouterr().out == ""
