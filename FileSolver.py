import os, time, subprocess, sys
from config import *


def solve():
    samplePath = "Exercises/" + exerciseFolder + "/samples"
    ExercisePath = "Exercises/" + exerciseFolder + "/" + exerciseFolder + ".py"
    for file in os.listdir(samplePath):
        file_path = samplePath + "/" + file
        print("-------------------------")
        if file_path.endswith(".in"):
            test_input = open(file_path).read().encode("utf-8")
            test_answer = open(file_path.replace(".in", ".ans")).read().encode("utf-8")
            t1 = time.time()
            p = subprocess.run([PythonShortcut, ExercisePath], input=test_input, capture_output=True)
            print(time.time() - t1, "ms")
            if p.returncode != 0:
                print("Error:", p.stderr)
            print("Sample input:\n", test_input.decode(), sep="")
            if p.stdout != test_answer:
                print("Wrong answer!")
                print("Expected:,", len(test_answer), "\n", test_answer.decode(), sep="")
                print("Got:", len(p.stdout.decode()), "\n", p.stdout.decode(), sep="")
            else:
                print("Good answer!")
                print("Answer:\n", p.stdout.decode(), sep="")
