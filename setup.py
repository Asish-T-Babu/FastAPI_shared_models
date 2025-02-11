from setuptools import setup, find_packages

setup(
    name="base_service",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "SQLAlchemy",
        "alembic",
        "psycopg2-binary",  # Use "sqlite" if testing locally
    ],
)
