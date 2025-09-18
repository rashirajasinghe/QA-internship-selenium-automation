#!/usr/bin/env python3
"""
QA Internship Assignment - Part 4: Selenium Automation
Run script for executing automated tests
"""

import subprocess
import sys
import os

def install_requirements():
    """Install required packages"""
    print("Installing required packages...")
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
        print("✅ Requirements installed successfully!")
    except subprocess.CalledProcessError as e:
        print(f"❌ Error installing requirements: {e}")
        return False
    return True

def run_tests():
    """Run the automated tests"""
    print("\n" + "="*50)
    print("🚀 Starting Selenium Automation Tests")
    print("="*50)
    
    # Create necessary directories
    os.makedirs("reports", exist_ok=True)
    os.makedirs("screenshots", exist_ok=True)
    os.makedirs("test_files", exist_ok=True)
    
    # Run tests
    try:
        print("\n📋 Running test suite...")
        result = subprocess.run([
            sys.executable, "-m", "pytest", 
            "tests/test_internship_application.py",
            "--html=reports/report.html",
            "--self-contained-html",
            "-v",
            "--tb=short"
        ], capture_output=True, text=True)
        
        print("Test Output:")
        print(result.stdout)
        
        if result.stderr:
            print("Errors/Warnings:")
            print(result.stderr)
        
        if result.returncode == 0:
            print("\n✅ All tests completed successfully!")
        else:
            print(f"\n⚠️ Tests completed with exit code: {result.returncode}")
        
        print(f"\n📊 Test results saved to: reports/report.html")
        print(f"📸 Screenshots saved to: screenshots/")
        
    except Exception as e:
        print(f"❌ Error running tests: {e}")

def main():
    """Main function"""
    print("QA Internship Assignment - Part 4: Selenium Automation")
    print("Future Code Tech Stack")
    print("-" * 50)
    
    # Install requirements
    if not install_requirements():
        print("❌ Failed to install requirements. Exiting.")
        return
    
    # Run tests
    run_tests()
    
    print("\n" + "="*50)
    print("🎉 Test execution completed!")
    print("="*50)

if __name__ == "__main__":
    main()
