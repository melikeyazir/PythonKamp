from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ac
from selenium.webdriver.common.action_chains import ActionChains
import pytest


#prefix => ön ek test_   #Test dosyalarında class adına test_ olarak başlanır ki dosya test dosyası olarak algılanabilsin
#postfix

class Test_DemoClass:
    #Her testten önce çağırılır
    def setup_method(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.maximize_window()
        self.driver.get("https://www.saucedemo.com/")
    #her testten sonra çağırılır
    def teardown_method(self):
        self.driver.quit()
    
    #setup -> test_demoFunc-> teardown
    def test_demoFunc(self):
        # 3A Act Arrange Assert
        text = "Hello"
        assert text == "Hello"
    #setup -> test_demoFunc-> teardown
    def test_demo2(self):
        assert True
   
   
    @pytest.mark.parametrize("username,password",[("1","1"),("kullaniciadim","sifrem")])    #parametrize ile tek seferde birkaç parametre ile birlikte test yapmamızı sağlar.
    # @pytest.mark.skip()  # SKİP pyteste aşağıdaki verileri atlattırma işlemi yapar!
    def test_invalid_login(self, username, password):            #invalid_login başarısız testler için olan bir yapıdır. Doğru sonuç alacak bir yapı oluşturulursa hata alınır.
        WebDriverWait(self.driver,5).until(ac.visibility_of_element_located((By.ID, "user-name")))
        usernameInput = self.driver.find_element(By.ID, "user-name")
        WebDriverWait(self.driver,5).until(ac.visibility_of_element_located((By.ID, "password")))
        passwordInput = self.driver.find_element(By.ID,"password")
        usernameInput.send_keys(username)
        passwordInput.send_keys(password)
               
        loginButton = self.driver.find_element(By.ID, "login-button")
        loginButton.click()
       
        errormessage = self.driver.find_element(By.XPATH,"//*[@id='login_button_container']/div/form/div[3]/h3")
        assert  errormessage.text == "Epic sadface: Username and password do not match any user in this service"
     
      
        assert True
    