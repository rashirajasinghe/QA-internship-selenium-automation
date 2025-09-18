import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from pages.internship_application_page import InternshipApplicationPage
from utils.test_data import TestData
import time
import os

class TestInternshipApplication:
    
    @pytest.fixture(scope="function")
    def setup(self):
        """Setup method to initialize driver before each test"""
        # Chrome options
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--headless")  # Run in headless mode
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--window-size=1920,1080")
        
        # Initialize driver
        service = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service, options=chrome_options)
        self.driver.maximize_window()
        
        # Initialize page object
        self.app_page = InternshipApplicationPage(self.driver)
        
        yield self.driver
        
        # Cleanup
        self.driver.quit()
    
    def test_successful_application_submission(self, setup):
        """Test successful internship application submission"""
        print("\n=== Testing Successful Application Submission ===")
        
        # Navigate to application page
        self.app_page.navigate_to_application_page()
        
        # Fill form with valid data
        self.app_page.enter_full_name(TestData.VALID_FULL_NAME)
        self.app_page.enter_email(TestData.VALID_EMAIL)
        self.app_page.enter_phone_number(TestData.VALID_PHONE)
        self.app_page.upload_cv_file(TestData.VALID_CV_PATH)
        
        # Submit application
        self.app_page.click_apply_button()
        
        # Wait for response
        time.sleep(3)
        
        # Verify success
        success_message = self.app_page.get_success_message()
        print(f"Success message: {success_message}")
        
        # Take screenshot
        self.driver.save_screenshot("screenshots/successful_application.png")
        print("Screenshot saved: successful_application.png")
    
    def test_invalid_email_validation(self, setup):
        """Test application with invalid email format"""
        print("\n=== Testing Invalid Email Validation ===")
        
        self.app_page.navigate_to_application_page()
        
        # Fill form with invalid email
        self.app_page.enter_full_name(TestData.VALID_FULL_NAME)
        self.app_page.enter_email(TestData.INVALID_EMAIL)
        self.app_page.enter_phone_number(TestData.VALID_PHONE)
        self.app_page.upload_cv_file(TestData.VALID_CV_PATH)
        
        # Submit application
        self.app_page.click_apply_button()
        
        # Wait for response
        time.sleep(3)
        
        # Check for error message
        error_message = self.app_page.get_error_message()
        print(f"Error message: {error_message}")
        
        # Take screenshot
        self.driver.save_screenshot("screenshots/invalid_email_error.png")
        print("Screenshot saved: invalid_email_error.png")
    
    def test_invalid_phone_validation_bug(self, setup):
        """Test application with invalid phone number (BUG TEST)"""
        print("\n=== Testing Invalid Phone Validation (BUG TEST) ===")
        
        self.app_page.navigate_to_application_page()
        
        # Fill form with invalid phone
        self.app_page.enter_full_name(TestData.VALID_FULL_NAME)
        self.app_page.enter_email(TestData.VALID_EMAIL)
        self.app_page.enter_phone_number(TestData.INVALID_PHONE)
        self.app_page.upload_cv_file(TestData.VALID_CV_PATH)
        
        # Submit application
        self.app_page.click_apply_button()
        
        # Wait for response
        time.sleep(3)
        
        # Check for error message
        error_message = self.app_page.get_error_message()
        success_message = self.app_page.get_success_message()
        
        print(f"Error message: {error_message}")
        print(f"Success message: {success_message}")
        
        if "success" in success_message.lower() or "submitted" in success_message.lower():
            print("🐛 BUG CONFIRMED: Application accepted invalid phone number 'abc'")
        else:
            print("✅ Bug fixed: Application properly rejected invalid phone number")
        
        # Take screenshot
        self.driver.save_screenshot("screenshots/invalid_phone_bug.png")
        print("Screenshot saved: invalid_phone_bug.png")
    
    def test_invalid_name_validation_bug(self, setup):
        """Test application with special characters in name (BUG TEST)"""
        print("\n=== Testing Invalid Name Validation (BUG TEST) ===")
        
        self.app_page.navigate_to_application_page()
        
        # Fill form with invalid name
        self.app_page.enter_full_name(TestData.INVALID_NAME)
        self.app_page.enter_email(TestData.VALID_EMAIL)
        self.app_page.enter_phone_number(TestData.VALID_PHONE)
        self.app_page.upload_cv_file(TestData.VALID_CV_PATH)
        
        # Submit application
        self.app_page.click_apply_button()
        
        # Wait for response
        time.sleep(3)
        
        # Check for error message
        error_message = self.app_page.get_error_message()
        success_message = self.app_page.get_success_message()
        
        print(f"Error message: {error_message}")
        print(f"Success message: {success_message}")
        
        if "success" in success_message.lower() or "submitted" in success_message.lower():
            print("🐛 BUG CONFIRMED: Application accepted invalid name 'Rashini@123'")
        else:
            print("✅ Bug fixed: Application properly rejected invalid name")
        
        # Take screenshot
        self.driver.save_screenshot("screenshots/invalid_name_bug.png")
        print("Screenshot saved: invalid_name_bug.png")
    
    def test_empty_required_fields(self, setup):
        """Test application with empty required fields"""
        print("\n=== Testing Empty Required Fields ===")
        
        self.app_page.navigate_to_application_page()
        
        # Leave name field empty
        self.app_page.enter_email(TestData.VALID_EMAIL)
        self.app_page.enter_phone_number(TestData.VALID_PHONE)
        self.app_page.upload_cv_file(TestData.VALID_CV_PATH)
        
        # Submit application
        self.app_page.click_apply_button()
        
        # Wait for response
        time.sleep(3)
        
        # Check for error message
        error_message = self.app_page.get_error_message()
        print(f"Error message: {error_message}")
        
        # Take screenshot
        self.driver.save_screenshot("screenshots/empty_fields_error.png")
        print("Screenshot saved: empty_fields_error.png")
    
    def test_invalid_file_type(self, setup):
        """Test application with invalid file type"""
        print("\n=== Testing Invalid File Type ===")
        
        self.app_page.navigate_to_application_page()
        
        # Fill form with invalid file
        self.app_page.enter_full_name(TestData.VALID_FULL_NAME)
        self.app_page.enter_email(TestData.VALID_EMAIL)
        self.app_page.enter_phone_number(TestData.VALID_PHONE)
        self.app_page.upload_cv_file(TestData.INVALID_FILE_PATH)
        
        # Submit application
        self.app_page.click_apply_button()
        
        # Wait for response
        time.sleep(3)
        
        # Check for error message
        error_message = self.app_page.get_error_message()
        print(f"Error message: {error_message}")
        
        # Take screenshot
        self.driver.save_screenshot("screenshots/invalid_file_error.png")
        print("Screenshot saved: invalid_file_error.png")
    
    def test_file_size_limit(self, setup):
        """Test application with file exceeding size limit"""
        print("\n=== Testing File Size Limit ===")
        
        self.app_page.navigate_to_application_page()
        
        # Fill form with large file
        self.app_page.enter_full_name(TestData.VALID_FULL_NAME)
        self.app_page.enter_email(TestData.VALID_EMAIL)
        self.app_page.enter_phone_number(TestData.VALID_PHONE)
        self.app_page.upload_cv_file(TestData.LARGE_FILE_PATH)
        
        # Submit application
        self.app_page.click_apply_button()
        
        # Wait for response
        time.sleep(3)
        
        # Check for error message
        error_message = self.app_page.get_error_message()
        print(f"Error message: {error_message}")
        
        # Take screenshot
        self.driver.save_screenshot("screenshots/file_size_error.png")
        print("Screenshot saved: file_size_error.png")
    
    def test_real_time_validation(self, setup):
        """Test real-time form validation"""
        print("\n=== Testing Real-time Validation ===")
        
        self.app_page.navigate_to_application_page()
        
        # Test email validation
        self.app_page.enter_email("invalid-email")
        self.app_page.tab_to_next_field()
        
        # Wait a moment for validation
        time.sleep(2)
        
        # Check for validation message
        validation_message = self.app_page.get_validation_message()
        print(f"Validation message: {validation_message}")
        
        # Take screenshot
        self.driver.save_screenshot("screenshots/real_time_validation.png")
        print("Screenshot saved: real_time_validation.png")
