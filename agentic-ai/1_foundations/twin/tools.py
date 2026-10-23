import json
import os
import requests
from dotenv import load_dotenv

load_dotenv(override=True)

pushover_user= os.getenv("PUSHOVER_USER")
pushover_token= os.getenv("PUSHOVER_TOKEN")
pushover_url= "https://api.pushover.net/1/messages.json"

# if pushover_user:
#     if pushover_user.startswith("u"):
#         print("Pushover User Key is set correctly.")
#     else:
#         print("Pushover user key is found but not correct")
# else:
#     print("Pushover key is not found")


# if pushover_token:
#     if pushover_token.startswith("a"):
#         print("Pushover Token is set correctly.")
#     else:
#         print("Pushover token is found but not correct")
# else:
#     print("Pushover token is not found")    


def push(message):
    payload = { "user": pushover_user, "token": pushover_token, "message": message }
    requests.post(pushover_url, data=payload)


def record_user_details(email, name="not provided", phone="not provided", note="not provided"):
    push(f"User Details: Email: {email}, Name: {name}, Phone: {phone}, Note: {note}")
    return "OK"


def record_unknown_questions(question):
    push(f"Recording {question} asked that I couldn't answer")
    return "OK"



record_user_details_json={

    "name":"record_user_details",
    "description":"Records user details and sends a notification via Pushover",
    "parameters":{
        "type":"object",
        "properties":{
            "email":{   
                    "type":"string",
                    "description":"The email address of the user"
                 },
            "name":{
                
                    "type":"string",
                    "description":"The name of the user"
                 },
            "phone":{
                    "type":"string",
                    "description":"The phone number of the user"
                 },
            "note":{
                    "type":"string",
                    "description":"Any additional notes about the user"
                 }
            },
            "required": ["email"]
        }
} 



record_unknown_questions_json={
    "name":"record_unknown_questions",
    "description":"Records questions that the AI couldn't answer and sends a notification via Pushover",
    "parameters":{
        "type":"object",
        "properties":{
            "question":{
                "type":"string",
                "description":"The question that the AI couldn't answer"
            }
        },
        "required": ["question"]
    }
}


tools=[{"type":"function",  "function":record_user_details_json},
       {"type":"function", "function":record_unknown_questions_json}
      ]


tool_map = {
    "record_user_details": record_user_details,
    "record_unknown_questions": record_unknown_questions,
}


def handle_tool_calls_manual_if(tool_calls):
    results=[]
    for tool_call in tool_calls:
        tool_name= tool_call.function.name
        argument= json.loads(tool_call.function.arguments)
        print(f"Tool called: {tool_name}", flush=True)
        tool = tool_map.get(tool_name)
        result = tool(**argument) if tool else "Unknown tool: " + tool_name
        results.append({"role":"tool", "content": json.dumps(result),"tool_call_id":tool_call.id})

    return results

