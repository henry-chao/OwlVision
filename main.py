from wx import App, STAY_ON_TOP
from app.OwlFrame import OwlFrame

if __name__ == '__main__':
    app = App()
    frm = OwlFrame()
    frm.Show()
    app.MainLoop()
