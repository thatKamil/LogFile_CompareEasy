######################################################################################################################
### Initialisation
######################################################################################################################
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
from tkinter.scrolledtext import ScrolledText

# New dictionaries holding relevant data from log file.
parameters_dict1 = {}
parameters_dict2 = {}
differences_list = []

parameters_list = ['Filter', 'Frame Averaging', 'Camera binning', 'Source Voltage (kV)',
                   'Source Current (uA)', 'Exposure (ms)', 'Rotation Step (deg)', 'Scanning position'
                                                                                  'Image Pixel Size (um)',
                   'Use 360 Rotation', 'Random Movement',
                   'Scan duration', 'Minimum for CS to Image Conversion', 'Maximum for CS to Image Conversion',
                   'Smoothing', 'Ring Artifact Correction']


######################################################################################################################
### Functions
######################################################################################################################

def openLogFileandProcess1():
    textArea.delete("1.0", "end")
    logPath1.delete("1.0", "end")

    tf1 = filedialog.askopenfilename(
        initialdir="C:/Users/MainFrame/Desktop/",
        title="Open Log file",
        filetypes=(("Log Files", "*.log"),)
    )

    logPath1.insert(END, tf1)  # Writes path address to text box in GUI

    # Opens and parses the data from log file
    with open(tf1, 'r') as fin:
        for line in fin:
            position = line.find('=')
            parameters_dict1[line[:position]] = (line[position + 1:]).strip()


def openLogFileandProcess2():
    textArea.delete("1.0", "end")
    logPath2.delete("1.0", "end")

    tf2 = filedialog.askopenfilename(
        initialdir="C:/Users/MainFrame/Desktop/",
        title="Open Log file",
        filetypes=(("Log Files", "*.log"),)
    )

    logPath2.insert(END, tf2)  # Writes path address to text box in GUI

    # Opens and parses the data from log file
    with open(tf2, 'r') as fin:
        for line in fin:
            position = line.find('=')
            parameters_dict2[line[:position]] = (line[position + 1:]).strip()


def compareLogFiles():
    differencesCounter = 0
    textArea.insert(INSERT, "=" * 97)
    for k1, v1 in parameters_dict1.items():
        for k2, v2 in parameters_dict2.items():
            if k1 == k2:
                if v1 != v2:
                    differences_list.append(k1)
                    differencesCounter += 1

    summaryDifference(differencesCounter)
    for object in differences_list:
        textArea.insert(END, '\n' + object)

    textArea.insert(INSERT, "\n\n" + "=" * 97)
    for k1, v1 in parameters_dict1.items():
        for k2, v2 in parameters_dict2.items():
            if k1 == k2:
                if v1 != v2:
                    k1_count = 48 - len(k1.strip())
                    v1_count = 41 - len(v1.strip())
                    v2_count = 41 - len(v2.strip())
                    textArea.insert(END, "\n" + k1 + " " * k1_count + "|\nLog 1: " + v1 + " " * v1_count + "|\nLog 2: "
                                    + v2 + " " * v2_count + "|\n" + '-' * 97)

                else:
                    textArea.insert(END, "\n\t\t\t\t\t\t| " + k1 + "\n\t\t\t\t\t\t| Log 1: " + v1 +
                                    "\n\t\t\t\t\t\t| Log 2: " + v2 + "\n" + "-" * 97)


def compareEssentialLogFiles():
    differencesCounter = 0
    textArea.insert(INSERT, "=" * 97)
    for k1, v1 in parameters_dict1.items():
        for k2, v2 in parameters_dict2.items():
            if k1 in parameters_list:
                if k1 == k2:
                    if v1 != v2:
                        differences_list.append(k1)
                        differencesCounter += 1

    summaryDifference(differencesCounter)
    for object in differences_list:
        textArea.insert(END, '\n' + object)

    textArea.insert(INSERT, '\n\n' + "=" * 97)
    for k1, v1 in parameters_dict1.items():
        for k2, v2 in parameters_dict2.items():
            if k1 in parameters_list:
                if k1 == k2:
                    if v1 != v2:
                        k1_count = 48 - len(k1.strip())
                        v1_count = 41 - len(v1.strip())
                        v2_count = 41 - len(v2.strip())
                        textArea.insert(END,
                                        "\n" + k1 + " " * k1_count + "|\nLog 1: " + v1 + " " * v1_count + "|\nLog 2: "
                                        + v2 + " " * v2_count + "|\n" + '-' * 97)

                    else:
                        textArea.insert(END, "\n\t\t\t\t\t\t| " + k1 + "\n\t\t\t\t\t\t| Log 1: " + v1 +
                                        "\n\t\t\t\t\t\t| Log 2: " + v2 + "\n" + "-" * 97)


def clearAllFields():
    textArea.delete("1.0", END)
    logPath1.delete("1.0", END)
    logPath2.delete("1.0", END)
    parameters_dict1.clear()
    parameters_dict2.clear()
    differences_list.clear()


def about():
    messagebox.showinfo('LogFile_CompareEasy', 'Developed by Kamil Sokolowski \nkamil.sokolowski@tri.edu.au \n\n'
                                               'Version 1.1 34th Feb 2021')


def summaryDifference(differencesCounter):
    textArea.insert(END, "\n======== Summary =======\n")
    if differencesCounter == 0:
        textArea.insert(END, 'There are no differences\nbetween the log files')
    if differencesCounter == 1:
        textArea.insert(END, 'There is 1 difference\nbetween the log files\n')
    if differencesCounter > 1:
        textArea.insert(END, 'There are ' + str(differencesCounter) + ' differences\nbetween the log files\n')
    textArea.insert(END, '========================')


######################################################################################################################
### GUI Interface Setup
######################################################################################################################

# Main windows setup
mainWindow = Tk()  # Links main window to the interpreter
mainWindow.title("LogFile_CompareEasy by Kamil_Sokolowski")
mainWindow.geometry("810x935+500+10")  # Window size and initial position
mainWindow['bg'] = 'khaki1'  # Background colour

# Text box
textArea = ScrolledText(mainWindow, width=97, height=50, bg='old lace', yscrollcommand='textScroll.set')
textArea.place(x=10, y=120)

# Log file path output text areas
logPath1 = Text(mainWindow, width=34, height=1, bg='old lace')
logPath1.place(x=95, y=34)
logPath2 = Text(mainWindow, width=34, height=1, bg='old lace')
logPath2.place(x=95, y=62)

# Main buttons
Button(mainWindow, text="Open Log 1", command=openLogFileandProcess1, height=1, width=10).place(x=9, y=30)
Button(mainWindow, text="Open Log 2", command=openLogFileandProcess2, height=1, width=10).place(x=9, y=60)
Button(mainWindow, text="Compare All", command=compareLogFiles, height=1, width=51).place(x=9, y=2)
Button(mainWindow, text="Compare Essentials", command=compareEssentialLogFiles, height=1, width=51).place(x=425, y=2)
Button(mainWindow, text="Clear All", command=clearAllFields, height=3, width=8).place(x=725, y=30)

# Labels
Label(mainWindow, text="Different Parameters", bg='khaki1').place(x=100, y=98)
Label(mainWindow, text="Identical Parameters", bg='khaki1').place(x=550, y=98)
Label(mainWindow, text="LogFile_CompareEasy", bg='khaki1', font='Helvetica 20').place(x=420, y=50)

textArea.insert(END, "\n\n\n\n\t Are you ready to compare easy?")

menubar = Menu(mainWindow, background='#ff0000', foreground='black', activebackground='white', activeforeground='black')
file = Menu(menubar, tearoff=0, background='white', foreground='black')
file.add_command(label="Save output")
file.add_command(label="Exit", command=mainWindow.quit)
menubar.add_cascade(label="More", menu=file)

help = Menu(menubar, tearoff=0)
help.add_command(label="Developer", command=about)
menubar.add_cascade(label="Info", menu=help)
mainWindow.config(menu=menubar)

mainWindow.mainloop()
