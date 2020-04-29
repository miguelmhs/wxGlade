#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#
# generated by wxGlade
#

import wx

# begin wxGlade: dependencies
# end wxGlade

# begin wxGlade: extracode
import wx.html
# end wxGlade


class MyFrame(wx.Frame):
    def __init__(self, *args, **kwds):
        # begin wxGlade: MyFrame.__init__
        kwds["style"] = kwds.get("style", 0) | wx.DEFAULT_FRAME_STYLE
        wx.Frame.__init__(self, *args, **kwds)
        self.SetSize((400, 300))
        self.SetTitle("frame")
        
        # Menu Bar
        self.frame_menubar = wx.MenuBar()
        self.SetMenuBar(self.frame_menubar)
        # Menu Bar end
        
        self.frame_statusbar = self.CreateStatusBar(1)
        self.frame_statusbar.SetStatusWidths([-1])
        # statusbar fields
        frame_statusbar_fields = ["frame_statusbar"]
        for i in range(len(frame_statusbar_fields)):
            self.frame_statusbar.SetStatusText(frame_statusbar_fields[i], i)
        
        # Tool Bar
        self.frame_toolbar = wx.ToolBar(self, -1)
        self.SetToolBar(self.frame_toolbar)
        self.frame_toolbar.Realize()
        # Tool Bar end
        
        self.panel_x = wx.Panel(self, wx.ID_ANY)
        
        sizer_1 = wx.BoxSizer(wx.VERTICAL)
        
        self.notebook_1 = wx.Notebook(self.panel_x, wx.ID_ANY)
        sizer_1.Add(self.notebook_1, 1, wx.EXPAND, 0)
        
        self.notebook_1_pane_1 = wx.Panel(self.notebook_1, wx.ID_ANY)
        self.notebook_1.AddPage(self.notebook_1_pane_1, "notebook_1_pane_1")
        
        sizer_1.Add((20, 20), 0, 0, 0)
        
        self.window_1 = wx.SplitterWindow(self.panel_x, wx.ID_ANY)
        self.window_1.SetMinimumPaneSize(20)
        sizer_1.Add(self.window_1, 1, wx.EXPAND, 0)
        
        self.window_1_pane_1 = wx.Panel(self.window_1, wx.ID_ANY)
        
        self.window_1_pane_2_scrolled = wx.ScrolledWindow(self.window_1, wx.ID_ANY, style=wx.TAB_TRAVERSAL)
        self.window_1_pane_2_scrolled.SetScrollRate(10, 10)
        
        self.html = wx.html.HtmlWindow(self.panel_x, wx.ID_ANY)
        sizer_1.Add(self.html, 1, wx.ALL | wx.EXPAND, 3)
        
        self.window_1.SplitVertically(self.window_1_pane_1, self.window_1_pane_2_scrolled)
        
        self.panel_x.SetSizer(sizer_1)
        
        self.Layout()
        # end wxGlade

# end of class MyFrame

class NotebookPageWithBases(NotebookPage, notebookpage.NotebookPage):
    def __init__(self, *args, **kwds):
        # begin wxGlade: NotebookPageWithBases.__init__
        kwds["style"] = kwds.get("style", 0) | wx.TAB_TRAVERSAL
        NotebookPage.__init__(self, *args, **kwds)
        notebookpage.NotebookPage.__init__(self)
        self.Layout()
        # end wxGlade

# end of class NotebookPageWithBases

class TestNotebookWithBasesInFrame(TestNotebook, testnotebook.TestNotebook):
    def __init__(self, *args, **kwds):
        # begin wxGlade: TestNotebookWithBasesInFrame.__init__
        kwds["style"] = kwds.get("style", 0) | wx.NB_TOP
        TestNotebook.__init__(self, *args, **kwds)
        testnotebook.TestNotebook.__init__(self)
        
        self.notebook_1_pane_1 = NotebookPageWithBases(self, wx.ID_ANY)
        self.AddPage(self.notebook_1_pane_1, "notebook_1_pane_1")
        # end wxGlade

# end of class TestNotebookWithBasesInFrame

class SplitterWindowWithBasesInFrame(TestSplitterWindow):
    def __init__(self, *args, **kwds):
        # begin wxGlade: SplitterWindowWithBasesInFrame.__init__
        kwds["style"] = kwds.get("style", 0) | wx.SP_3D
        TestSplitterWindow.__init__(self, *args, **kwds)
        
        self.window_1_pane_1 = wx.Panel(self, wx.ID_ANY)
        
        self.window_1_pane_2 = wx.Panel(self, wx.ID_ANY)
        self.SplitVertically(self.window_1_pane_1, self.window_1_pane_2)
        # end wxGlade

# end of class SplitterWindowWithBasesInFrame

class TestPanelWithBasesInFrame(TestPanel, testpanel.TestPanel):
    def __init__(self, *args, **kwds):
        # begin wxGlade: TestPanelWithBasesInFrame.__init__
        kwds["style"] = kwds.get("style", 0)
        TestPanel.__init__(self, *args, **kwds)
        testpanel.TestPanel.__init__(self)
        
        sizer_1 = wx.BoxSizer(wx.VERTICAL)
        
        self.notebook_1 = TestNotebookWithBasesInFrame(self, wx.ID_ANY)
        sizer_1.Add(self.notebook_1, 1, wx.EXPAND, 0)
        
        self.window_1 = SplitterWindowWithBasesInFrame(self, wx.ID_ANY)
        sizer_1.Add(self.window_1, 1, wx.EXPAND, 0)
        
        self.html = wx.html.HtmlWindow(self, wx.ID_ANY)
        sizer_1.Add(self.html, 1, wx.ALL | wx.EXPAND, 3)
        
        self.SetSizer(sizer_1)
        
        self.Layout()
        # end wxGlade

# end of class TestPanelWithBasesInFrame

class MyFrameWithBases(TestFrame, testframe.TestFrame):
    def __init__(self, *args, **kwds):
        # begin wxGlade: MyFrameWithBases.__init__
        kwds["style"] = kwds.get("style", 0) | wx.DEFAULT_FRAME_STYLE
        TestFrame.__init__(self, *args, **kwds)
        testframe.TestFrame.__init__(self)
        self.SetSize((400, 300))
        self.SetTitle("frame")
        
        # Menu Bar
        self.frame_copy_menubar = wx.MenuBar()
        self.SetMenuBar(self.frame_copy_menubar)
        # Menu Bar end
        
        self.frame_copy_statusbar = self.CreateStatusBar(1)
        self.frame_copy_statusbar.SetStatusWidths([-1])
        # statusbar fields
        frame_copy_statusbar_fields = ["frame_copy_statusbar"]
        for i in range(len(frame_copy_statusbar_fields)):
            self.frame_copy_statusbar.SetStatusText(frame_copy_statusbar_fields[i], i)
        
        # Tool Bar
        self.frame_copy_toolbar = wx.ToolBar(self, -1)
        self.SetToolBar(self.frame_copy_toolbar)
        self.frame_copy_toolbar.Realize()
        # Tool Bar end
        
        self.panel_1 = TestPanelWithBasesInFrame(self, wx.ID_ANY)
        self.Layout()
        # end wxGlade

# end of class MyFrameWithBases

class MyDialog(wx.Dialog):
    def __init__(self, *args, **kwds):
        # begin wxGlade: MyDialog.__init__
        kwds["style"] = kwds.get("style", 0) | wx.DEFAULT_DIALOG_STYLE
        wx.Dialog.__init__(self, *args, **kwds)
        self.SetTitle("dialog")
        
        sizer_1 = wx.BoxSizer(wx.VERTICAL)
        
        sizer_1.Add((0, 0), 0, 0, 0)
        
        self.SetSizer(sizer_1)
        sizer_1.Fit(self)
        
        self.Layout()
        # end wxGlade

# end of class MyDialog

class MyPanel(wx.Panel):
    def __init__(self, *args, **kwds):
        # begin wxGlade: MyPanel.__init__
        kwds["style"] = kwds.get("style", 0) | wx.TAB_TRAVERSAL
        wx.Panel.__init__(self, *args, **kwds)
        
        sizer_1 = wx.BoxSizer(wx.VERTICAL)
        
        sizer_1.Add((0, 0), 0, 0, 0)
        
        self.SetSizer(sizer_1)
        sizer_1.Fit(self)
        
        self.Layout()
        # end wxGlade

# end of class MyPanel

class MyMDIChildFrame(wx.MDIChildFrame):
    def __init__(self, *args, **kwds):
        # begin wxGlade: MyMDIChildFrame.__init__
        kwds["style"] = kwds.get("style", 0) | wx.DEFAULT_FRAME_STYLE
        wx.MDIChildFrame.__init__(self, *args, **kwds)
        self.SetSize((400, 300))
        self.SetTitle("frame_1")
        
        sizer_1 = wx.BoxSizer(wx.VERTICAL)
        
        sizer_1.Add((0, 0), 0, 0, 0)
        
        self.SetSizer(sizer_1)
        
        self.Layout()
        # end wxGlade

# end of class MyMDIChildFrame

class MyMenuBar(wx.MenuBar):
    def __init__(self, *args, **kwds):
        # begin wxGlade: MyMenuBar.__init__
        wx.MenuBar.__init__(self, *args, **kwds)
        # end wxGlade

# end of class MyMenuBar

class wxToolBar(wx.ToolBar):
    def __init__(self, *args, **kwds):
        # begin wxGlade: wxToolBar.__init__
        kwds["style"] = kwds.get("style", 0)
        wx.ToolBar.__init__(self, *args, **kwds)
        self.Realize()
        # end wxGlade

# end of class wxToolBar

class MyDialogWithBases(MyDialogBase, mydialogbases.MyDialogBase):
    def __init__(self, *args, **kwds):
        # begin wxGlade: MyDialogWithBases.__init__
        kwds["style"] = kwds.get("style", 0) | wx.DEFAULT_DIALOG_STYLE
        MyDialogBase.__init__(self, *args, **kwds)
        mydialogbases.MyDialogBase.__init__(self)
        self.SetTitle("dialog")
        
        sizer_1 = wx.BoxSizer(wx.VERTICAL)
        
        sizer_1.Add((0, 0), 0, 0, 0)
        
        self.SetSizer(sizer_1)
        sizer_1.Fit(self)
        
        self.Layout()
        # end wxGlade

# end of class MyDialogWithBases

class MyPanelWithBases(MyPanelBase, mypanelbases.MyPanelBase):
    def __init__(self, *args, **kwds):
        # begin wxGlade: MyPanelWithBases.__init__
        kwds["style"] = kwds.get("style", 0) | wx.TAB_TRAVERSAL
        MyPanelBase.__init__(self, *args, **kwds)
        mypanelbases.MyPanelBase.__init__(self)
        
        sizer_1 = wx.BoxSizer(wx.VERTICAL)
        
        sizer_1.Add((0, 0), 0, 0, 0)
        
        self.SetSizer(sizer_1)
        sizer_1.Fit(self)
        
        self.Layout()
        # end wxGlade

# end of class MyPanelWithBases

class MyPanelScrolled(wx.ScrolledWindow):
    def __init__(self, *args, **kwds):
        # begin wxGlade: MyPanelScrolled.__init__
        kwds["style"] = kwds.get("style", 0) | wx.TAB_TRAVERSAL
        wx.ScrolledWindow.__init__(self, *args, **kwds)
        self.SetScrollRate(10, 10)
        
        sizer_1 = wx.BoxSizer(wx.VERTICAL)
        
        sizer_1.Add((0, 0), 0, 0, 0)
        
        self.SetSizer(sizer_1)
        sizer_1.Fit(self)
        
        self.Layout()
        # end wxGlade

# end of class MyPanelScrolled

class MyApp(wx.App):
    def OnInit(self):
        self.frame = MyFrame(None, wx.ID_ANY, "")
        self.SetTopWindow(self.frame)
        self.frame.Show()
        return True

# end of class MyApp

if __name__ == "__main__":
    app = MyApp(0)
    app.MainLoop()
