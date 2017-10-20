import os

ENV = os.environ.get('ENV')
SETTINGS = {
    'clash_key': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiIsImtpZCI6IjI4YTMxOGY3LTAwMDAtYTFlYi03ZmExLTJjNzQzM2M2Y2NhNSJ9.eyJpc3MiOiJzdXBlcmNlbGwiLCJhdWQiOiJzdXBlcmNlbGw6Z2FtZWFwaSIsImp0aSI6IjA3YWNmYzI3LTg2ZjktNDIyNC1iZTBiLTcwZWZmNzVjZjhlNCIsImlhdCI6MTQ5NzIyMjk4Mywic3ViIjoiZGV2ZWxvcGVyL2U0NDIwZTlmLTExMGYtNWNlNS04MGJkLWJlZDBhMWVmYjZjZSIsInNjb3BlcyI6WyJjbGFzaCJdLCJsaW1pdHMiOlt7InRpZXIiOiJkZXZlbG9wZXIvc2lsdmVyIiwidHlwZSI6InRocm90dGxpbmcifSx7ImNpZHJzIjpbIjE4MS4yMTAuNDEuMTk1Il0sInR5cGUiOiJjbGllbnQifV19.2B7fhNxww3BxFIfKVUJu_3LLUhyBQnYY2afK3ihFUrj8AUobJLt_frt8DLB4Y-u8YNDD9aNeL7YmpCORjgt-WQ'
}
if (ENV == 'production'):
    SETTINGS = {
        'clash_key':''
    }
elif (ENV == 'qa'):
    SETTINGS = {
        'clash_key':''
    }
elif (ENV == 'dev'):
    SETTINGS = {
        'clash_key':''
    }
