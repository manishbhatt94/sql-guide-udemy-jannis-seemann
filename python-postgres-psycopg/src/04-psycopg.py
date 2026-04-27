"""Demo for SQL injection if directly using user input in query string"""

import psycopg

# Enter the string: "1' OR 'abc' = 'abc" (without double quotes)
# OR this:
# "1234'; DELETE FROM students_copy; SELECT * FROM students WHERE id = '1234"
student_id = input("Enter student_id to query: ")
print(f"Received this student_id from user input: [{student_id}]")

with psycopg.connect(
    "postgresql://postgres:manish@localhost:5432/language_school"
) as conn:
    with conn.cursor() as cur:
        print("Executing below query:")
        print("SELECT * FROM students WHERE id = '" + student_id + "'")

        # Vulnerable to SQL Injection Attack:
        # students = cur.execute(
        #     "SELECT * FROM students WHERE id = '" + student_id + "'"
        # ).fetchall()
        # print(students)

        # Safe from SQL Injection Attack:
        students = cur.execute(
            "SELECT * FROM students WHERE firstname = %s", [student_id]
        ).fetchall()
        print(students)
