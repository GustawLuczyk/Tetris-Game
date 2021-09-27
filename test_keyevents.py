import pygame, view
from keyevents import *
import pytest

def test_key_creat():
    ev = KeyEvent()
    
    assert ev.key == KeyType.NONE
    assert ev.state == KeyState.NONE
    
  
def test_key_assign():
    
    kk = KeyEvent()
    kk.key = KeyType.LEFT
    kk.state = KeyState.UP
    
    assert kk.key == KeyType.LEFT
    assert kk.state == KeyState.UP
    
    with pytest.raises(AssertionError):
        kk.key = 2

    with pytest.raises(AssertionError):
        kk.state = 2


def test_key_process_create(capsys):
    
    kp = KeyProcess()
    print(kp._KeyProcess__keys)
    #assert capsys.readouterr().out == ""
    
    
def test_key_process_pygame():
    
    pygame.init()
    surface = pygame.Surface((250, 750))
    surface.fill((80,220,100))
    view.window_generator()
    pygame.display.flip()
    
    quit = False
    while not quit:
        for pgevent in pygame.event.get():
            if pgevent.type == pygame.QUIT:
                quit = True
     