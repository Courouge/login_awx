import os, sys, subprocess, getpass, requests

class HiddenPrints:
    def __enter__(self):
        self._original_stdout = sys.stdout
        sys.stdout = open(os.devnull, 'w')

    def __exit__(self, exc_type, exc_val, exc_tb):
        sys.stdout.close()
        sys.stdout = self._original_stdout


url = "http://localhost:80"
url_login = url + "/api/login/"
username = raw_input("Username: ")
pswd = getpass.getpass('Password:')
tmp_id =  id(pswd)

with requests.session() as s:
    s.get(url_login,verify=False)
    csrf = s.get(url_login).cookies['csrftoken']
    headers = {
        'X-CSRFToken': csrf,
        'Referer' : url_login,
        'Content-Type':'application/x-www-form-urlencoded'
    }
    login_data = {
        'username': username,
        'password': pswd,
        'csrfmiddlewaretoken': csrf,
        'next': '/'
    }
    response = s.post(url_login, data=login_data)

    with HiddenPrints():
        myCmd = 'tower-cli job_template list --insecure --tower-username ' + username + ' --tower-password ' + pswd + ' --tower-host ' + url
        if tmp_id == id(pswd):
            subprocess.call(myCmd, shell=True)
        else:
            print "something is injected in your password"
