import os
import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox
import yaml
from rgbi_gui_2 import RGBI_SEC_GUI

import yml_to_cli

# GUI for RGBI
class RGBI_GUI:
    def __init__(self, window):
        window.title("Bounding Box Generator")
        window.geometry('650x310')
        window.configure(background='#f0f0f0')
        window.resizable(False, False)

        self.style = ttk.Style()
        self.style.configure('TFrame', background='#f0f0f0')
        self.style.configure('TButton', background='#f0f0f0')
        self.style.configure('TLabel', background='#f0f0f0', font=('Arial', 10))

        def yolo_callbackFunc(event):
            selected_yolo = event.widget.get()
            yolo_ver.set(selected_yolo)
            print("Selected Yolo Version =", selected_yolo)

        def browseInpFunc():
            inputDir = filedialog.askopenfilename(initialdir=os.getcwd(), title="Select Input File")
            print("Input Directory =", inputDir)
            ipPathName.set(inputDir)

        def browseOutFunc():
            OutputDir = filedialog.askdirectory(initialdir=os.getcwd(), initialfile=None)
            print("Output Directory =", OutputDir)
            opPathName.set(OutputDir)

        def browseYoloFunc():
            YoloDir = filedialog.askopenfilename(initialdir=os.getcwd(), title="Select Yolo Weights File")
            print("Yolo weights Directory =", YoloDir)
            yoloPathName.set(YoloDir)

        def ymlConvert():
            data = {
                'input_dir': ipPathName.get(),
                'yolo_dir': yoloPathName.get(),
                'yolo_ver': yolo_ver.get(),
                'class_id': class_id.get(),
                'image_size': size.get(),
                'output_dir': opPathName.get()
            }

            # Path of the YAML file
            file_path = 'data.yml'

            # File opened in write mode
            with open(file_path, 'w') as file:
                yaml.dump(data, file)

        def generateReports():
            stripPath = ipPathName.get()
            stryoloPath = yoloPathName.get()
            stryoloVer = yolo_ver.get()
            intclassId = class_id.get()
            intimageSize = size.get()
            stropPath = opPathName.get()

            if (
                len(stripPath) == 0
                or len(stryoloPath) == 0
                or len(stryoloVer) == 0
                or len(str(intclassId)) == 0
                or len(str(intimageSize)) == 0
                or len(stropPath) == 0
            ):
                messagebox.showerror("Error", "Input Directory or Output Directory is not specified!")
            else:
                msgbox = messagebox.askyesno(
                    "Successful Completion",
                    "The output is generated successfully!\n\nClick 'Yes' to open the output directory.\nClick 'No' to quit this application.",
                )

                if msgbox == True:
                    path = os.path.realpath(stropPath)
                    os.startfile(path)
                    window.destroy()
                else:
                    window.destroy()

        def generateOutput():
            ymlConvert()
            yml_to_cli.Command.run_command()
            generateReports()
            results_gui = RGBI_SEC_GUI()

        self.frame_header = LabelFrame(window, text = 'Choose the options:', padx = 10, pady = 5, font = ('Arial', 10, 'bold'))
        self.frame_header.config(relief = GROOVE)
        self.frame_header.pack()
                   
        self.labelInput = ttk.Label(self.frame_header, text = "Input Directory:") 
        self.labelInput.grid(column = 0, row = 0,  sticky = 'sw', pady = 10)
        ipPathName = StringVar(value=os.path.abspath(os.getcwd()).replace("\\", "/"))
        self.entryInputPath = ttk.Entry(self.frame_header, width = 55, font = ('Arial',10), textvariable = ipPathName)
        self.entryInputPath.grid(column = 1, row = 0)
        self.btnBrowseIpDir = ttk.Button(self.frame_header, text = "Browse", command = browseInpFunc)
        self.btnBrowseIpDir.grid(column = 2, row = 0,  padx = 10, ipadx = 2, ipady = 2)
        
        self.labelYoloPath = ttk.Label(self.frame_header, text = "Yolo Weights Path:")
        self.labelYoloPath.grid(column = 0, row = 1, sticky = 'sw', pady = 10)
        yoloPathName = StringVar(value=os.path.abspath(os.getcwd()).replace("\\", "/"))
        self.entryyoloPath = ttk.Entry(self.frame_header, width = 55, font = ('Arial',10), textvariable = yoloPathName)
        self.entryyoloPath.grid(column = 1, row = 1)
        self.btnBrowseYoloDir = ttk.Button(self.frame_header, text = "Browse", command = browseYoloFunc)
        self.btnBrowseYoloDir.grid(column = 2, row = 1,  padx = 10, ipadx = 2, ipady = 2)
        
        self.labelVersion = ttk.Label(self.frame_header, text = "YOLO Version:")
        self.labelVersion.grid(column = 0, row = 2, sticky = 'sw', pady = 10) 
        yolo_ver = StringVar()

        self.comboYolo = ttk.Combobox(self.frame_header, width = 15, values=["v8", "v7", "v5"], textvariable = yolo_ver)
        self.comboYolo.grid(column = 1, row = 2, sticky = 'sw', pady = 10)
        self.comboYolo.current(0)

        self.labelClass = ttk.Label(self.frame_header, text = "Class Id:")
        self.labelClass.grid(column = 0, row = 3, sticky = 'sw', pady = 10)
        class_id = IntVar()
        class_id.set(0)
        self.entrycid = tk.Entry(self.frame_header, width = 15, font = ('Arial',10), textvariable = class_id)
        self.entrycid.grid(column = 1, row = 3, sticky = 'sw', pady = 10)

        self.labelSize = ttk.Label(self.frame_header, text = "Image Size:")
        self.labelSize.grid(column = 0, row = 4, sticky = 'sw', pady = 10)
        size = IntVar()
        size.set(640) 
        self.entrysize = tk.Entry(self.frame_header, width = 15, font = ('Arial',10), textvariable = size)
        self.entrysize.grid(column = 1, row = 4, sticky = 'sw', pady = 10)

        self.labelOutputPath = ttk.Label(self.frame_header, text = "Output Directory:")
        self.labelOutputPath.grid(column = 0, row = 5, sticky = 'sw', pady = 10)
        opPathName = StringVar(value=os.path.abspath(os.getcwd()).replace("\\", "/"))
        self.entryOutputPath = ttk.Entry(self.frame_header, width = 55, font = ('Arial',10), textvariable = opPathName)
        self.entryOutputPath.grid(column = 1, row = 5)
        self.btnBrowseOpDir = ttk.Button(self.frame_header, text = "Browse", command = browseOutFunc)
        self.btnBrowseOpDir.grid(column = 2, row = 5,  padx = 10, ipadx = 2, ipady = 2)

        self.btnGenRes = ttk.Button(self.frame_header, text = "Generate Output", command = generateOutput, width=30)
        self.btnGenRes.grid(column = 1, row = 6, ipadx = 3, ipady = 3)
                    
        self.comboYolo.bind("<<ComboboxSelected>>", yolo_callbackFunc)
        
        
def main():            
    window = Tk()
    RGBI_GUI(window)
    window.mainloop()

if __name__ == "__main__": 
    main()
