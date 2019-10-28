import requests

url = "http://localhost/api/login/"

with requests.session() as s:
    s.get(url,verify=False)
    csrf = s.get(url).cookies['csrftoken']
    headers = {
        'X-CSRFToken': csrf,
        'Referer' : url,
        'Content-Type':'application/x-www-form-urlencoded'
    }
    login_data = {
        'username': 'admin',
        'password': 'password',
        'csrfmiddlewaretoken': csrf,
        'next': '/'
    }
    response = s.post(url, data=login_data)
    print(response.status_code)
    print(response.cookies['sessionid'])
    print(s.get('http://localhost/api/v2/me/').json()['results'][0]['username'])
