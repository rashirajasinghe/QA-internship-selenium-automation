from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import os

class InternshipApplicationPage:
    
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
    
    # Locators - Update these based on actual form elements
    FULL_NAME_FIELD = (By.NAME, "full_name")  # Update based on actual form
    EMAIL_FIELD = (By.NAME, "email")  # Update based on actual form
    PHONE_FIELD = (By.NAME, "phone")  # Update based on actual form
    CV_UPLOAD = (By.NAME, "cv_file")  # Update based on actual form
    APPLY_BUTTON = (By.XPATH, "//button[contains(text(), 'Apply')]")  # Update based on actual form
    SUCCESS_MESSAGE = (By.CLASS_NAME, "success-message")  # Update based on actual form
    ERROR_MESSAGE = (By.CLASS_NAME, "error-message")  # Update based on actual form
    VALIDATION_MESSAGE = (By.CLASS_NAME, "validation-message")  # Update based on actual form
    
    def navigate_to_application_page(self):
        """Navigate to the internship application page"""
        print("Navigating to application page...")
        self.driver.get("http://futurecodetechnologies.cloud/careers")
        
        # Wait for page to load
        try:
            self.wait.until(EC.presence_of_element_located(self.FULL_NAME_FIELD))
            print("Page loaded successfully")
        except:
            print("Warning: Could not find full name field, trying alternative locators...")
            # Try alternative locators
            try:
                self.wait.until(EC.presence_of_element_located((By.TAG_NAME, "input")))
                print("Found input fields on page")
            except:
                print("Error: Could not load application form")
    
    def enter_full_name(self, name):
        """Enter full name in the form"""
        try:
            name_field = self.wait.until(EC.element_to_be_clickable(self.FULL_NAME_FIELD))
            name_field.clear()
            name_field.send_keys(name)
            print(f"Entered full name: {name}")
        except:
            print("Error: Could not find or interact with full name field")
            # Try alternative locators
            try:
                name_field = self.driver.find_element(By.XPATH, "//input[@placeholder='Your name']")
                name_field.clear()
                name_field.send_keys(name)
                print(f"Entered full name (alternative): {name}")
            except:
                print("Error: Could not find full name field with any locator")
    
    def enter_email(self, email):
        """Enter email in the form"""
        try:
            email_field = self.wait.until(EC.element_to_be_clickable(self.EMAIL_FIELD))
            email_field.clear()
            email_field.send_keys(email)
            print(f"Entered email: {email}")
        except:
            print("Error: Could not find or interact with email field")
            # Try alternative locators
            try:
                email_field = self.driver.find_element(By.XPATH, "//input[@placeholder='you@gmail.com']")
                email_field.clear()
                email_field.send_keys(email)
                print(f"Entered email (alternative): {email}")
            except:
                print("Error: Could not find email field with any locator")
    
    def enter_phone_number(self, phone):
        """Enter phone number in the form"""
        try:
            phone_field = self.wait.until(EC.element_to_be_clickable(self.PHONE_FIELD))
            phone_field.clear()
            phone_field.send_keys(phone)
            print(f"Entered phone: {phone}")
        except:
            print("Error: Could not find or interact with phone field")
            # Try alternative locators
            try:
                phone_field = self.driver.find_element(By.XPATH, "//input[@placeholder='+94 7X XXX XXXX']")
                phone_field.clear()
                phone_field.send_keys(phone)
                print(f"Entered phone (alternative): {phone}")
            except:
                print("Error: Could not find phone field with any locator")
    
    def upload_cv_file(self, file_path):
        """Upload CV file"""
        try:
            if os.path.exists(file_path):
                file_input = self.driver.find_element(*self.CV_UPLOAD)
                file_input.send_keys(file_path)
                print(f"Uploaded CV file: {file_path}")
            else:
                print(f"Warning: Test file not found: {file_path}")
                # Create a dummy file for testing
                self.create_dummy_file(file_path)
                file_input = self.driver.find_element(*self.CV_UPLOAD)
                file_input.send_keys(file_path)
                print(f"Created and uploaded dummy file: {file_path}")
        except:
            print("Error: Could not find or interact with file upload field")
            # Try alternative locators
            try:
                file_input = self.driver.find_element(By.XPATH, "//input[@type='file']")
                if os.path.exists(file_path):
                    file_input.send_keys(file_path)
                    print(f"Uploaded CV file (alternative): {file_path}")
                else:
                    self.create_dummy_file(file_path)
                    file_input.send_keys(file_path)
                    print(f"Created and uploaded dummy file (alternative): {file_path}")
            except:
                print("Error: Could not find file upload field with any locator")
    
    def create_dummy_file(self, file_path):
        """Create a dummy file for testing"""
        try:
            os.makedirs(os.path.dirname(file_path), exist_ok=True)
            with open(file_path, 'w') as f:
                f.write("This is a dummy CV file for testing purposes.")
            print(f"Created dummy file: {file_path}")
        except Exception as e:
            print(f"Error creating dummy file: {e}")
    
    def click_apply_button(self):
        """Click the apply button"""
        try:
            apply_button = self.wait.until(EC.element_to_be_clickable(self.APPLY_BUTTON))
            apply_button.click()
            print("Clicked apply button")
        except:
            print("Error: Could not find or click apply button")
            # Try alternative locators
            try:
                apply_button = self.driver.find_element(By.XPATH, "//button[contains(text(), 'Apply as an Intern')]")
                apply_button.click()
                print("Clicked apply button (alternative)")
            except:
                try:
                    apply_button = self.driver.find_element(By.XPATH, "//input[@type='submit']")
                    apply_button.click()
                    print("Clicked submit button (alternative)")
                except:
                    print("Error: Could not find any submit button")
    
    def get_success_message(self):
        """Get success message after submission"""
        try:
            success_element = self.wait.until(EC.presence_of_element_located(self.SUCCESS_MESSAGE))
            return success_element.text
        except:
            # Try alternative locators
            try:
                success_element = self.driver.find_element(By.XPATH, "//div[contains(@class, 'success')]")
                return success_element.text
            except:
                try:
                    success_element = self.driver.find_element(By.XPATH, "//div[contains(text(), 'success')]")
                    return success_element.text
                except:
                    return "No success message found"
    
    def get_error_message(self):
        """Get error message after submission"""
        try:
            error_element = self.wait.until(EC.presence_of_element_located(self.ERROR_MESSAGE))
            return error_element.text
        except:
            # Try alternative locators
            try:
                error_element = self.driver.find_element(By.XPATH, "//div[contains(@class, 'error')]")
                return error_element.text
            except:
                try:
                    error_element = self.driver.find_element(By.XPATH, "//div[contains(text(), 'error')]")
                    return error_element.text
                except:
                    return "No error message found"
    
    def get_validation_message(self):
        """Get real-time validation message"""
        try:
            validation_element = self.driver.find_element(*self.VALIDATION_MESSAGE)
            return validation_element.text
        except:
            # Try alternative locators
            try:
                validation_element = self.driver.find_element(By.XPATH, "//div[contains(@class, 'validation')]")
                return validation_element.text
            except:
                try:
                    validation_element = self.driver.find_element(By.XPATH, "//span[contains(@class, 'error')]")
                    return validation_element.text
                except:
                    return None
    
    def tab_to_next_field(self):
        """Tab to next field to trigger validation"""
        try:
            self.driver.find_element(*self.EMAIL_FIELD).send_keys(Keys.TAB)
            print("Tabbed to next field")
        except:
            print("Error: Could not tab to next field")
