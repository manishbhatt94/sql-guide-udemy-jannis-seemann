# Using PostgreSQL from Python

## Modern Setup: Using `uv` (Recommended)

#### Create a directory for working

```bash
mkdir python-postgres-psycopg
cd python-postgres-psycopg
```

#### Intialize a `uv` "lib" project

```bash
uv init --lib  # --lib prevents it from creating a default 'main.py'
```

This will create a `pyproject.toml` file (among others) in this directory.


Remove the unnecessary 'src' folder, and add this to `pyproject.toml`:
```toml
[tool.uv]
package = false
```

This will allow us to tell 'uv' not to treat this project as a package, but just
as a bunch of stand-alone scripts.

#### Add dependencies

Install [psycopg](https://pypi.org/project/psycopg/) using:

```bash
# Install `psycopg`:
uv add "psycopg[binary,pool]"

# Install `SQLAlchemy`:
uv add SQLAlchemy
```

This creates (if not already present) a package lockfile `uv.lock`, and also
mentions the package just added in the `pyproject.toml` file.

**Confirm packages installed with `uv tree`:**

```bash
uv tree

 python-postgres-psycopg  uv tree
Resolved 8 packages in 1ms
python-postgres-psycopg v0.1.0
├── psycopg[binary, pool] v3.3.3
│   ├── tzdata v2026.2
│   ├── psycopg-binary v3.3.3 (extra: binary)
│   └── psycopg-pool v3.3.0 (extra: pool)
│       └── typing-extensions v4.15.0
└── sqlalchemy v2.0.49
    ├── greenlet v3.5.0
    └── typing-extensions v4.15.0
```


#### Run a script

Use `uv run` as:

```bash
uv run 01-psycopg.py
```

## Legacy: Using `pip` & `venv` manually

Create new Virtual Environment:

```bash
python3 -m venv ./.venv
```

Activate the virtual environment:

```bash
source .venv/bin/activate
```

After this, we can install Python packages using "pip".

## Using `psycopg`

Package Documentation: https://www.psycopg.org/psycopg3/

Install using PIP:

```bash
pip install "psycopg[binary,pool]"
```

Then run `pip freeze` to mention dependencies in a .txt file:

```bash
pip freeze > requirements.txt
```
