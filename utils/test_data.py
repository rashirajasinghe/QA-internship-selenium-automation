import os

class TestData:
    # Valid test data
    VALID_FULL_NAME = "John Doe"
    VALID_EMAIL = "john.doe@example.com"
    VALID_PHONE = "+94 77 123 4567"
    
    # Invalid test data
    INVALID_EMAIL = "invalid-email@.com"
    INVALID_PHONE = "abc"  # This should fail but currently passes (BUG)
    INVALID_NAME = "Rashini@123"  # This should fail but currently passes (BUG)
    
    # File paths
    VALID_CV_PATH = os.path.join(os.getcwd(), "test_files", "valid_cv.pdf")
    INVALID_FILE_PATH = os.path.join(os.getcwd(), "test_files", "invalid_file.txt")
    LARGE_FILE_PATH = os.path.join(os.getcwd(), "test_files", "large_file.pdf")
    
    # Test URLs
    APPLICATION_URL = "http://futurecodetechnologies.cloud/careers"
    
    # Expected messages
    SUCCESS_MESSAGE = "Application submitted successfully"
    EMAIL_ERROR_MESSAGE = "Please enter a valid email address"
    PHONE_ERROR_MESSAGE = "Please enter a valid phone number"
    NAME_ERROR_MESSAGE = "Name contains invalid characters"
    FILE_ERROR_MESSAGE = "Please upload a valid file type"
    SIZE_ERROR_MESSAGE = "File size must be less than 10MB"
    
    # Additional test data for comprehensive testing
    VALID_NAMES = [
        "John Doe",
        "Jane Smith",
        "Bob Johnson",
        "Alice Brown",
        "Charlie Wilson"
    ]
    
    INVALID_NAMES = [
        "John@123",
        "Mary#Smith",
        "Bob$Johnson",
        "Alice123",
        "Test!@#$%"
    ]
    
    VALID_EMAILS = [
        "john.doe@example.com",
        "jane.smith@test.com",
        "bob.johnson@company.org"
    ]
    
    INVALID_EMAILS = [
        "user@.com",
        "user.com",
        "user@",
        "user@domain",
        "invalid-email@.com"
    ]
    
    VALID_PHONES = [
        "+94 77 123 4567",
        "+94 71 987 6543",
        "+94 70 555 1234"
    ]
    
    INVALID_PHONES = [
        "abc",
        "123",
        "1234567890",
        "invalid-phone",
        "+94 abc def ghi"
    ]
