import os,subprocess,datetime
from config import *

def logConfig() :
    cfgFileName = "Logs/"+exerciseFile.replace(".py","")+" - "+ExerciseName+".log"
    current_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    sep = f"------------------- {ExerciseName} - { current_date }------------------\n"
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

ExercisePath = "Exercises/"+exerciseFile

if inputMode == inputModes.KATTISAPI:
    os.system(PythonShortcut+" KattisApiRequester.py "+ExerciseName+" " + ExercisePath)

elif inputMode == inputModes.FILE:
    with open(inputFile, 'r') as file:
        input_data = file.read().encode()  # We need to encode the string to bytes

    p = subprocess.run([PythonShortcut, ExercisePath], input=input_data, capture_output=True)
    print("---")
    print("Your output :")

    print(p.stdout.decode())
    print("---")
    print("Expected :")

    print(open(outputFile).read())

elif inputMode == inputModes.CONSOLE:
    os.system(PythonShortcut + " " + ExercisePath)