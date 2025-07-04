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

```bash
# Run all tests
pytest

# Run tests with HTML report
pytest --html=reports/report.html

# Run tests in parallel
pytest -n auto

# Run specific test markers
pytest -m "login"

# Run with detailed output
pytest -v
```

### Test Configuration

The `.env` file contains test configuration variables:
- Gmail test account credentials
- Browser settings (headless mode, browser type)
- Test data configuration
- Screenshot and video recording options
