AI-Powered Smart City Problem Detection & Prediction System

An AI-powered Smart City application developed using Python, Flask, MySQL, HTML, CSS, and JavaScript to detect, manage, and predict common city problems such as traffic, garbage, water, and infrastructure issues.

🚀 Features
🔍 Smart city problem detection
🤖 AI-based problem prediction
📊 Interactive dashboard
🗄️ MySQL database integration
📈 Data visualization and charts
🗺️ City problem monitoring
🚨 Problem alerts
👥 Citizen problem reporting
🔗 Flask REST API
📁 CSV dataset support
🛠️ Technologies Used
Technology	Purpose
Python	Backend programming
Flask	Web framework / API
MySQL	Database
HTML	Web page structure
CSS	Website styling
JavaScript	Frontend functionality
Pandas	Data processing
CSV	Sample datasets
📂 Project Structure
smart-city-ai/
│
├── app.py
│
├── database/
│   └── db.py
│
├── dataset/
│   └── smart_city_data.csv
│
├── templates/
│   └── index.html
│
├── static/
│   ├── css/
│   │   └── style.css
│   │
│   └── js/
│       └── script.js
│
├── screenshots/
│   ├── dashboard.png
│   ├── prediction.png
│   └── reports.png
│
├── requirements.txt
│
└── README.md
⚙️ Installation
1. Clone the repository
git clone YOUR_GITHUB_REPOSITORY_URL
2. Open the project folder
cd smart-city-ai
3. Create a virtual environment
python -m venv venv
4. Activate the virtual environment

Windows:

venv\Scripts\activate
5. Install required packages
pip install -r requirements.txt

If you don't have a requirements.txt file yet:

pip install flask mysql-connector-python pandas
🗄️ MySQL Database Setup
1. Open MySQL

Create a database:

CREATE DATABASE smart_city;
2. Select the database
USE smart_city;
3. Create the required tables

Example:

CREATE TABLE problems (
    id INT AUTO_INCREMENT PRIMARY KEY,
    problem_type VARCHAR(100),
    location VARCHAR(100),
    description TEXT,
    status VARCHAR(50)
);
4. Configure the database connection

Open:

database/db.py

Add your MySQL details:

import mysql.connector

def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="YOUR_PASSWORD",
        database="smart_city"
    )

Replace YOUR_PASSWORD with your MySQL password.

▶️ Run the Flask Application

Start the Flask server:

python app.py

You should see something similar to:

Running on http://127.0.0.1:5000

Open your browser and visit:

http://127.0.0.1:5000
🔗 API Endpoints
Home
GET /

Returns the main application page or Flask status.

Get Problems
GET /problems

Returns city problems stored in the MySQL database.

Example:

http://127.0.0.1:5000/problems

Example response:

[
    {
        "id": 1,
        "problem_type": "Traffic",
        "location": "Hyderabad",
        "description": "Heavy traffic detected",
        "status": "Open"
    }
]
📊 Dashboard

The dashboard provides information about:

🚦 Traffic problems
🗑️ Garbage problems
💧 Water problems
🛣️ Road/infrastructure problems
📈 Problem statistics
🤖 Prediction results
🚨 Alerts
👥 Citizen reports
🖼️ Screenshots
Dashboard

Add your dashboard screenshot here:

![Smart City Dashboard](screenshots/dashboard.png)
Prediction

Add your prediction screenshot here:

![Prediction Dashboard](screenshots/prediction.png)
Citizen Reports

Add your citizen-report screenshot here:

![Citizen Reports](screenshots/reports.png)
🔄 How the System Works
Citizen / City Data
        ↓
     Dataset
        ↓
   Data Processing
        ↓
       Flask
        ↓
   MySQL Database
        ↓
   AI Prediction
        ↓
   Smart Dashboard
        ↓
 Problems / Alerts / Reports
🎯 Project Objective

The main objective of this project is to use AI and data-driven technologies to help identify and predict problems in cities.

The system can help organize city problem data and provide useful information through a centralized dashboard.

🔮 Future Improvements
Real-time IoT sensor integration
Advanced machine learning models
Live traffic data
GPS-based problem detection
Mobile application
Cloud deployment
Real-time notifications
Advanced prediction models
Automated city authority alerts
👨‍💻 Author

Rakesh Koduru

B.Tech Computer Science Engineering

Interested in:

Data Engineering
Python
SQL
Data Processing
Backend Development
AI & Machine Learning
