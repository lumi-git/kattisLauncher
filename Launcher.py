import os,subprocess,datetime,FileSolver
from config import *

def logConfig() :
    cfgFileName = "Logs/"+exerciseFolder +"-"+ExerciseName+".log"
    current_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    sep = f"------------------- {ExerciseName} - { current_date } ------------------\n"
    cfg = open("config.py", "r").read()

    if not os.path.exists(cfgFileName):
        # Create the file if it doesn't exist
        open(cfgFileName, 'w+').close()

    cfgSave = open(cfgFileName, "r")
    content = cfgSave.read()
    cfgSave.close()
    cfgSave = open(cfgFileName, "w")
    cfgSave.write(sep+cfg+ "\n" +content)
    cfgSave.close()

print("Launching " + ExerciseName + " in " + inputMode.name+" mode.")
logConfig()

ExercisePath = "Exercises/"+exerciseFolder
ExerciseFile = ExercisePath+"/"+exerciseFolder+".py"
if inputMode == inputModes.KATTISAPI:
    os.system(PythonShortcut+" KattisApiRequester.py "+ExerciseName+" " + ExerciseFile)

elif inputMode == inputModes.FILE:
    FileSolver.solve()

elif inputMode == inputModes.CONSOLE:
    os.system(PythonShortcut + " " + ExerciseFile)