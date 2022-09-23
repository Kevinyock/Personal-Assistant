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

    def IsGoogleDown(self):
        responseCode = requests.get("http://www.google.com/").status_code
        self.statusCode(responseCode,"Google")

    def statusCode(self,responseCode,WebsiteName):
        if(responseCode == 100):
            print("Continue")
        elif(responseCode == 200):
            print(WebsiteName + " Is Online")
            print("Ok")
        elif(responseCode == 301):
            print("URL was moved to a new link")
        elif(responseCode == 302):
            print("URL was found")
        elif(responseCode == 303):
            print("See Other")
        elif(responseCode == 304):
            print("Not modified")
        elif(responseCode == 307):
            print("Temporary Redirect")
        elif(responseCode == 400):
            print("Bad Request")
        elif(responseCode == 401):
            print("Unauthorized")
        elif(responseCode == 403):
            print("Forbidden")
        elif(responseCode == 404):
            print("Not Found")
        elif(responseCode == 405):
            print("Method Not Allowed")
        elif(responseCode == 408):
            print("Request Timeout")
        elif(responseCode == 410):
            print("Gone")
        elif(responseCode == 415):
            print("Unsupported Media Type")
        elif(responseCode == 500):
            print("Internal Server Error")
        elif(responseCode == 502):
            print("Bad Gateway")
        elif(responseCode == 503):
            print("Service Unavailable")
        elif(responseCode == 504):
            print("Gateway Timeout")
        elif(responseCode == 509):
            print("Bandwidth Limit Exceeded")
        