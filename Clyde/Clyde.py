import time
import datetime
import random
import math


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
        "No I am a chat bot like a dumber cleverbot",
        "ecdthegreat and pastaboy844 created me",
        "Let's put a smile on that face"
    ]
}

def checkResponse(msg):
    msg = msg.lower() 

    output = "not found"
    
    for i, response in enumerate(responses["questions"]):
        if response in msg:
            output = responses["response"][i] 
    
    return output

while True:
    message = input("Ask me a question: ")
    output = checkResponse(message)

    if message == "generate number":
        min = int(input("Type the minimum value: "))
        max = int(input("Type maximum value: "))

        print("Generated number ", random.randint(min, max)) 
    elif message == "whats the time":
        date = time.localtime(time.time())
        hour = date[3] - 4

        if hour > 12:
            hour -= 12

        hourMinute = str(hour) + ":" + str(date[4])
        print("The current time is: ", hourMinute)
    elif message == "whats the day":
        date = time.localtime(time.time())
        day = date[2]
        dayNumber = str(day) 
        print("The current day is ", dayNumber)
    else: 
        if output == "not found":
            print(output)
            addQA = input("Do you want me to add this response to my database: ")
            if addQA == "yes":
                respond = input("What is the answer to the question: ")
                responses["questions"].append(message)
                responses["response"].append(respond)
        else:
            print(output)
    
