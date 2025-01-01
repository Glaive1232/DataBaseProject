from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_URL = "postgresql+pg8000://pguser:pwd123@localhost:8082/construction"

# Create the engine and session
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def check_connection():
    try:
        # Attempt to connect
        with engine.connect() as connection:
            print("Database connection successful!")
    except Exception as e:
        print(f"Failed to connect to the database: {e}")

if __name__ == "__main__":
    check_connection()
