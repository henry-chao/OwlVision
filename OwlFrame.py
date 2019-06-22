from wx import Frame, Menu, MenuBar, ID_EXIT, EVT_MENU


class OwlFrame(Frame):

    def __init(self, *args, **kw):
        super(OwlFrame, self).__init__(*args, **kw)

        self.makeMenuBar()
        self.CreateStatusBar()
        self.SetStatusText("OwlFrame")

    def makeMenuBar(self):
        fileMenu = Menu()
        exitItem = fileMenu.append(ID_EXIT)

        menuBar = MenuBar()
        menuBar.Append(fileMenu, "&File")

        self.SetMenuBar(menuBar)
        self.Bind(EVT_MENU, self.OnExit, exitItem)

    def OnExit(self, event):
        self.Close(True)
