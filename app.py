from fastapi import FastAPI, Request, HTTPException
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
import uvicorn

app = FastAPI(title="Birthday Treasure Box")

# Configure templates directory
templates = Jinja2Templates(directory="templates")

# SECURITY: Answers are securely stored on the backend, 
# ensuring they cannot be seen by simply inspecting the webpage source code.
QUIZ_DATA = {
    0: {
        "answer": "school", # Set correct answer for Q1
        "hint": "Hint: It was a special place starting with 's'..."
    },
    1: {
        "answer": "red", # Set correct answer for Q2
        "hint": "Hint: Look at the main theme of this page..."
    },
    2: {
        "answer": "chinnu", # Set correct answer for Q3
        "hint": "Hint: Sweet like a bee's creation..."
    }
}

class AnswerRequest(BaseModel):
    question_index: int
    answer: str

@app.get("/")
async def home(request: Request):
    # Render the aesthetic HTML frontend
    return templates.TemplateResponse(request=request, name="index.html")

@app.post("/verify")
async def verify_answer(data: AnswerRequest):
    question_index = data.question_index
    user_answer = data.answer.strip().lower()
    
    if question_index in QUIZ_DATA:
        correct_answer = QUIZ_DATA[question_index]['answer'].lower()
        
        # Verify the answer accurately
        if user_answer == correct_answer:
            return {"correct": True}
        else:
            return {"correct": False, "hint": QUIZ_DATA[question_index]['hint']}
            
    raise HTTPException(status_code=400, detail="Invalid request")

@app.post("/blow_candles")
async def blow_candles():
    # Demonstrating "using the python" to handle logic/state transitions 
    # Just a simple acknowledgment from the backend. 
    return {"message": "Candles blown out successfully!"}

@app.post("/cut_cake")
async def cut_cake():
    # Secure Python backend handling the cake cutting event!
    return {"message": "Cake sliced successfully! The gift is ready to be unlocked."}

if __name__ == '__main__':
    # Start the secure backend server
    print("Starting the secure Birthday Box server. Go to http://127.0.0.1:8000")
    uvicorn.run("app:app", host="127.0.0.1", port=8000, reload=True)
