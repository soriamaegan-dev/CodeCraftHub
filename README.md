# 📚 CodeCraftHub — Personalized Learning Platform for Developers

A full-stack learning management system built with Python Flask and a 
responsive HTML dashboard. Developers can track courses they want to 
learn with full CRUD functionality.

## 🌐 Live Demo
👉https://soriamaegan-dev.github.io/CodeCraftHub/dashboard.html

## 📖 About
CodeCraftHub is a REST API-based learning platform that allows developers
to manage their learning journey by tracking courses, completion dates,
and progress status — all stored in a simple JSON file with no database
required.

## 🚀 Features
- ✅ Full CRUD — Create, Read, Update, Delete courses
- ✅ JSON file storage — no database needed
- ✅ Input validation with helpful error messages
- ✅ CORS enabled for browser-based frontend
- ✅ Auto-generated course IDs and timestamps
- ✅ Status tracking — Not Started, In Progress, Completed
- ✅ Beautiful dashboard UI with stats overview
- ✅ Responsive design for mobile and desktop

## 🛠️ Tech Stack
- **Backend**: Python, Flask, Flask-CORS
- **Storage**: JSON file
- **Frontend**: HTML, CSS, JavaScript
- **Tools**: curl, Git

## 📁 Project Structure
```
CodeCraftHub/
├── app.py              # Flask REST API with all CRUD endpoints
├── courses.json        # JSON file for storing course data
├── requirements.txt    # Python dependencies
├── dashboard.html      # Full CRUD dashboard UI
└── README.md          # Project documentation
```

## 🔌 API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/courses` | Get all courses |
| GET | `/api/courses/<id>` | Get one course by ID |
| POST | `/api/courses` | Create a new course |
| PUT | `/api/courses/<id>` | Update an existing course |
| DELETE | `/api/courses/<id>` | Delete a course |

## 📋 Course Data Format
```json
{
  "id": 1,
  "name": "Python for Beginners",
  "description": "Learn Python from scratch",
  "target_date": "2026-06-01",
  "status": "Not Started",
  "created_at": "2026-03-21 10:00:00"
}
```

## ⚙️ Installation & Setup

### Step 1 — Clone the repo
```bash
git clone https://github.com/soriamaegan-dev/CodeCraftHub
cd CodeCraftHub
```

### Step 2 — Create virtual environment
```bash
python3 -m venv my_env
source my_env/bin/activate  # Mac/Linux
my_env\Scripts\activate     # Windows
```

### Step 3 — Install dependencies
```bash
pip install -r requirements.txt
```

### Step 4 — Run the server
```bash
python3 app.py
```

### Step 5 — Open the dashboard
Open `dashboard.html` in your browser while the server is running.

## 🧪 Testing the API

### Create a course
```bash
curl -X POST http://localhost:8080/api/courses \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Python Basics",
    "description": "Learn Python fundamentals",
    "target_date": "2026-06-01",
    "status": "Not Started"
  }'
```

### Get all courses
```bash
curl http://localhost:8080/api/courses
```

### Get one course
```bash
curl http://localhost:8080/api/courses/1
```

### Update a course
```bash
curl -X PUT http://localhost:8080/api/courses/1 \
  -H "Content-Type: application/json" \
  -d '{"status": "In Progress"}'
```

### Delete a course
```bash
curl -X DELETE http://localhost:8080/api/courses/1
```

## ❌ Error Handling

| Error | Status Code | Message |
|-------|-------------|---------|
| Missing field | 400 | "Course name is required" |
| Invalid status | 400 | "Invalid status. Must be one of: ..." |
| Invalid date | 400 | "Invalid date format. Use YYYY-MM-DD" |
| Not found | 404 | "Course with ID X not found" |
| Server error | 500 | "Failed to create course: ..." |

## 🔧 Troubleshooting

**Port already in use:**
```bash
pkill -f "python3 app.py"
python3 app.py
```

**On macOS port 5000 blocked:**
- Go to System Preferences → General → AirDrop & Handoff
- Turn off AirPlay Receiver
- Or change port to 8080 in app.py

**Module not found:**
```bash
source my_env/bin/activate
pip install -r requirements.txt
```

**courses.json corrupted:**
```bash
echo "[]" > courses.json
```

## 📚 What I Learned
- How to build a REST API with Python and Flask
- How to implement full CRUD operations
- How to store and retrieve data from a JSON file
- How to enable CORS for browser-based frontends
- How to validate API inputs and handle errors
- How to build a frontend dashboard with HTML/CSS/JavaScript
- How to use AI tools to accelerate development

## 🎓 Built As Part Of
IBM AI Developer Professional Certificate — Coursera
Final Project: CodeCraftHub Learning Management System
