from example import db
from example import Company, KPI

db.create_all()
one = Company(ticker="TGT")
two = Company(ticker="AMZN")
db.session.add_all([one, two])
db.session.commit()

first = KPI(kpi_name="NET_REVENUE", company=one)
second = KPI(kpi_name="INTERNET_REVENUE", company=one)
third = KPI(kpi_name="NET_REVENUE", company=two)
db.session.commit()
