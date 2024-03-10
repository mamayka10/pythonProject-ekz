from sqlalchemy import String, Integer, Column, Text, create_engine
from sqlalchemy.orm import sessionmaker, declarative_base


engine = create_engine('sqlite:///base_3.db')

Base = declarative_base()

class PARTS3(Base):
    __tablename__ = 'parts'

    id = Column(Integer(), primary_key=True)
    sku = Column(String(50), nullable=False)
    brand = Column(Text(), nullable=False)

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

parts_table = [
    {'sku': '03586', 'brand': 'FEBI'},
    {'sku': '03587', 'brand': 'FEBI'},
    {'sku': '03588', 'brand': 'FEBI'}
]

for part_table in parts_table:
    part = PARTS3(**part_table)
    session.add(part)

session.commit()

session.close()
