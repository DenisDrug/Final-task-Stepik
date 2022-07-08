

class BasePage():
    def __init__(self, driver, url):
        self.driver = driver
        self.url = url

    def open(self):
        self.browser.get(self.url)