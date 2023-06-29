import subprocess,sys,zipfile,io,time,requests,config
from pathlib import Path



def solve():
    samples_url = f"https://open.kattis.com/problems/{config.ExerciseName}/file/statement/samples.zip"
    r = requests.get(samples_url)
    r.raise_for_status()

    with zipfile.ZipFile(io.BytesIO(r.content)) as z:
        for file in z.filelist:
            ExercisePath = "Exercises/" + config.exerciseFolder
            ExerciseFile = ExercisePath + "/" + config.exerciseFolder + ".py"
            file_path = Path(file.filename)
            print("-------------------------")
            if file_path.suffix == ".in":
                test_input = z.read(file).decode("utf-8")
                test_answer = z.read(f"{file_path.stem}.ans").decode("utf-8")
                t1 = time.time()
                p = subprocess.run([sys.executable, ExerciseFile],
                                   input=test_input, encoding="utf-8", capture_output=True)
                print(time.time() - t1, "ms")
                if p.returncode != 0:
                    print("Error:", p.stderr)
                print("Sample input:\n", test_input, sep="")
                if p.stdout != test_answer:
                    print("Wrong answer!")
                    print("Expected:,", len(test_answer), "\n", test_answer, sep="")
                    print("Got:", len(p.stdout), "\n", p.stdout, sep="")
                else:
                    print("Good answer!")
                    print("Answer:\n", p.stdout, sep="")