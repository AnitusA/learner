import json
import time

def user():
    subject = input("Enter the subject: ")
    syllabus = input("Enter the syllabus (separate by commas): ")
    topics = [topic.strip() for topic in syllabus.split(",")]

    study_plan = {"subject": subject, "topics": []}
    index = 0
    while index < len(topics):
        print(f"\nTopic {index + 1}: {topics[index]}")
        timing = int(input("How much time do you need for this topic : "))
        study_plan["topics"].append({"index": index + 1, "topic": topics[index], "time": timing})
        remainder= timing / 3
        wastetime = 0
        for i in range(3):
            time.sleep(remainder)
            wastetime += remainder
            remain = timing - wastetime
            print(f"Reminder {i+1}: Keep working on {topics[index]}")
            print(f"Remaining time: {remain : .2f} seconds")
        if remain == 0:
            print(" time is crossed the deadline for this topic")
           
        ask=input(f"\nYou have completed {topics[index]} ? (yes/no): ").lower()
        if ask == "yes":
            print("great")
            
            
        else :
            print("you have not completed your topic you can finish it by later")
            print("your activity is saved in your learning page")
            exit()

        if index == len(topics) - 1:
            print("\nYou have completed your syllabus")
            quiz()
            break
        print("\nYou have completed the current topic.")
        continue_study = input("Do you want to continue to the next topic? (yes/no): ").strip().lower()
        if continue_study != "yes":
            break
        
        index += 1


    save_to_json(study_plan)

def quiz():
    print("Welcome to the quiz!")
    print("Please answer the following questions with 'yes' or 'no'.")
    mark = 0
    question1 = input("list is immutable ? (yes/no): ").lower()
    if question1 == "no":
        mark += 1
        print("Correct!")
    else:
        print("Incorrect!")
    question2 = input("Set allow duplicate values ? (yes/no): ").lower()
    if question2 == "no":
        mark += 1
        print("Correct!")
    else:
        print("Incorrect!")
    question3 = input("Set is un ordered ? (yes/no): ").lower()
    if question3 == "yes":
        mark += 1
        print("Correct!")
    else:
        print("Incorrect!")
    question4 = input("def keyword is only used for user defined function ? (yes/no): ").lower()
    if question4 == "yes":
        mark += 1
        print("Correct!")
    else:
        print("Incorrect!")
    question5 = input("tuple is mutable ? (yes/no): ").lower()
    if question5 == "no":
        mark += 1
        print("Correct!")
    else:
        print("Incorrect!")
    marks = (mark / 5) * 100
    print(f"Your score is: {marks}%")
    if marks >= 20:
        print("You have completed the subject successfully.")
    else :
        print("You have not completed the subject successfully.")
        user()

            
                

def save_to_json(data):
    filename = "study_plan.json"
    with open(filename, "w") as f:
        json.dump(data, f, indent=4)
        print("your activity is saved in your learning page")

if __name__ == "__main__":
    user()