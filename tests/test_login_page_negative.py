import time
import pytest
from selenium.webdriver.common.by import By


class TestNegativeScenarios:

    @pytest.mark.login
    @pytest.mark.negative
    @pytest.mark.parametrize("username, password, expected_error_message", [("incorrectUser", "Password123",
                                                                             "Your username is invalid!"),
                                                                            ("student", "incorrectPassword",
                                                                             "Your password is invalid!")])
    def test_negative_login(self, driver, username, password, expected_error_message):
        # Open page
        # driver = webdriver.Chrome()
        driver.get("https://practicetestautomation.com/practice-test-login/")
        time.sleep(2)

        # Type username incorrectUser into Username field
        username_locator = driver.find_element(By.ID, "username")
        username_locator.send_keys(username)

        # Type password Password123 into Password field
        password_locator = driver.find_element(By.XPATH, "//input[@id='password']")
        password_locator.send_keys(password)

        # Push Submit button
        submit_button_locator = driver.find_element(By.XPATH, "//button[@id='submit']")
        submit_button_locator.click()
        time.sleep(2)

        # Verify error message is displayed
        error_message_locator = driver.find_element(By.XPATH, "//div[@id='error']")
        assert error_message_locator.is_displayed(), "Error message is not displayed, but it should"

        # Verify error message text is Your username is invalid!
        actual_error_message = error_message_locator.text
        assert actual_error_message == expected_error_message, "Error message is not expected"

    # @pytest.mark.login
    # @pytest.mark.negative
    def test_negative_username(self, driver):
        # Open page
        # driver = webdriver.Chrome()
        driver.get("https://practicetestautomation.com/practice-test-login/")
        time.sleep(2)

        # Type username incorrectUser into Username field
        username_locator = driver.find_element(By.ID, "username")
        username_locator.send_keys("incorrectUser")

        # Type password Password123 into Password field
        password_locator = driver.find_element(By.XPATH, "//input[@id='password']")
        password_locator.send_keys("Password123")

        # Push Submit button
        submit_button_locator = driver.find_element(By.XPATH, "//button[@id='submit']")
        submit_button_locator.click()
        time.sleep(2)

        # Verify error message is displayed
        error_message_locator = driver.find_element(By.XPATH, "//div[@id='error']")
        assert error_message_locator.is_displayed(), "Error message is not displayed, but it should"

        # Verify error message text is Your username is invalid!
        actual_error_message = error_message_locator.text
        assert actual_error_message == "Your username is invalid!", "Error message is not expected"

    # @pytest.mark.login
    # @pytest.mark.negative
    def test_negative_password(self, driver):
        # Open page
        # driver = webdriver.Chrome()

        # Open webpage
        driver.get("https://practicetestautomation.com/practice-test-login/")
        time.sleep(2)

        # Type username student into Username field
        username_locator = driver.find_element(By.ID, "username")
        username_locator.send_keys("student")

        # Type password incorrectPassword into Password field
        password_locator = driver.find_element(By.ID, "password")
        password_locator.send_keys("incorrectPassword")

        # Push Submit button
        submit_button_locator = driver.find_element(By.XPATH, "//button[@id='submit']")
        submit_button_locator.click()
        time.sleep(2)

        # Verify error message is displayed
        error_message_locator = driver.find_element(By.XPATH, "//div[@id='error']")
        error_message_locator.is_displayed(), "Error message it not displayed, but it should"

        # Verify error message text is Your password is invalid!
        actual_error_message = error_message_locator.text
        assert actual_error_message == "Your password is invalid!", "Error message is not expected"
