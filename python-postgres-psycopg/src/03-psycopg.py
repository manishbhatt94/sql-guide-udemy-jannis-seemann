"""Demo of passing named parameters query in cursor.execute().

Use dict instead of list to supply parameter values.
"""

import psycopg


def insert_data():
    student_data = {
        "firstname": "Walter",
        "lastname": "White",
        "course_id": 3,
    }

    # Connect to an existing database
    with psycopg.connect(
        "postgresql://postgres:manish@localhost:5432/language_school"
    ) as conn:
        # Open a cursor to perform database operations
        with conn.cursor() as cur:
            print("Attepting to insert new student record")
            cur.execute(
                "INSERT INTO students_copy (firstname, lastname, course_id) "
                + "VALUES (%(firstname)s, %(lastname)s, %(course_id)s)",
                student_data,
            )
            print(f"Inserted new student record: {student_data}")


if __name__ == "__main__":
    insert_data()
