# loading packages
from sqlalchemy import create_engine, inspect, Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
import os
from dotenv import load_dotenv

# Load environment variables from a .env file
load_dotenv()

# Database connection settings from environment variables
DB_HOST = os.getenv("DB_HOST")
DB_DATABASE = os.getenv("DB_DATABASE")
DB_USERNAME = os.getenv("DB_USERNAME")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_PORT = int(os.getenv("DB_PORT", 3306))
DB_CHARSET = os.getenv("DB_CHARSET", "utf8mb4")

# Define the base class for declarative models
Base = declarative_base()

# Define the Patient and AllergyTest models
class Patient(Base):
    __tablename__ = 'patients'

    id = Column(Integer, primary_key=True)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    date_of_birth = Column(Date, nullable=False)
    gender = Column(String(10), nullable=False)

    # Establish a relationship with the AllergyTest model
    allergytests = relationship('AllergyTest', back_populates='patient')

class AllergyTest(Base):
    __tablename__ = 'allergy_tests'

    id = Column(Integer, primary_key=True)
    patient_id = Column(Integer, ForeignKey('patients.id'), nullable=False)
    test_name = Column(String(100), nullable=False)
    test_result = Column(String(100), nullable=False)
    test_date = Column(Date, nullable=False)

    # Establish a relationship with the Patient model
    patient = relationship('Patient', back_populates='allergytests')

# Part 2 - Create the database connection and engine
connect_args = {'ssl': {'fake_flag_to_enable_tls': True}}
connection_string = f'mysql+pymysql://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_DATABASE}?charset={DB_CHARSET}'

# Create the SQLAlchemy engine
engine = create_engine(
    connection_string,
    connect_args=connect_args
)

# Test the database connection
inspector = inspect(engine)
table_names = inspector.get_table_names()
print("Tables in the database:", table_names)

# Part 3 - Create the tables using the defined models
Base.metadata.create_all(engine)

print("Tables created successfully.")

### Running migrations 
""" these steps are then performed in the termainl, outside of your python code

1. alembic init migrations
` alembic init migrations `

2. edit alembic.ini to point to your database
` sqlalchemy.url = mysql+mysqlconnector://username:password@host/database_name `

3. edit env.py to point to your models
`from db_schema import Base`
`target_metadata = Base.metadata `

4. create a migration
` alembic revision --autogenerate -m "create tables" `

5. run the migration
` alembic upgrade head `

in addition, you can run ` alembic history ` to see the history of migrations
or you can run with the --sql flag to see the raw SQL that will be executed

so it could be like:
` alembic upgrade head --sql `

or if you then want to save it:
` alembic upgrade head --sql > migration.sql `

6. check the database

7. roll back: To roll back a migration in Alembic, you can use the downgrade command. 
The downgrade command allows you to revert the database schema to a previous 
migration version. Here's how you can use it:

`alembic downgrade <target_revision>` 

or if you want to roll back to the previous version, you can use the -1 flag:
`alembic downgrade -1`
 

"""