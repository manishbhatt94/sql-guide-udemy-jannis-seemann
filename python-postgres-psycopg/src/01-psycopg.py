import psycopg


def connection_str_format_keyword_value():
    """Connect using the Keyword/Value format of Database Connection String, as
    supported by libpq Postgres C Library.

    See: https://www.postgresql.org/docs/current/libpq-connect.html#LIBPQ-CONNSTRING-KEYWORD-VALUE

    Example(s):

        "host=localhost port=5432 dbname=mydb connect_timeout=10"
    """
    # Connect to an existing database
    with psycopg.connect(
        "host=localhost port=5432 dbname=language_school user=postgres password=manish"
    ) as conn:
        print(f"Connection: {conn}")
        # Open a cursor to perform database operations
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM students")
            print(cur.fetchone())


def connection_str_format_connection_uri():
    """Connect using the Keyword/Value format of Database Connection String, as
    supported by libpq Postgres C Library.

    See: https://www.postgresql.org/docs/current/libpq-connect.html#LIBPQ-CONNSTRING-URIS

    Examples:
        The URI scheme designator can be either postgresql:// or postgres://.

        postgresql://
        postgresql://localhost
        postgresql://localhost:5433
        postgresql://localhost/mydb
        postgresql://user@localhost
        postgresql://user:secret@localhost
        postgresql://other@localhost/otherdb?connect_timeout=10&application_name=myapp
        postgresql://host1:123,host2:456/somedb?target_session_attrs=any&application_name=myapp
    """
    # Connect to an existing database
    with psycopg.connect(
        "postgresql://postgres:manish@localhost:5432/language_school"
    ) as conn:
        print(f"Connection: {conn}")
        # Open a cursor to perform database operations
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM students")
            print(cur.fetchone())


if __name__ == "__main__":
    connection_str_format_keyword_value()
    connection_str_format_connection_uri()
