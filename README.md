# CoCAPI IP Adress
`138.68.228.152`

# Pre-requisites:
Have python, pip and virtualenv installed
Create a .json with the following format and the mysql 
can have all the parameters as the [PyMySql Connection Object parameters][pymysql-connection]:
```json
{
    "clash_key": "your.berear.clashkey",
    "mysql": {
        "user":"userNameHere",
        "password":"mysupersecurepassword",
        "database":"mydb",
        "host":"localhost",
        "port": 3306,
        "charset": "utf8",
        "use_unicode": true
    }
}
```
# Installing and running
1. `virtualenv venv`
2. For linux & OS X users: `source venv/bin/activate`. For windows users: `.\venv\Scripts\activate`
3. Install all the requirements: `pip install -r requirements.txt`
4. Linux & OS X: `sh server.sh`. Windows: `python main.py`
5. Now open the browser and write the following url: `localhost:8080`


    [pymysql-connection]: https://pymysql.readthedocs.io/en/latest/modules/connections.html