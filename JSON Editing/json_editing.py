"""
Created by: Meto Trajkovski
Email: metot@hotmail.com
"""

import wx  
import json


class Mywin(wx.Frame):

    def __init__(self, parent, title, size):
        """Create the GUI
        """
        super(Mywin, self).__init__(parent, title = title, size = size, style = wx.SYSTEM_MENU | wx.CAPTION | wx.CLOSE_BOX) 
        
        # load the data from content.json
        self.load_data()

        # create a panel
        panel = wx.Panel(self)

        # create a dropdown
        elements = list(self.data.keys())
        self.select = wx.ComboBox(panel, choices = elements) 
        self.select.Bind(wx.EVT_COMBOBOX, self.change_selection)

        # create a text area for macedonian text
        self.mk_text = wx.TextCtrl(panel, size = (200,100), style = wx.TE_MULTILINE)
        self.mk_text.Bind(wx.EVT_TEXT, self.changed_mk_text)

        # create a text area for english text
        self.en_text = wx.TextCtrl(panel ,size = (200,100), style = wx.TE_MULTILINE)
        self.en_text.Bind(wx.EVT_TEXT, self.changed_en_text) 

        # create a save button
        self.save_btn = wx.Button(panel, -1, 'Save data')
        self.save_btn.Bind(wx.EVT_BUTTON, self.save_data)

        # create grid boxes with labels
        vbox = wx.BoxSizer(wx.VERTICAL) 

        hbox1 = wx.BoxSizer(wx.HORIZONTAL) 
        l1 = wx.StaticText(panel, -1, 'Select element ID:')
        hbox1.Add(l1, 0, wx.ALL, 5)
        hbox1.Add(self.select, 0, wx.ALL, 5)

        hbox2 = wx.BoxSizer(wx.HORIZONTAL) 
        l2 = wx.StaticText(panel, -1, 'MK text:')
        hbox2.Add(l2, 0, wx.ALL, 5)
        hbox2.Add(self.mk_text, 0, wx.ALL, 5)

        hbox3 = wx.BoxSizer(wx.HORIZONTAL) 
        l3 = wx.StaticText(panel, -1, 'EN text:')
        hbox3.Add(l3, 0, wx.ALL, 5)
        hbox3.Add(self.en_text, 0, wx.ALL, 5)

        hbox4 = wx.BoxSizer(wx.HORIZONTAL) 
        hbox4.Add(self.save_btn, 0, wx.ALL, 5)

        vbox.Add(hbox1)
        vbox.Add(hbox2)
        vbox.Add(hbox3)
        vbox.Add(hbox4)
        panel.SetSizer(vbox) 

        self.Centre() 
        self.Show() 
        self.Fit()  


    def load_data(self):
        """Load the data from content.json file and convert it to dict.
        """
        self.data = ''
        with open('content.json', 'r') as file:
            self.data = json.load(file)


    def save_data(self, event):
        """Handle button click and save the data from the GUI into content.json file.
        """
        with open('content.json', 'w') as file:
            json_string = json.dumps(self.data, indent=4, sort_keys=True)
            file.write(json_string)


    def change_selection(self, event):
        """Handle selection change and fill the text areas.
        """
        translations = self.data[self.select.GetValue()]

        self.mk_text.SetValue(translations['mk'])
        self.en_text.SetValue(translations['en'])


    def changed_mk_text(self, event):
        """Handle mk text change and update the data dict.
        """
        selection = self.select.GetValue()
        if selection != '':
            self.data[selection]['mk'] = event.GetString()


    def changed_en_text(self, event):
        """Handle en text change and update the data dict.
        """
        selection = self.select.GetValue()
        if selection != '':
            self.data[selection]['en'] = event.GetString()


def create_app():
    """Create the app GUI, load the data from content.json file and save it there.
    """
    app = wx.App() 
    Mywin(None,  'Change WEB content', (270, 330)) 
    app.MainLoop()


if __name__ == '__main__':
    create_app()