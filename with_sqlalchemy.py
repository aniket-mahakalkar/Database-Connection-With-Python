from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker

# Set up the engine
engine = create_engine("sqlite:///users.db", echo=True)  # use MySQL with 'mysql+pymysql://user:password@localhost/dbname'

# Base class
Base = declarative_base()

# Define a table as a class
class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)

    def __repr__(self):
        return f"<User(name={self.name}, age={self.age})>"

# Create tables
Base.metadata.create_all(engine)

# Create session
Session = sessionmaker(bind=engine)
session = Session()


new_user = User(name="Aniket", age=21)
session.add(new_user)
session.commit()

# Get all users
users = session.query(User).all()
for user in users:
    print(user)

# Filter specific users
young_users = session.query(User).filter(User.age < 30).all()


user = session.query(User).filter_by(name="Aniket").first()
user.age = 30
session.commit()

# MySQL engine format:
engine = create_engine("mysql+pymysql://username:password@localhost/test_db")

result = engine.execute("SELECT * FROM users")
for row in result:
    print(row)


session.close()
