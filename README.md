# Serlialized Python Objects

The goal of this project is to develop skills around serializing Python classes to and from both SQL and JSON.

Reference:<br>
https://marshmallow-sqlalchemy.readthedocs.io/en/latest/

<b>User Story:</b><br>
<b>AS A</b> financial analyst<br>
<b>I WANT TO</b> map my companies across various things like KPIS and SECTORS<br>
<b>SO THAT I</b> can visualize mappings easily in an app with JSON (and share with Javascript front end apps) but also maintain a second form database structure on the back end in SQL

This project uses flask and marshmallow along with sqlalchemy as an ORM.

![image](https://user-images.githubusercontent.com/39496491/222187293-2ac82371-ec90-40ca-807e-20cd15746bbf.png)

The example.py uses a combination of sqlalchemy's Model class inheritance and Marshmallow auto schema for serialization.

![image](https://user-images.githubusercontent.com/39496491/222187629-3cfd8593-057e-4090-a89e-56e28a4974de.png)

Run setup.py to initialize the SQLite database.
