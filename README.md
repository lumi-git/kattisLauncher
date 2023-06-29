# kattisLauncher

Complete simple launcher for kattis exercises

## setup

Basic setup for the launcher

- be sure to have all modules by running : 
    > python3 -m pip install -r requirements.txt
    
    or

    > pip install -r requirements.txt

    based on your python config


- Place your exercise in the Exercises folder

- configure the exercise you want to run in config.py as explained in the configuration section

- the output will be print in the console

- a log file will be created in the Logs folder to keep track of the exercises you have done

## Configuration

You will be able to modify these values in config.py file


- ExerciseName
    - > The name of the exercise you want to code based on the kattis website
- inputMode
    - > The mode of input you want to use based on inputModes enum

- exerciseFolder
    - > The name of the folder where your exercise is located
    (The folder must be in the Exercises folder, and the name must be the same as the python file)
      
- PythonShortcut
    - > The shortcut you want to use to run the python file

## usage

- kattis API Mode
  - Set the exerciseName and exerciseFile 
  - Run the Launcher.py file with inputMode = inputModes.KATTISAPI
    > this mode will run the exerciseFile with the input from the kattis website and will compare the output with the output from the kattis website.

- File Mode
  - set the input file and output file you want to use
  - run the Launcher.py file with inputMode = inputModes.FILE
  > this mode will run the exerciseFile with the inputFile as input and will compare the output with the outputFile.
- Console Mode
  - run the Launcher.py file with inputMode = inputModes.CONSOLE
  - write the input in the console
    > this mode will run the exerciseFile with the input from the console.