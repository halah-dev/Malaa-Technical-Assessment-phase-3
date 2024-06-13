import random
from models import Alert
from faker import Faker
import os
from dotenv import load_dotenv

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

load_dotenv()

engine = create_engine(os.getenv("DATABASE_URL"))

Session = sessionmaker(bind=engine)
session = Session()

num = 15

fake = Faker()
symbols = ["AAPL", "MSFT", "GOOG", "AMZN", "META"]
for _ in range(num):
    data = Alert(
        name=fake.name(),
        symbol=random.choice(symbols),
        threshold_price=round(random.uniform(1.0, 500.0), 2),
    )
    session.add(data)
    session.commit()
