from wx import App
from OwlFrame import OwlFrame

if __name__ == '__main__':
    app = App()
    frm = OwlFrame(None, title="OwlVision")
    frm.Show()
    app.MainLoop()
