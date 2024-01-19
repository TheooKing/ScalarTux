from .settings import GlobalSettings

def debug_print(*values: object, sep: str | None = " ", end: str | None = "\n", file: None = None, flush = False, tags:list = [])->None:
    """
    Print statement that gets called only when the debug of the application is equal to `True`.
    Basically the Print function, but only print when `GlobalSettings._debug == True`
    """
    if GlobalSettings._debug and DebugTags.debug_tags is not []:
        for i in tags:
            if i in DebugTags.debug_tags:
                print(*values, sep, end, file, flush)
    elif GlobalSettings._debug:
        print(*values, sep, end, file, flush)

class DebugTags:
    '''
    Stores an active dictionary that upon called it will try to match what the 
    programmer wants to debug and subsequently approve calls that come from that source.
    '''

    debug_tags = []

    @staticmethod
    def import_tags(tags:list) -> None:
        DebugTags.debug_tags += tags  

class ScreenDebug:
    """
    Shows debug information in the screen.
    """
    pass

