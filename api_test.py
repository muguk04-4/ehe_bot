import requests
import json

# GET POST 메소드를 한정해서 가져오는 법을 알아야됨
# 뭔가 이상함
# 다른 예제 찾기
# 어떻게 해야 할까
def send_api(path, method):
    API_HOST = "https://developer-lostark.game.onstove.com/guilds/rankings?serverName=%EB%A3%A8%ED%8E%98%EC%98%A8"
    my_jwt = "bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsIng1dCI6IktYMk40TkRDSTJ5NTA5NWpjTWk5TllqY2lyZyIsImtpZCI6IktYMk40TkRDSTJ5NTA5NWpjTWk5TllqY2lyZyJ9.eyJpc3MiOiJodHRwczovL2x1ZHkuZ2FtZS5vbnN0b3ZlLmNvbSIsImF1ZCI6Imh0dHBzOi8vbHVkeS5nYW1lLm9uc3RvdmUuY29tL3Jlc291cmNlcyIsImNsaWVudF9pZCI6IjEwMDAwMDAwMDAwMDA0OTcifQ.JwVQU-cdtyXpwFMJuZeRxPZb_pyz9JWY-2zZCwNwr2OaD2AbYSbHadZw8dIjO4b1f-BvmvEi0Xr6LDdnu0hWSZu3l1C7SIlf5IJPglJwtqPr2bTG2KVVjoq0SWmhxZkLNNuKBjXHG1ADGzem_3vtKnnbHkANBV8uZGzxfz3v-62bUMEAdKKdougJekJ-r22td_SPzv5jgpKlFAae1bHu2nYx7Q0Dz78pxWBnBLJsLCvs8enEFuYrAfD-IICDPntETTmSQjDOH23OkQJseVJnGfvzTyjcUvZO8d0M4-xv3p27D5E2tr9hUZyNnlDhxpncZ63FyMIT8FpUqM5hsPPDjA"
    url = API_HOST + path
    headers = {'Content-Type': 'application/json', 'charset': 'UTF-8', 'Accept': '*/*', 'authorization': my_jwt}
    body = {
        "key1": "value1",
        "key2": "value2"
    }
    try:
        if method == 'GET':
            response = requests.get(url, headers=headers)
        elif method == 'POST':
            response = requests.post(url, headers=headers, data=json.dumps(body, ensure_ascii=False, indent="\t"))
        print("response status %r" % response.status_code)
        print("response text %r" % response.text)
    except Exception as ex:
        print(ex)