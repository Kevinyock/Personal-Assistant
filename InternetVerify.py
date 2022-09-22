import requests

class InternetConnection():

    def __init__(self):
        self.timeout = 1
        print("Internet connection module online")
        self.InternetStatus()

    def InternetStatus(self):
        try:
            requests.head("http://www.google.com/", timeout = self.timeout)
            print("Internet Connectivity is Active")
        except requests.ConnectionError:
            print("The Internet is down")
