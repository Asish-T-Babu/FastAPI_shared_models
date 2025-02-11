import os

DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://postgres:password@localhost/two_in_one_repo")
