# CoCAPI
IP: 138.68.228.152

# Pre-requisites:
Have python, pip and virtualenv installed
Create a .json with the following format:
```json
{
    "clash_key": "your.berear.clashkey",
    "mysql": {
        "MYSQL_DATABASE_USER":"str",
        "MYSQL_DATABASE_PASSWORD":"str",
        "MYSQL_DATABASE_DB":"str",
        "MYSQL_DATABASE_HOST":"str",
        "MYSQL_DATABASE_PORT": "int"
    }
}
```
# Installing and running
1. `virtualenv venv`
2. For linux & OS X users: `source venv/bin/activate`. For windows users: `.\venv\Scripts\activate`
3. Install all the requirements: `pip install -r requirements.txt`
4. Linux & OS X: `sh server.sh`. Windows: `python main.py`
5. Now open the browser and write the following url: `localhost:8080`