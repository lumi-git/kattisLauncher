import os
import subprocess
from config import *

print("Launching " + ExerciseName + " in " + inputMode.name+" mode.")
if inputMode == inputModes.KATTISAPI:
    os.system("python3 KattisApiRequester.py "+ExerciseName+" " + exerciseFile)

elif inputMode == inputModes.FILE:
    with open(inputFile, 'r') as file:
        input_data = file.read().encode()  # We need to encode the string to bytes

    p = subprocess.run(["python3", exerciseFile], input=input_data, capture_output=True)
    print("---")
    print("Your output :")

    print(p.stdout.decode())
    print("---")
    print("Expected :")

    print(open(outputFile).read())


elif inputMode == inputModes.CONSOLE:
    os.system(exerciseFile)