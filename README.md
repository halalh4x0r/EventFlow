# EventFlow — Full Stack Event Planner App

EventFlow is a full-stack event planning platform built using **React (frontend)** and **Flask (backend)**.  
Users can create events, RSVP to events, comment on events, and manage their own listings.

This project is built by **Group 2**.

---

# Tech Stack

## Frontend
- React (Vite)
- React Router
- Formik + Yup for form validation
- Context API for authentication state

## Backend
- Flask
- SQLAlchemy ORM
- Flask-Migrate
- Flask-Bcrypt
- JWT-based authentication

## Database
- SQLite (dev)
- PostgreSQL (production)

---

# Main Features

###  User & Auth
- User registration & login
- JWT-based authentication
- Profile view
- Optional roles: user, organizer, admin

### Events
- Create an event
- View all events
- View single event details
- Update or delete your own events
- Upload image URL (optional)

### RSVPs
- RSVP to an event
- Prevent duplicate RSVP
- Prevent RSVP if event is full (optional)
- Organizer can view attendee list

### Comments (optional feature)
- Add comments to events
- View comments under event details

---

# Project Structure
EventFlow/
│
├── backend/
│   ├── app.py
│   ├── config.py
│   ├── requirements.txt
│   │
│   ├── models/
│   │   ├── __init__.py
│   │   ├── user.py
│   │   ├── event.py
│   │   ├── rsvp.py
│   │   └── comment.py
│   │
│   ├── routes/
│   │   ├── __init__.py
│   │   ├── auth_routes.py
│   │   ├── event_routes.py
│   │   ├── rsvp_routes.py
│   │   └── comment_routes.py
│   │
│   ├── utils/
│   │   ├── auth.py
│   │   └── validators.py
│   │
│   └── migrations/
│
├── frontend/
│   ├── package.json
│   ├── vite.config.js
│   │
│   ├── src/
│   │   ├── App.jsx
│   │   ├── main.jsx
│   │   │
│   │   ├── components/
│   │   │   ├── NavBar.jsx
│   │   │   ├── EventCard.jsx
│   │   │   ├── EventForm.jsx
│   │   │   ├── LoginForm.jsx
│   │   │   ├── RegisterForm.jsx
│   │   │   └── CommentList.jsx
│   │   │
│   │   ├── pages/
│   │   │   ├── Home.jsx
│   │   │   ├── EventDetails.jsx
│   │   │   ├── CreateEvent.jsx
│   │   │   └── Profile.jsx
│   │   │
│   │   ├── context/
│   │   │   └── AuthContext.jsx
│   │   │
│   │   └── styles/
│   │       └── global.css
│   │
│   └── public/
│       └── index.html
│
└── README.md

Backend and frontend live inside one monorepo for easier development and deployment.

---

# ⚙ Backend Setup

### 1. Navigate to backend
cd backend


### 2. Install dependencies


pip install -r requirements.txt


### 3. Run migrations


flask db upgrade


### 4. Start server


flask run


---

# 🖥 Frontend Setup

### 1. Navigate to frontend


cd frontend


### 2. Install dependencies


npm install


### 3. Start development server


npm run dev


---

# Connecting Frontend to Backend

Inside `frontend/src/config.js`


export const API_URL = "http://localhost:5000
";


All fetch calls use:


fetch(${API_URL}/events)


---

#  Deployment (Render)

- Deploy backend as a **Web Service**
- Deploy frontend as a **Static Site**
- Enable CORS on Flask backend
- Use a PostgreSQL DB on Render

---

# Team Roles

### **Team A — Frontend**
- Component creation
- Pages & routes
- Formik validation
- Fetch integration
- UI/UX design

### **Team B — Backend**
- API models & relationships
- Authentication
- CRUD routes
- Validations
- Deployment setup

---

#  License
MIT License


