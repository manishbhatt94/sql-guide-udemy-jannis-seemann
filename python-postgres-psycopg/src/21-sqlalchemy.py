from sqlalchemy import Integer, String, create_engine, select
from sqlalchemy.orm import DeclarativeBase, Mapped, Session, mapped_column


class Base(DeclarativeBase):
    pass


class Student(Base):
    __tablename__ = "students_copy"
    id: Mapped[int] = mapped_column(primary_key=True)
    firstname: Mapped[str] = mapped_column(String(30))
    lastname: Mapped[str] = mapped_column(String(30))
    email: Mapped[str] = mapped_column(String(30))
    age: Mapped[int] = mapped_column(Integer())
    payment_status: Mapped[str] = mapped_column(String(30))

    def __repr__(self) -> str:
        return f"Student(id={self.id!r}, firstname={self.firstname!r}, lastname={self.lastname!r})"


engine = create_engine(
    "postgresql+psycopg://postgres:manish@localhost/language_school2", echo=True
)
with Session(engine) as session:
    # print("Fetch all students:")
    # # Below line equivalent to: "SELECT * FROM students;"
    # stmt = select(Student)
    # print()

    print("Fetch students whose firstname is one of ('Kimberly', 'Deborah'):")
    # Below line equivalent to: "SELECT * FROM students WHERE firstname IN ('Kimberly', 'Deborah');"
    stmt = select(Student).where(Student.firstname.in_(["Kimberly", "Deborah"]))
    print()

    print("Print fetched students:")
    for student in session.scalars(stmt):
        print(student)


# Note the logs printed by SQLAlchemy for the WHERE..firstname..IN query:
# i.e. for:
# stmt = select(Student).where(Student.firstname.in_(["Kimberly", "Deborah"]))

# Note that, the generated query is properly parameterized & safe from SQL Injection.

# SQLAlchemy generated logs:

# 2026-04-28 13:36:50,214 INFO sqlalchemy.engine.Engine SELECT students_copy.id, students_copy.firstname, students_copy.lastname, students_copy.email, students_copy.age, students_copy.payment_status
# FROM students_copy
# WHERE students_copy.firstname IN (%(firstname_1_1)s::VARCHAR, %(firstname_1_2)s::VARCHAR)
# 2026-04-28 13:36:50,215 INFO sqlalchemy.engine.Engine [generated in 0.00042s] {'firstname_1_1': 'Kimberly', 'firstname_1_2': 'Deborah'}
