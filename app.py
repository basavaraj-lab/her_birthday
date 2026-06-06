from fastapi import FastAPI, Request, HTTPException, UploadFile, File, Form
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
import uvicorn
import json
from pathlib import Path
from typing import Optional

app = FastAPI(title="Birthday Treasure Box")

# Configure templates and static files
templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")

# SECURITY: Answers are securely stored on the backend, 
# ensuring they cannot be seen by simply inspecting the webpage source code.
QUIZ_DATA = {
    0: {
        "answer": "BUs stand", # Set correct answer for Q1
        "hint": "Hint: Think about where we had our first date..."
    },
    1: {
        "answer": "pink", # Set correct answer for Q2
        "hint": "Hint: It's something you do to flowers, and also to my heart when you smile..."
    },
    2: {
        "answer": "chinnu", # Set correct answer for Q3
        "hint": "Hint: Sweet like a bee's creation..."
    },
    3: {
        "answer": "Husharu", # Set correct answer for Q4
        "hint": "Hint: Its something I say to you in every ending conversation..."
    },
    4: {
        "answer": "🤍", # Set correct answer for Q5
        "hint": "Hint: It's a symbol of pure love, just like how I feel about you every day..."
    }
    


}

REWARDS = {
    0: "🤗 Unlimited Hug Coupon",
    1: "🍫 Chocolate Treat",
    2: "🎬 Movie Date Coupon",
    3: "💌 Love Letter",
    4: "⭐ Special Surprise"
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

        if user_answer == correct_answer:
            return {"correct": True, "reward": REWARDS.get(question_index, "🎉 Well done!")}
        else:
            return {"correct": False, "hint": QUIZ_DATA[question_index]['hint']}
    
#scratch card 

            
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

@app.post("/save_today_memory")
async def save_today_memory(
    message: Optional[str] = Form(None),
    image: Optional[UploadFile] = File(None)
):
    try:
        data = {}
        
        if message:
            data['message'] = message
        
        if image:
            # Save the uploaded image
            image_path = Path("static/images/today_memory.jpg")
            with open(image_path, "wb") as f:
                content = await image.read()
                f.write(content)
            data['image_url'] = "/static/images/today_memory.jpg"
        
        # Save to JSON file
        json_path = Path("static/today_memory.json")
        with open(json_path, "w") as f:
            json.dump(data, f)
        
        return {"success": True, **data}
    except Exception as e:
        print(f"Error saving memory: {e}")
        raise HTTPException(status_code=500, detail="Failed to save memory")

@app.get("/get_today_memory")
async def get_today_memory():
    try:
        json_path = Path("static/today_memory.json")
        if json_path.exists():
            with open(json_path, "r") as f:
                data = json.load(f)
            return data
        return {"message": None, "image_url": None}
    except Exception as e:
        return {"message": None, "image_url": None}

@app.post("/remove_today_memory")
async def remove_today_memory():
    try:
        # Remove JSON file
        json_path = Path("static/today_memory.json")
        if json_path.exists():
            json_path.unlink()
        
        # Remove image file
        image_path = Path("static/images/today_memory.jpg")
        if image_path.exists():
            image_path.unlink()
        
        return {"success": True}
    except Exception as e:
        print(f"Error removing memory: {e}")
        raise HTTPException(status_code=500, detail="Failed to remove memory")

if __name__ == '__main__':
    # Start the secure backend server
    print("Starting the secure Birthday Box server. Go to http://127.0.0.1:8000")
    uvicorn.run("app:app", host="127.0.0.1", port=8000, reload=True)
