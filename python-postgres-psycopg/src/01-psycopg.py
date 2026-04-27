import psycopg

# Connect to an existing database
with psycopg.connect(
    "host=localhost port=5432 dbname=language_school user=postgres password=manish"
) as conn:
    print(f"Connection: {conn}")
    # Open a cursor to perform database operations
    with conn.cursor() as cur:
        ...
