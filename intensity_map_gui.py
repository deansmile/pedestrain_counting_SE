# Ground truth images directory
# Model
# Output directory

import os

import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox

import yaml

# GUI for RGBI           

class RGBI_SEC_GUI:
    
    def __init__(self):
        self.window = Tk()
        self.window.title("Intensity Map Generator")
        self.window.geometry('660x230')
        self.window.configure(background = '#f0f0f0')
        self.window.resizable(False, False)
        
        self.style = ttk.Style()
        self.style.configure('TFrame',  background = '#f0f0f0')
        self.style.configure('TButton', background = '#f0f0f0')
        self.style.configure('TLabel',  background = '#f0f0f0', font = ('Arial', 10))     

        def yolo_callbackFunc(event):
            selected_model = event.widget.get()
            model.set(selected_model)
            print("Selected Yolo Version = ", selected_model)                                                        
        
        def browseOutFunc():
            OutputDir = filedialog.askdirectory(initialdir=os.getcwd(), initialfile=None)
            print("Output Directory = ", OutputDir)
            opPathName.set(OutputDir)

        def browseOiFunc():
            OiDir = filedialog.askopenfilename(initialdir=os.getcwd(), title = "Select Original Image")
            print("Original Image Directory = ", OiDir)
            oiPathName.set(OiDir)

        def browseGrtFunc():
            GrtDir = filedialog.askopenfilename(initialdir=os.getcwd(), title = "Select Ground Truth Image")
            print("Ground Truth Image Directory = ", GrtDir)
            grtPathName.set(GrtDir)

        def ymlConvert():
            data = {
            'model': model.get(),
            'ground_truth_dir': grtPathName.get(),
            'output_dir': opPathName.get()
            }

            # Path of the YAML file
            file_path = 'data.yml'

            # File opened in write mode
            with open(file_path, 'w') as file:
                yaml.dump(data, file)

        def generateReports():
            
            strgroundtruthPath = grtPathName.get()
            strModel     = model.get()
            stropPath = opPathName.get()

            if len(strgroundtruthPath) == 0 or len(strModel) == 0 or len(stropPath) == 0:
                 messagebox.showerror("Error", "Input Directory or Output Directory is not specified!")
            else: 
                msgbox = messagebox.askyesno("Successful Completion", "The output is generated successfully!\n\nClick 'Yes' to open the output directory.\nClick 'No' to quit this application.")
                    
                if msgbox == True:
                    path=os.path.realpath(stropPath)
                    os.startfile(path)
                else:
                    self.window.destroy()
        
        def generateOutput():
            ymlConvert()
            generateReports()

       
        self.frame_header = LabelFrame(self.window, text = 'Choose the options:', padx = 10, pady = 5, font = ('Arial', 10, 'bold'))
        self.frame_header.config(relief = GROOVE)
        self.frame_header.pack()
                   
        self.labelOIPath = ttk.Label(self.frame_header, text = "Original Image:")
        self.labelOIPath.grid(column = 0, row = 0, sticky = 'sw', pady = 10)
        oiPathName = StringVar(value=os.path.abspath(os.getcwd()).replace("\\", "/"))
        self.entryoiPath = ttk.Entry(self.frame_header, width = 55, font = ('Arial',10), textvariable = oiPathName)
        self.entryoiPath.grid(column = 1, row = 0)
        self.btnBrowseOiDir = ttk.Button(self.frame_header, text = "Browse", command = browseOiFunc)
        self.btnBrowseOiDir.grid(column = 2, row = 0,  padx = 10, ipadx = 2, ipady = 2)

        self.labelGrtPath = ttk.Label(self.frame_header, text = "Ground Truth Image:")
        self.labelGrtPath.grid(column = 0, row = 1, sticky = 'sw', pady = 10)
        grtPathName = StringVar(value=os.path.abspath(os.getcwd()).replace("\\", "/"))
        self.entrygrtPath = ttk.Entry(self.frame_header, width = 55, font = ('Arial',10), textvariable = grtPathName)
        self.entrygrtPath.grid(column = 1, row = 1)
        self.btnBrowseGrtDir = ttk.Button(self.frame_header, text = "Browse", command = browseGrtFunc)
        self.btnBrowseGrtDir.grid(column = 2, row = 1,  padx = 10, ipadx = 2, ipady = 2)
        
        self.labelVersion = ttk.Label(self.frame_header, text = "Model:")
        self.labelVersion.grid(column = 0, row = 2, sticky = 'sw', pady = 10) 
        model = StringVar()
        self.comboYolo = ttk.Combobox(self.frame_header, width = 15, values=["MCNN", "XYZ"], textvariable = model)
        self.comboYolo.grid(column = 1, row = 2, sticky = 'sw', pady = 10)
        self.comboYolo.current(0)

        self.labelOutputPath = ttk.Label(self.frame_header, text = "Output Directory:")
        self.labelOutputPath.grid(column = 0, row = 3, sticky = 'sw', pady = 10)
        opPathName = StringVar(value=os.path.abspath(os.getcwd()).replace("\\", "/"))
        self.entryOutputPath = ttk.Entry(self.frame_header, width = 55, font = ('Arial',10), textvariable = opPathName)
        self.entryOutputPath.grid(column = 1, row = 3)
        self.btnBrowseOpDir = ttk.Button(self.frame_header, text = "Browse", command = browseOutFunc)
        self.btnBrowseOpDir.grid(column = 2, row = 3,  padx = 10, ipadx = 2, ipady = 2)

        self.btnGenRes = ttk.Button(self.frame_header, text = "Generate Output", command = generateOutput, width=30)
        self.btnGenRes.grid(column = 1, row = 4, ipadx = 3, ipady = 3)
                    
        self.comboYolo.bind("<<ComboboxSelected>>", yolo_callbackFunc)

        

def main():            
    RGBI_SEC_GUI()

if __name__ == "__main__": 
    main() 
