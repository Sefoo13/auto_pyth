class Welcome(object):
    def __init__(self, driver):
        self.driver = driver

    def SignIn(self):
        self.driver.find_element_by_id("Sign_in").click()

    def SignUp(self):
        self.driver.find_element_by_id("Sign_up").click()

    def Test(self):
        return SignUp()