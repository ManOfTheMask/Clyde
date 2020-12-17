import time
import datetime
import random
import math
import json

print("Clyde.py using Python 3.8.2 ")


responses = {
    "questions" : [
        "who are you",
        "what is your age",
        "what is your favorite number",
        "who is the best teacher",
        "what is your favorite color",
        "are you a real ai",
        "who created you",
        "why so serious"
    ],
    "response" : [
        "My name is Clyde",
        "0",
        "69",
        "Mrs caso",
        "green",
        "No I am a chat bot like cleverbot",
        "ecdthegreat and pastaboy844 created me",
        "Let's put a smile on that face"
    ]
}
def remember(filename = 'QA.json'):
    try:
        #Loads the file 
        with open(filename) as f:
            QA = json.load(f)

        for question in QA["questions"]:
            responses["questions"].append(question)
        for response in QA["response"]:
            responses["response"].append(response)
    except FileNotFoundError:
        #Handles error if the file doesn't exist 
        with open(filename, 'w') as f:
            json.dump(responses, f)
def save(filename = 'QA.json') -> bool: 
    try:
        with open(filename, "w") as f:
            json.dump(responses, f) 
        return True
    except FileNotFoundError:
        return False

def checkResponse(msg):
    msg = msg.lower() 

    output = "not found"
    
    for i, response in enumerate(responses["questions"]):
        if response in msg:
            output = responses["response"][i] 
    
    return output

remember() 
#allows you to input a question
while True:
    message = input("Ask me a question: ")
    output = checkResponse(message)
    #creates a random number
    if message == "generate number":
        min = int(input("Type the minimum value: "))
        max = int(input("Type maximum value: "))

        print("Generated number ", random.randint(min, max))
        #tells the time 
    elif message == "whats the time":
        date = time.localtime(time.time())
        hour = date[3] - 5

        if hour > 12:
            hour -= 12

        hourMinute = str(hour) + ":" + str(date[4])
        print("The current time is: ", hourMinute)
    elif message == "whats the day":
        date = time.localtime(time.time())
        day = date[2]
        dayNumber = str(day) 
        print("The current day is ", dayNumber)
        #saves the file
    elif message == "save":
        if save():
            print("File Saved Correctly")
        else:
            print("File didn't save correctly") 
    else: 
        if output == "not found":
            print(output)
            addQA = input("Do you want me to add this response to my database: ")
            if addQA == "yes":
                respond = input("What is the answer to the question: ")
                responses["questions"].append(message)
                responses["response"].append(respond)

                save() 
        else:
            print(output)

