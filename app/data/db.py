# app/data/db.py
import os
from sqlalchemy import create_engine
from dotenv import load_dotenv

load_dotenv() # Load variables from .env file in the root directory

def get_db_engine():
    """Creates and returns a SQLAlchemy engine for PostgreSQL using DATABASE_URL."""
    database_url = os.getenv("DATABASE_URL")

    if not database_url:
        raise ValueError("DATABASE_URL environment variable is not set in your .env file or environment.")

    # Ensure the URL starts with postgresql:// if using psycopg2 implicitly
    # SQLAlchemy typically infers the driver from the URL scheme
    # If the URL provided by Supabase already includes the driver (like postgresql+psycopg2://), 
    # this check might not be strictly necessary, but it's good practice.
    if not database_url.startswith("postgresql://") and not database_url.startswith("postgresql+psycopg2://"):
        # You might want to adjust this check based on the exact format Supabase provides
        raise ValueError("DATABASE_URL does not seem to be a valid PostgreSQL connection string.")

    # Remove the explicit construction of db_url
    # db_hostname = os.getenv("DB_HOSTNAME")
    # ... other variables ...
    # db_url = f"postgresql+psycopg2://{db_user}:{db_password}@{db_hostname}:{db_port}/{db_name}"
    
    try:
        # Use the full DATABASE_URL directly
        engine = create_engine(database_url)
        # Optional: Test connection immediately to fail fast
        # with engine.connect() as connection:
        #     print("Database connection successful.")
        return engine
    except Exception as e:
        print(f"Error creating database engine from DATABASE_URL: {e}")
        raise

# You could create a default engine instance for convenience if needed,
# but creating it on demand within functions is often safer.
# engine = get_db_engine() 