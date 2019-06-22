from wx import App, STAY_ON_TOP
from app.OwlFrame import OwlFrame

if __name__ == '__main__':
    app = App()
    frm = OwlFrame(None, title="OwlVision", style=STAY_ON_TOP)
    frm.Show()
    app.MainLoop()
