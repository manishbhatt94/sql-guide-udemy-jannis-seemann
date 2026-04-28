from typing import List

from sqlalchemy import ForeignKey, Integer, String, create_engine, select
from sqlalchemy.orm import DeclarativeBase, Mapped, Session, mapped_column, relationship


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

    course_id: Mapped[int] = mapped_column(ForeignKey("courses.id"))
    course: Mapped["Course"] = relationship(back_populates="students")

    def __repr__(self) -> str:
        return f"Student(id={self.id!r}, firstname={self.firstname!r}, lastname={self.lastname!r})"


class Course(Base):
    __tablename__ = "courses"
    id: Mapped[int] = mapped_column(primary_key=True)
    language_name: Mapped[str] = mapped_column(String(30))
    language_level: Mapped[int] = mapped_column(Integer)
    description: Mapped[str] = mapped_column(String())

    students: Mapped[List["Student"]] = relationship(back_populates="course")

    def __repr__(self) -> str:
        return f"Course(id={self.id!r}, language_name={self.language_name!r})"


engine = create_engine(
    "postgresql+psycopg://postgres:manish@localhost/language_school2", echo=True
)
with Session(engine) as session:
    stmt = select(Student).where(Student.firstname.in_(["Kimberly", "Deborah"]))
    for student in session.scalars(stmt):
        print(f"\nStudent[id={student.id}] --> {student}")
        print(f"Student[id={student.id}]'s course --> {student.course}\n")
        # Note: Accessing `student.course` above fires a separate SELECT query
        # to get the course record from the courses table for each distinct
        # course_id.
        # So, if our students SELECT query returned 10 student records each
        # having course_id's that happen to be all unique, then due to accessing
        # the student.course property for each of these student records, SQL
        # Alchemy ends up firing 10 separate queries of this form:
        # SELECT..FROM..courses..WHERE..course_id=?.
        # Check this, with: `create_engine(conn_str, echo=True)`
