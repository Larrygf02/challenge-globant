## GET STARTED

Dependencies: python, postgres

### CONFIG DATABASE

1. In pgadmin execute

```
    create database globant
```

2. Inside database globant execute the file "resources/sql/init.sql" to create the tables

3. Setup postgres username and password if different from mine in "services/config/variables.py"

```
    user = "postgres"
    password = "admin"
```

### START PROJECT LOCAL

1. Create environment and install dependencies

```
    pip install virtualenv
    virtualenv .venv
    source .venv/bin/activate
    pip install -r requirements.txt
```

2. Execute etl process to load data csv to tables.

```
    python etl.py
```

3. Runserver

```
    python main.py
```

4. Download postman collection to test the endpoints "challenge.postman_collection.json"

https://raw.githubusercontent.com/Larrygf02/challenge-globant/develop/challenge.postman_collection.json
