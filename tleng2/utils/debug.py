from .settings import GlobalSettings

def debug_print(*values: object, sep: str | None = " ", end: str | None = "\n", file: None = None, flush = False)->None:
    """
    Print statement that gets called only when the debug of the application is equal to `True`.

    Basically the Print function, but only print when `GlobalSettings._debug == True`
    """
    if GlobalSettings._debug:
        print(*values, sep, end, file, flush)
    else:
        pass

class DebugPrint:
    '''
    Stores an active dictionary that upon called it will try to match what the 
    programmer wants to debug and subsequently approve calls that come from that source.
    '''
    @staticmethod
    def debug_print(*values: object, sep: str | None = " ", end: str | None = "\n", file: None = None, flush = False)->None:
       """
       Print statement that gets called only when the debug of the application is equal to `True`.

       Basically the Print function, but only print when `GlobalSettings._debug == True`
       """
       if GlobalSettings._debug:
           print(*values, sep, end, file, flush)  

class ScreenDebug:
    """
    Shows debug information in the screen.
    """
    pass

