from resources.alert_rules.alert_rule_model import AlertRule
from resources.alerts.alert_model import Alert

import os
from dotenv import load_dotenv

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

load_dotenv()

engine = create_engine(os.getenv("DATABASE_URL"))

Session = sessionmaker(bind=engine)
session = Session()

Alert.metadata.create_all(bind=engine)
AlertRule.metadata.create_all(bind=engine)
