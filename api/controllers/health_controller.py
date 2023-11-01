from flask import jsonify
from flask_cors import cross_origin
import config

@cross_origin()
def index() -> dict:
    """Simple healthcheck with uptime info"""
    try:
        conn = config.get_db()
        if conn is None:
            raise Exception("Database connection failed!")
    except Exception as db_connection_error:
        print(f"ERROR: Database connection failed: {db_connection_error}")
        return jsonify(
            {'status': 'ERROR', 'message': 'Database connection failed'}
        ), 500

    try:
        cursor = conn.cursor()
        query = "show global status like 'Uptime'"
        cursor.execute(query)
        results = cursor.fetchall()
        cursor.close()
        conn.close()
        return {'status': 'OK', 'uptime': int(results[0][1])}
    except Exception as e:
        print(f"ERROR: Error during database operation: {e}")
        if cursor:
            cursor.close()
        if conn:
            conn.close()
        return jsonify(
            {'status': 'ERROR', 'message': 'Error during database operation'}
        ), 500
