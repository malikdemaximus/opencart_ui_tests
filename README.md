
# Selenium Page Object Model Project

This project demonstrates the usage of the **Page Object Model** pattern in Selenium for automating login and registration flows.

## Project Structure
- **pages/** - Contains the Page Object classes for Login and Registration pages.
- **tests/** - Contains test cases for Login and Registration.
- **drivers/** - Contains the web driver for running tests.

## Technologies Used
- Selenium WebDriver
- Python
- Unittest

## Setup
1. Clone this repository.
2. Install the required dependencies using pip:
   ```bash
   pip install -r requirements.txt
   ```
3. Download the appropriate driver for your browser (e.g., ChromeDriver for Google Chrome).
4. Run the tests:
   ```bash
   python -m unittest tests/test_login.py
   python -m unittest tests/test_register.py
   ```

## Notes
- The tests assume that the website is hosted at `http://yourwebsite.com`. Update the URL as per your needs.
- The project is structured using the Page Object Model (POM) pattern for better scalability and maintainability.

## Authors
- Yermekbay Abdulmalik

## License
This project is licensed under the MIT License.
