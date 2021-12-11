import PySimpleGUI as sg



layout_1 = [
    [sg.Listbox(values=( self.list_files() ),
                    select_mode=None, 
                    enable_events=True ,
                    size=(40,18),
                    bind_return_key=True,
                    key="list_box")]


]