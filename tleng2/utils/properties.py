# have every not setting related variable stored here
import pygame
from .settings import GlobalSettings
from abc import abstractmethod, ABC

class LocalProperties:
    @abstractmethod
    def __init__(self):
        """
        Put the local specific properties that you want the scene/enviroment/object to have
        e.x. (pseudo code)

        self.clock = 30
        self.window = comic_sans
        self.disp = True
        self.in-game-keyboard = False
        """    

class GlobalProperties:
    """
    Global properties, needed across the game.
    """
    
    # Temporary display variables
    __temp_disp = None
    
    _window = None # the window that you see
    _display = None # the inner display of the window
    _clock = pygame.time.Clock()

    # _index_event = 1

    # animation_database = {} # probably not to use

    @staticmethod
    def load_display( bg_color: tuple[int, int, int] = (200, 200, 255) ) -> None:
        """
        Initialize the display.
        """
        GlobalProperties._display = pygame.Surface(GlobalSettings._disp_res) 
        GlobalProperties._window = pygame.display.set_mode(GlobalSettings._win_res)
        GlobalProperties._display.fill(bg_color)

    @staticmethod
    def set_caption(caption: str) -> None:
        pygame.display.set_caption(caption)


    @staticmethod
    def lazy_upscale_display(new_res:tuple[int,int] = GlobalSettings._win_res):
        """
        Scaling the display to the size of the window.
        And updates the window with the upscale.
        Warning may be very pixelated.
        """
        GlobalProperties.__temp_disp = pygame.transform.scale(GlobalProperties._display, new_res)
        GlobalProperties._window.blit(GlobalProperties.__temp_disp, (0, 0))


    @staticmethod
    def update_window() -> None:
        """
        Updates the window from _display immedietely.
        """
        GlobalProperties._window.blit(GlobalProperties._display, (0, 0))


    @staticmethod
    def fill_display(color: tuple[int, int, int]):
        """
        Fill the display with color.
        """
        GlobalProperties._display.fill(color)