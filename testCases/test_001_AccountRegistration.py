from utilites.customLogger import LogGen
from pageObjects.HomePage import HomePage
from utilites.readProperties import ReadConfig


class Test_001_AccountReg:
    baseURL = ReadConfig.getApplicationURL()
    logger = LogGen.loggen()

    def test_account_reg(self,setup):
        self.logger.info("***test case 001 started")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.hp=HomePage(self.driver)
        self.hp.clickMyAccount()
        self.logger.info("***test case 001 My account clicked")
        # self.hp.clickRegister()
        # self.regpage=AccountRegistrationPage(self.driver)
        # self.regpage.setFirstName("John")
        # self.regpage.setLastName("Canedy")
        # self.email = "lklkl"
        # self.regpage.setEmail(self.email)
        # self.regpage.setTelephone("65656565")
        # self.regpage.setPassword("abcxyz")
        # self.regpage.setConfirmPassword("abcxyz")
        # self.regpage.setPrivacyPolicy()
        # self.regpage.clickContinue()
        # self.confmsg=self.regpage.getconfirmationmsg()
        # self.driver.close()
        # if self.confmsg=="Your Account Has Been Created!":
        #     assert True
        # else:
        #     assert False
        self.logger.info("***test case 001 completed")






