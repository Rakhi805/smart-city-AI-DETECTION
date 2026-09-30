# AI-Powered Smart City Problem Detection & Prediction System

## Run
1. Install Python and MySQL.
2. Create database: run `database/smart_city.sql` in MySQL.
3. In `database/db.py`, replace `YOUR_MYSQL_PASSWORD` with your MySQL password.
4. Open terminal in this folder.
5. `python -m venv venv`
6. Windows: `venv\\Scripts\\activate` / Linux/macOS: `source venv/bin/activate`
7. `pip install -r requirements.txt`
8. `python app.py`
9. Open http://127.0.0.1:5000

## Structure
- Frontend: templates/, static/
- Backend: app.py
- Database: database/
- Data: data/
- AI/ML: ml/, models/
