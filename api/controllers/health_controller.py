from flask_cors import cross_origin
import config

@cross_origin()
def index() -> dict:
    """Simple healthcheck with uptime info"""
    conn = config.get_db()
    cursor = conn.cursor()
    query = "show global status like 'Uptime'"
    cursor.execute(query)
    results = cursor.fetchall()
    cursor.close()
    conn.close()
    try:
        return {'status': 'OK', 'uptime': int(results[0][1])}
    except Exception:
        return {'status': 'OK'}
