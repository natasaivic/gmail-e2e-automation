# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a Gmail end-to-end automation testing project that covers:
- User login workflows
- Email composition and sending
- Email receipt verification
- Email searching functionality
- Email archiving operations

The goal is to ensure seamless and reliable Gmail email functionality through automated testing.

## Architecture Notes

This project uses **Playwright** for browser automation and **pytest** for test execution and organization.

## Technology Stack

- **Browser Automation**: Playwright - Modern, fast, and reliable browser automation
- **Test Framework**: pytest - Powerful Python testing framework with excellent fixtures and reporting
- **Language**: Python 3.8+

## Architecture Considerations

### Current Architecture
- **Browser Automation**: Playwright with headed mode for visibility
- **Test Framework**: pytest with comprehensive configuration
- **Test Execution**: Slow motion with pauses for educational purposes
- **Reporting**: HTML reports with screenshots and detailed logs
- **Configuration**: Environment-based setup with flexible modes

### Test Strategy & Architecture

**Hybrid Testing Approach**: The project uses both dedicated authentication tests and integrated workflow tests for comprehensive coverage.

#### 1. Dedicated Authentication Tests
- **Purpose**: Isolate login functionality for focused testing and debugging
- **Coverage**: OAuth2, 2FA, app passwords, invalid credentials, session persistence
- **Benefits**: Fast feedback, clear error isolation, comprehensive edge case testing
- **Test File**: `tests/test_login.py` (planned)

#### 2. Integrated Workflow Tests  
- **Purpose**: Test realistic user scenarios with login as prerequisite
- **Coverage**: Complete user journeys from login through email operations
- **Benefits**: Real-world validation, performance testing, user experience validation
- **Test Files**: `tests/test_email_*.py` (planned)

#### 3. Shared Authentication Fixtures
- **Purpose**: Reusable login utilities across all test suites
- **Implementation**: `tests/fixtures/auth_fixtures.py` (planned)
- **Features**: Pre-authenticated pages, login page setup, session management

### Future Implementation Considerations
- **Authentication**: Gmail login handling OAuth2, 2FA, and app-specific passwords
- **Email Verification**: Integration with email APIs or IMAP for receipt verification
- **Test Data Management**: Pytest fixtures for test accounts and email data management
- **Page Object Model**: Implement page objects for maintainable test code
- **Parallel Execution**: Leverage pytest-xdist for parallel test execution (use headless mode)
- **CI/CD Integration**: Design tests to run reliably in automated environments

## Project Structure

```
gmail-e2e-automation/
├── venv/                    # Virtual environment (tracked in git)
├── requirements.txt         # Python dependencies
├── .env                     # Environment variables
├── .gitignore              # Git ignore rules
├── pytest.ini              # Pytest configuration
├── README.md               # Project documentation
├── CLAUDE.md               # Claude Code guidance
├── screenshots/             # Test screenshots
├── reports/                 # HTML test reports
├── videos/                  # Test videos (if enabled)
└── tests/                  # Test files
    ├── conftest.py         # Playwright fixtures and configuration
    ├── test_smoke.py       # Smoke tests for basic functionality
    ├── test_login.py       # Dedicated authentication tests (planned)
    ├── test_email_compose.py  # Email composition workflows (planned)
    ├── test_email_search.py   # Email search functionality (planned)
    ├── test_email_management.py # Email organization workflows (planned)
    ├── fixtures/           # Shared test utilities (planned)
    │   └── auth_fixtures.py    # Authentication fixtures and utilities
    └── page_objects/       # Page object models (for future use)
```

## Development Commands

```bash
# Activate virtual environment
source venv/bin/activate    # On Windows: venv\Scripts\activate

# Install dependencies (if not already installed)
pip install -r requirements.txt

# Install Playwright browsers (if not already installed)
playwright install

# DEVELOPMENT MODE (Default - Headed with pauses)
# Run all tests with visible browser and output
pytest -v -s

# Run specific test file
pytest tests/test_smoke.py -v -s

# Run specific test
pytest tests/test_smoke.py::test_gmail_page_loads -v -s

# Run tests with specific markers
pytest -m smoke -v -s        # Smoke tests only
pytest -m login -v -s        # Authentication tests only (when implemented)
pytest -m email -v -s        # Email workflow tests only (when implemented)

# Generate HTML report (development mode)
pytest --html=reports/report.html -v -s

# PRODUCTION/CI MODE (Headless)
# Run tests in headless mode
HEADLESS=true pytest -v

# Run tests in parallel (headless recommended)
HEADLESS=true pytest -n auto

# BROWSER SELECTION
# Run with different browsers
BROWSER=firefox pytest -v -s
BROWSER=webkit pytest -v -s

# DEBUGGING
# Run with custom timeout
TIMEOUT=60000 pytest -v -s

# Run with video recording
VIDEO_ON_FAILURE=true pytest -v -s
```

## Test Configuration

### Current Test Setup
- **Development Mode**: Tests run in headed mode with 500ms slow motion
- **5-Second Pause**: Tests pause before browser closes for result viewing
- **Smoke Tests**: Basic Gmail page loading and element verification
- **Screenshot Capture**: Screenshots saved for each test
- **Comprehensive Logging**: Detailed test execution logs

### Environment Configuration
- **Virtual Environment**: The `venv/` directory is tracked in git for consistency
- **Environment Variables**: Use `.env` file for test configuration
- **Test Credentials**: Configure Gmail test account in `.env` file
- **Browser Settings**: Configurable via environment variables
- **Headed Mode Default**: HEADLESS=false for development visibility

### Test Execution Modes
1. **Development Mode (Default)**:
   - Headed browser with visible actions
   - 500ms slow motion between operations
   - 5-second pause at test completion
   - Perfect for debugging and development

2. **CI/Production Mode**:
   - Headless browser for faster execution
   - No pauses or slow motion
   - Suitable for automated environments

### Configuration Files
- **`.env`**: Environment variables and test settings
- **`pytest.ini`**: Pytest configuration with markers and reporting
- **`tests/conftest.py`**: Playwright fixtures and browser setup

## Security Considerations

- Never commit real Gmail credentials to the repository
- Use environment variables in `.env` file for test account credentials
- Create `.env.local` for actual credentials (this file should be gitignored)
- Consider using Gmail's test/sandbox environments when available
- Implement proper cleanup of test data after test runs
- Use app-specific passwords for Gmail authentication

## Current Implementation Status

### Completed Features
- ✅ Virtual environment setup with all dependencies
- ✅ Playwright and pytest configuration
- ✅ Environment variable management
- ✅ Smoke tests for Gmail page loading
- ✅ Headed mode with slow motion for development
- ✅ 5-second pause feature for result viewing
- ✅ Screenshot capture and test reporting
- ✅ Comprehensive pytest configuration

### Test Execution Features
- **Visible Browser**: Tests run in headed mode by default
- **Slow Motion**: 500ms delays between actions for better visibility
- **Pause Feature**: 5-second pause before browser closes
- **Screenshot Capture**: Automatic screenshots for verification
- **Detailed Logging**: Comprehensive test execution logs
- **Flexible Configuration**: Easy switching between headed/headless modes

### Important Notes
- The virtual environment (`venv/`) is included in the repository for consistency
- All dependencies are pre-installed in the virtual environment
- Playwright browsers are downloaded separately using `playwright install`
- Test reports are generated in the `reports/` directory
- Screenshots are saved in the `screenshots/` directory
- Use `-s` flag with pytest to see pause messages and print output
- Default configuration is optimized for development and learning