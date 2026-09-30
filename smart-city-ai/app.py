from flask import Flask, jsonify, request
from database.db import get_db_connection, init_db

app = Flask(__name__)


@app.route("/")
def home():
    return "Smart City Flask is running!"


@app.route("/problems")
def problems():
    try:
        connection = get_db_connection()
        cursor = connection.cursor(dictionary=True)

        cursor.execute("SELECT * FROM problems")
        data = cursor.fetchall()

        cursor.close()
        connection.close()

        return jsonify(data)

    except Exception as e:
        return jsonify({
            "error": str(e)
        }), 500


@app.route("/predictions")
def predictions():
    try:
        connection = get_db_connection()
        cursor = connection.cursor(dictionary=True)

        cursor.execute("SELECT * FROM predictions")
        data = cursor.fetchall()

        cursor.close()
        connection.close()

        return jsonify(data)

    except Exception as e:
        return jsonify({
            "error": str(e)
        }), 500


@app.route("/citizen_reports", methods=["GET"])
def citizen_reports():
    try:
        connection = get_db_connection()
        cursor = connection.cursor(dictionary=True)

        cursor.execute("SELECT * FROM citizen_reports")
        data = cursor.fetchall()

        cursor.close()
        connection.close()

        return jsonify(data)

    except Exception as e:
        return jsonify({
            "error": str(e)
        }), 500


@app.route("/citizen_reports", methods=["POST"])
def add_citizen_report():
    try:
        payload = request.get_json()

        location = payload.get("location")
        problem_type = payload.get("problem_type")
        priority = payload.get("priority")
        description = payload.get("description")

        if not location or not problem_type:
            return jsonify({
                "error": "location and problem_type are required"
            }), 400

        connection = get_db_connection()
        cursor = connection.cursor()

        cursor.execute(
            """
            INSERT INTO citizen_reports (location, problem_type, priority, description)
            VALUES (%s, %s, %s, %s)
            """,
            (location, problem_type, priority, description)
        )
        connection.commit()

        new_id = cursor.lastrowid

        cursor.close()
        connection.close()

        return jsonify({
            "message": "Report submitted successfully",
            "id": new_id
        }), 201

    except Exception as e:
        return jsonify({
            "error": str(e)
        }), 500


if __name__ == "__main__":
    # Automatically creates the database, tables, and sample data
    # (only if they don't already exist) every time the app starts.
    init_db()
    app.run(debug=True)

