#TO RUN:
#set the filename variable to the name of the question data, you could save it as questions.txt if youd like
#make sure the files are in the same directory
#run python3 study.py

import random

filename = "questions.txt" #filename var is HERE

questions = []
entry = {}
with open(filename) as file:
    with open(filename) as file:
        lines = [line.rstrip() for line in file]

    lastedit = "q"
    for i in range(len(lines)):
        line = lines[i]
        if (line.startswith("-   Question")):
            lastedit = "q"
            questions.append(entry)
            entry = {}
            entry["answers"] = []
            entry["question"] = line.strip()
        elif(len(line) > 6 and line[5] == ":"):
            lastedit = "a"
            entry["answers"].append(line[4:].strip())
        elif(len(line) > 11 and line[10] == ":"):
            lastedit = "s"
            entry["solution"] = (line[4:].strip())
        elif(len(line) > 16 and line[15] == ":"):
            lastedit = "e"
            entry["explanation"] = (line[4:].strip())
        else:
            if (lastedit == "q"):
                entry["question"] = entry["question"] + "\n" + line
            #if (lastedit == "a"):
            #if (lastedit == "s"):
            if (lastedit == "e"):
                entry["explanation"] = entry["explanation"] + "\n" + line

        i += 1
                


del questions[0]

def globalFunc():
    global total_correct
    total_correct = 0

globalFunc()


#questions are ready

def printQuestion(question, index):
    global total_correct
    print("\n\n\n\n\n\n\n\n\n\n\n" + question["question"] + "\n\n")
    for answer in question["answers"]:
        print(answer)

    solution = question["solution"][8]
    your_answer = input("\n\n\n\n\n\n\n\nYour answer: ")
    if (solution == your_answer):
        print("\nCorrect!")
        total_correct += 1
    else:
        print("\nNot quite.")
    print("\n" + question["solution"])
    print("\n\n" + question["explanation"])
    

    print(str(total_correct) + "/" +  str(index + 1))
    print("Percentage: " + "{0:.0%}".format(total_correct / (index + 1)))

    input("\n\n\npress enter to move on: ")

print("Terraform Study")
play_count = input("How many questions would you like to study? (INT or 'all', such as '1', '10', 'all'): ")
is_random = input("Would you like the questions to be random? (yes or no): ")
if (is_random == "yes"):
    random.shuffle(questions)

if (play_count == "all"):
    play_count = len(questions)
else:
    play_count = int(play_count)

for i in range(play_count):
    print("\n\n\tQuestion " + str(i + 1) + "/" + str(play_count) + ":\n")
    printQuestion(questions[i], i)

print("Complete!")
print("Final Score: " + "{0:.0%}".format(total_correct / (play_count)))