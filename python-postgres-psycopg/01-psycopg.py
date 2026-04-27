import psycopg

# Connect to an existing database
with psycopg.connect(
    "host=host.docker.internal port=5432 dbname=language_school user=rooter password=manish"
) as conn:
    print("Connection " + conn)
    # Open a cursor to perform database operations
    with conn.cursor() as cur:
        ...
