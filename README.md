# SQL Guide: Code-Along repository

Course: "Learn SQL: The Hands-on Guide with interactive exercises"

Link: https://www.udemy.com/course/sql-guide/

Author: Jannis Seemann

---

### Backup & Restore of a PostgreSQL Database

#### Backup using `pg_dump`

Backing up to Plain Text (.sql file) format. This is alright for small size
databases.

```bash
# Syntax:
# pg_dump -U [username] -h [host] -p 5432 -W [database_name] > backup_file.sql

# -W --> Prompts for password

pg_dump -U postgres -h localhost -p 5432 -W language_school > db_language_school_bkp.sql
```

#### Restore to new database using `psql`

> First, create the new database:
>
> ```sql
> CREATE DATABASE language_school2;
> ```

To restore a plain-text SQL file, use the `psql` utility.

This executes the SQL commands inside the file (specified using the `-f` flag)
against your new database.

```bash
# Syntax:
# psql -U [username] -d [new_database_name] -f backup_file.sql

psql -U postgres -h localhost -p 5432 -W language_school2 -f db_language_school_bkp.sql
```

Note:
- `-d [new_database_name]`: Specifies the target database.
- `-f backup_file.sql`: Tells psql to read commands from the file.
