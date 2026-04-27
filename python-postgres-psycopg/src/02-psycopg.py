import psycopg

french_level2_courseid = 7


def fetch_data():
    # Connect to an existing database
    with psycopg.connect(
        "postgresql://postgres:manish@localhost:5432/language_school"
    ) as conn:
        # Open a cursor to perform database operations
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM students")

            print("Table: students. Operation: fetchone()")
            # fetchone() - fetches one record
            print(cur.fetchone(), end="\n\n")

            print("Table: students. Operation: fetchmany(5)")
            # fetchmany(N) - fetches next N (=5) records
            print(cur.fetchmany(5), end="\n\n")

            print("Table: teachers. Operation: fetchall()")
            # fetchall() - fetches all records
            teachers = cur.execute("SELECT * FROM teachers").fetchall()
            print(teachers, end="\n\n")

            print(
                "Table: students. Operation: fetchall(). WHERE clause & Query"
                r" Params usage (%s). "
            )
            # Filter Query (with WHERE) & Dynamic Query Parameters with %s:
            french_students = cur.execute(
                "SELECT * FROM students WHERE course_id = %s", [french_level2_courseid]
            ).fetchall()
            print(french_students)


def insert_data():
    with psycopg.connect(
        "postgresql://postgres:manish@localhost:5432/language_school"
    ) as conn:
        with conn.cursor() as cur:
            print("Inserting a data record in students_copy table")
            cur.execute(
                "INSERT INTO students_copy (firstname, lastname, course_id) VALUES (%s, %s, %s)",
                ["Barack", "Obama", french_level2_courseid],
            )


if __name__ == "__main__":
    fetch_data()
    insert_data()
