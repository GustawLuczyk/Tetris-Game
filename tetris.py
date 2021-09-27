import pygame, view, time, random
from pygame import event
from audioplayer import AudioPlayer
from game_model import Manage
from events import *
from pgevents import *
from timer import *
from keyevents import *

def init():
    pygame.init()
    surface = pygame.Surface((250, 750))
    surface.fill((80,220,100))
    view.window_generator()
   

def draw_board(model):
    surface = pygame.Surface((250, 750))
    surface.fill((80,220,100))
    view.window_generator()
    view.window.blit(surface, (500, 0))
    positions = model.GetPositions()
    view.squares(0, positions, 50)
    view.squares((0,0,0), positions, 50, 2)
    future_rectangles = model.GetSucceedingShapes(30, (600,330), (600, 480), (600,620))
    view.squares(0, future_rectangles, 30)
    view.line()
    pygame.display.flip()
    
def update_board(model, events):
    try:
        if events.event == TimerEvent.TinyTick:
            model.Fall()
            draw_board(model)
    except:
        pass
    
def run():
    model = Manage
    event_queue = EventsQueue()
    timer_processor = Timer()
    pygame_processor = PygameProcess()
    key_processor = KeyProcess()
    
    draw_board(model)
    
    quit = False
    while not quit:
        
        timer_processor.process(event_queue)
        pygame_processor.process(event_queue)
        key_processor.process(event_queue)
        update_board(model, event_queue)

        #try:
        if isinstance(event_queue.event, KeyEvent):
            if event_queue.event.key == KeyType.EXIT:
                quit = True
        #except:
        #    pass
   

if __name__ == "__main__":
    init()
    run()
