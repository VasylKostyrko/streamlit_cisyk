from sqlalchemy import text


def do_query(engine, sql_string):
    with engine.connect() as conn:
        result = conn.execute(text(sql_string)).fetchall()
        return result