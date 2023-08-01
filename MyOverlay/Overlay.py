from MyLibrary.funcs import myfunctions

def InnitOverlay():
    return myfunctions.StartOverlay()
    
def settext(text: str, PosX: int, PosY: int):
    myfunctions.settext(text, PosX: int, PosY: int)
    
def KillOverlay():
    myfunctions.KillOverlay()
    
def StatusOverlay():
    return myfunctions.StatusOverlay
