# Deployment Instructions

## Important Note:
This is a FastAPI Python application with a backend server. Firebase Hosting only supports static websites.

## Options to Deploy:

### Option 1: Deploy to a Python hosting service (Recommended)
- **Render.com** (Free tier available)
- **Railway.app** (Free tier available)
- **PythonAnywhere** (Free tier available)
- **Heroku** (Paid)

### Option 2: Keep it Local
Run the app locally and share the link on your local network:
```bash
cd /Users/basavarajurk/her_birthday
source venv/bin/activate
python3 app.py
```
Then access it at: http://127.0.0.1:8000

### Option 3: Deploy to Render.com (Step by Step)

1. Go to https://render.com and sign up
2. Click "New +" → "Web Service"
3. Connect your GitHub repository: basavaraj-lab/her_birthday
4. Configure:
   - Name: her-birthday
   - Environment: Python 3
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `uvicorn app:app --host 0.0.0.0 --port $PORT`
5. Click "Create Web Service"
6. Wait for deployment (5-10 minutes)
7. You'll get a URL like: https://her-birthday.onrender.com

### Note about Firebase:
The Firebase config you provided is for Firebase services (database, storage, etc.), not for hosting this type of application. You would need to convert the entire app to a static website (no Python backend) to use Firebase Hosting.

## Files Already Prepared:
- ✅ requirements.txt
- ✅ app.py (FastAPI server)
- ✅ static files
- ✅ templates
- ✅ .gitignore (excludes large files)

## To Run Locally:
```bash
cd /Users/basavarajurk/her_birthday
source venv/bin/activate
python3 app.py
```

Access at: http://127.0.0.1:8000
