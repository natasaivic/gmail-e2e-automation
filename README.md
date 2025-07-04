# Gmail E2E Automation Testing Suite

## Overview

This comprehensive end-to-end testing framework validates critical Gmail workflows using **Playwright** and **pytest**. The suite ensures email functionality remains reliable and performs as expected across different environments and user scenarios.

## Test Coverage

The automation suite covers the following core email workflows:

### Authentication & Access
- User login authentication flows
- Account security verification
- Session management validation

### Email Composition & Delivery
- Email composition interface testing
- Message formatting and attachment handling
- Email sending functionality validation
- Delivery confirmation testing

### Email Management Operations
- Inbox message retrieval and display
- Email search functionality across various criteria
- Email archiving and organizational features
- Message filtering and categorization

### Data Validation
- Email content integrity verification
- Receipt confirmation testing
- Cross-platform email synchronization

## Quality Assurance Objectives

- **Functional Testing**: Verify all Gmail features work as designed
- **Regression Testing**: Ensure new changes don't break existing functionality
- **Cross-browser Compatibility**: Validate consistent behavior across browsers
- **Performance Testing**: Monitor email operation response times
- **Data Integrity**: Ensure email content remains intact throughout workflows

## Technology Stack

- **Browser Automation**: Playwright - Modern, fast, and reliable cross-browser automation
- **Test Framework**: pytest - Powerful Python testing framework with excellent fixtures and reporting
- **Language**: Python 3.8+
- **Browsers Supported**: Chromium, Firefox, WebKit (Safari)

## Test Environment

The test suite is designed to run against Gmail's web interface using Playwright's browser automation capabilities. Tests provide comprehensive coverage of user-facing functionality while maintaining test data isolation and cleanup procedures.

## Project Setup

### Prerequisites
- Python 3.8+
- Git

### Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd gmail-e2e-automation
   ```

2. **Set up virtual environment**
   ```bash
   # Virtual environment is included in the repository
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Install Playwright browsers**
   ```bash
   playwright install
   ```

5. **Configure environment variables**
   ```bash
   # Copy and edit .env file with your test credentials
   cp .env .env.local
   # Edit .env.local with your actual Gmail test account credentials
   ```

### Running Tests

#### Available Tests
- **Smoke Tests**: Basic functionality verification (`tests/test_smoke.py`)
  - Gmail page loading verification
  - Basic element presence checks

#### Test Execution Commands

```bash
# Run all tests (headed mode by default for development)
pytest

# Run with visible output (shows pause messages)
pytest -v -s

# Run specific test file
pytest tests/test_smoke.py -v -s

# Run specific test
pytest tests/test_smoke.py::test_gmail_page_loads -v -s

# Run smoke tests only
pytest -m smoke -v -s

# Run tests with HTML report
pytest --html=reports/report.html -v -s
```

#### Test Modes

**Development Mode (Default - Headed)**:
- Browser opens visibly
- 500ms slow motion between actions
- 5-second pause at end of each test
- Perfect for debugging and development

**CI/Production Mode (Headless)**:
```bash
# Force headless mode
HEADLESS=true pytest -v

# Run tests in parallel (headless recommended)
HEADLESS=true pytest -n auto
```

#### Browser Configuration
```bash
# Run with different browser
BROWSER=firefox pytest -v -s
BROWSER=webkit pytest -v -s

# Custom timeout
TIMEOUT=60000 pytest -v -s
```

### Test Configuration

The project includes comprehensive test configuration:

#### Configuration Files
- **`.env`**: Environment variables and test settings
- **`pytest.ini`**: Pytest configuration with markers and reporting
- **`tests/conftest.py`**: Playwright fixtures and browser setup

#### Key Settings
- **HEADLESS=false**: Runs tests in visible browser (development mode)
- **SLOW_MO=500**: 500ms delays between actions for better visibility
- **TIMEOUT=30000**: 30-second timeout for page operations
- **5-second pause**: Tests pause before browser closes for result viewing

#### Test Environment Variables
```bash
# Browser Configuration
HEADLESS=false          # Show browser during tests
BROWSER=chromium        # Browser type (chromium/firefox/webkit)
TIMEOUT=30000           # Operation timeout in milliseconds
BASE_URL=https://mail.google.com

# Test Data
GMAIL_TEST_EMAIL=your_test_email@gmail.com
GMAIL_TEST_PASSWORD=your_app_specific_password
TEST_RECIPIENT_EMAIL=recipient@example.com
TEST_SUBJECT_PREFIX=E2E_TEST

# Test Artifacts
SCREENSHOT_ON_FAILURE=true
VIDEO_ON_FAILURE=true
TRACE_ON_FAILURE=true
```

#### Test Reports and Artifacts
- **HTML Reports**: Generated in `reports/report.html`
- **Screenshots**: Saved in `screenshots/` directory
- **Videos**: Saved in `videos/` directory (if enabled)
- **Traces**: Playwright traces for debugging failures
