import psycopg2

def connect_to_db():
    with psycopg2.connect() as conn:
        with conn.cursor() as cur:
            pass