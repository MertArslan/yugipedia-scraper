import requests


class NetworkController:

    def get_website(self, website):
        page = requests.get(website)
        if page.status_code != 200:
            print("something went wrong")
        else:
            print("got the website")
        return page

