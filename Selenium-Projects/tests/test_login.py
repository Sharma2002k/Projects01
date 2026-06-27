from pages.login_page import LoginPage

def test_login(driver):

    driver.get("https://practicetestautomation.com/practice-test-login/")

    login = LoginPage(driver)
    login.login("student", "Password123")

    assert "Logged In Successfully" in driver.page_source