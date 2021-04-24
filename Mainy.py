######################################################################################################################
### Initialisation
######################################################################################################################
import os
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
from tkinter.scrolledtext import ScrolledText

# New dictionaries holding relevant data from log file.
parameters_dict1 = {}
parameters_dict2 = {}
differences_list = []

# Parses the 'Essential Parameters'.
parameters_list = ['Filter', 'Frame Averaging', 'Camera binning', 'Source Voltage (kV)',
                   'Source Current (uA)', 'Exposure (ms)', 'Rotation Step (deg)', 'Scanning position'
                   'Image Pixel Size (um)', 'Use 360 Rotation', 'Random Movement', 'Scan duration', 
                   'Minimum for CS to Image Conversion', 'Maximum for CS to Image Conversion',
                   'Smoothing', 'Ring Artifact Correction']

def resource_path(relative_path):
    """ Get absolute path to resource """
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)

# Prepares information for the 'About' button.
aboutText = []
aboutPath = resource_path("about")
aboutFile = open(aboutPath, "r", encoding="utf-8")
for line in aboutFile.readlines():
    aboutText.append(line)
informationAbout = ''.join(aboutText)

# Prepares information for the 'Use Guide' button.
useText = []
usePath = resource_path("useGuide")
useFile = open(usePath, "r", encoding="utf-8")
for line in useFile.readlines():
    useText.append(line)
informationUseGuide = ''.join(useText)

######################################################################################################################
### Functions
######################################################################################################################

def openLogFileandProcess1():
  """ Processes the first log file """
    textArea.delete("1.0", "end")
    logPath1.delete("1.0", "end")

    # User directs to path of first log file.
    tf1 = filedialog.askopenfilename(
        initialdir="C:/Users/MainFrame/Desktop/",
        title="Choose log file 1",
        filetypes=(("Log Files", "*.log"),))

    logPath1.insert(END, tf1)  # Writes path address to text box in GUI

    # Opens and parses the data from log file
    with open(tf1, 'r') as fin:
        for line in fin:
            position = line.find('=')
            parameters_dict1[line[:position]] = (line[position + 1:]).strip()


def openLogFileandProcess2():
    """ Processes the second log file """
    textArea.delete("1.0", "end")
    logPath2.delete("1.0", "end")

    # User directs to path of second log file.
    tf2 = filedialog.askopenfilename(
        initialdir="C:/Users/MainFrame/Desktop/",
        title="Choose logg file 2",
        filetypes=(("Log Files", "*.log"),))

    logPath2.insert(END, tf2)  # Writes path address to text box in GUI

    # Opens and parses the data from log file
    with open(tf2, 'r') as fin:
        for line in fin:
            position = line.find('=')
            parameters_dict2[line[:position]] = (line[position + 1:]).strip()


def compareLogFiles():
   """Compares the 'Essential' parameters of the log files"""
    textArea.delete("1.0", END)
    
    # Determines the number of different parameters
    differencesCounter = 0
    for k1, v1 in parameters_dict1.items():
        for k2, v2 in parameters_dict2.items():
            if k1 == k2:
                if v1 != v2:
                    differences_list.append(k1)
                    differencesCounter += 1

    # Prints a summary in the text box.
    # The number of differences and lists parameters.               
    summaryDifference(differencesCounter)
    for object in differences_list:
        textArea.insert(END, '\n' + object)
  
    # Detailed output of similarities and differences.
    textArea.insert(INSERT, "\n\n" + "=" * 97)
    for k1, v1 in parameters_dict1.items():
        for k2, v2 in parameters_dict2.items():
            if k1 == k2:
                if v1 != v2:
                    k1_count = 48 - len(k1.strip())  # Text formatting
                    v1_count = 41 - len(v1.strip())  # Text formatting
                    v2_count = 41 - len(v2.strip())  # Text formatting
                    textArea.insert(END, "\n" + k1 + " " * k1_count + "|\nLog 1: " + v1 + " " * v1_count + "|\nLog 2: "
                                    + v2 + " " * v2_count + "|\n" + '-' * 97)

                else:
                    textArea.insert(END, "\n\t\t\t\t\t\t| " + k1 + "\n\t\t\t\t\t\t| Log 1: " + v1 +
                                    "\n\t\t\t\t\t\t| Log 2: " + v2 + "\n" + "-" * 97)


def compareEssentialLogFiles():
    """Compares all parameters in the log file for differences"""
    textArea.delete("1.0", END)
    
    # Determines number of differences between parameters
    differencesCounter = 0
    for k1, v1 in parameters_dict1.items():
        for k2, v2 in parameters_dict2.items():
            if k1 in parameters_list:
                if k1 == k2:
                    if v1 != v2:
                        differences_list.append(k1)
                        differencesCounter += 1

    # Prints a summary in the text box.
    # The number of differences and lists parameters.
    summaryDifference(differencesCounter)
    for object in differences_list:
        textArea.insert(END, '\n' + object)

    # Detailed output of similarities and differences.
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
    """Clears all text fields on screen"""
    textArea.delete("1.0", END)
    logPath1.delete("1.0", END)
    logPath2.delete("1.0", END)
    parameters_dict1.clear()
    parameters_dict2.clear()
    differences_list.clear()


def summaryDifference(differencesCounter):
    """Summarises the number of differences as a sentance """
    textArea.insert(END, "\n======== Summary =======\n")
    if differencesCounter == 0:
        textArea.insert(END, 'There are no differences\nbetween the log files')
    if differencesCounter == 1:
        textArea.insert(END, 'There is 1 difference\nbetween the log files\n')
    if differencesCounter > 1:
        textArea.insert(END, 'There are ' + str(differencesCounter) + ' differences\nbetween the log files\n')
    textArea.insert(END, '========================')

def aboutInformation():
  """ Displays message box with program information """
    messagebox.showinfo('about', message=informationAbout)

def useInformation():
  """ Displays message box with program use information """
    messagebox.showinfo('useGuide', message=informationUseGuide)


######################################################################################################################
### GUI Interface Setup
######################################################################################################################

# Main windows setup
mainWindow = Tk()  # Links main window to the interpreter
mainWindow.title("LogFile_CompareEasy by Kamil_Sokolowski")
mainWindow.geometry("810x600+200+15")  # Window size and initial position
mainWindow['bg'] = 'gray98'  # Background colour

# Icon top left window
iconPath = resource_path("icon.png")
mainWindow.tk.call('wm', 'iconphoto', mainWindow._w, PhotoImage(file=iconPath))

# Text box
textArea = ScrolledText(mainWindow, width=97, height=29, bg='old lace', yscrollcommand='textScroll.set')
textArea.place(x=10, y=120)
asciiPath = resource_path("asciiArt")
asciiArt = open(asciiPath, 'r')
asciiArtOutput = asciiArt.read()
textArea.insert(END, asciiArtOutput)

# Log file path output text areas
logPath1 = Text(mainWindow, width=50, height=1, bg='old lace')
logPath1.place(x=95, y=5)
logPath2 = Text(mainWindow, width=50, height=1, bg='old lace')
logPath2.place(x=95, y=33)

# Main buttons
Button(mainWindow, text="Log file 1", command=openLogFileandProcess1, height=1, width=10).place(x=9, y=2)
Button(mainWindow, text="Log file 2", command=openLogFileandProcess2, height=1, width=10).place(x=9, y=30)
Button(mainWindow, text="Compare All", command=compareLogFiles, height=1, width=55).place(x=408, y=60)
Button(mainWindow, text="Compare Essentials", command=compareEssentialLogFiles, height=1, width=55).place(x=9, y=60)
Button(mainWindow, text="Clear All", command=clearAllFields, height=3, width=8).place(x=737, y=2)
Button(mainWindow, text="Guide", command=useInformation, height=1, width=7).place(x=675, y=4)
Button(mainWindow, text="About", command=aboutInformation, height=1, width=7).place(x=675, y=32)

# Labels
Label(mainWindow, text="Different Parameters", bg='gray98').place(x=100, y=98)
Label(mainWindow, text="Identical Parameters", bg='gray98').place(x=550, y=98)
Label(mainWindow, text="Ready to compare \neasy?", bg='gray98', font='Helvetica 15').place(x=500, y=2)

mainWindow.mainloop()
