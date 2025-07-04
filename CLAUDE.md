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

- **Authentication**: Gmail login will require handling OAuth2 or app-specific passwords
- **Email Verification**: May need integration with email APIs or IMAP for receipt verification
- **Test Data Management**: Use pytest fixtures for test accounts and email data management
- **Page Object Model**: Implement page objects for maintainable test code
- **Parallel Execution**: Leverage pytest-xdist for parallel test execution
- **CI/CD Integration**: Design tests to run reliably in automated environments

## Project Structure

```
gmail-e2e-automation/
├── venv/                    # Virtual environment (tracked in git)
├── requirements.txt         # Python dependencies
├── .env                     # Environment variables template
├── .gitignore              # Git ignore rules
├── README.md               # Project documentation
├── CLAUDE.md               # Claude Code guidance
└── tests/                  # Test files (to be created)
    ├── conftest.py         # Pytest configuration
    ├── page_objects/       # Page object models
    └── test_*.py           # Test files
```

## Development Commands

```bash
# Activate virtual environment
source venv/bin/activate    # On Windows: venv\Scripts\activate

# Install dependencies (if not already installed)
pip install -r requirements.txt

# Install Playwright browsers (if not already installed)
playwright install

# Run all tests
pytest

# Run tests with specific markers
pytest -m "login"

# Run tests in parallel
pytest -n auto

# Run tests with detailed output
pytest -v

# Generate HTML report
pytest --html=reports/report.html

# Run tests with screenshots on failure
pytest --screenshot=on

# Run tests with video recording
pytest --video=on
```

## Environment Configuration

- **Virtual Environment**: The `venv/` directory is tracked in git for consistency
- **Environment Variables**: Use `.env` file for test configuration
- **Test Credentials**: Configure Gmail test account in `.env` file
- **Browser Settings**: Configurable via environment variables

## Security Considerations

- Never commit real Gmail credentials to the repository
- Use environment variables in `.env` file for test account credentials
- Create `.env.local` for actual credentials (this file should be gitignored)
- Consider using Gmail's test/sandbox environments when available
- Implement proper cleanup of test data after test runs
- Use app-specific passwords for Gmail authentication

## Important Notes

- The virtual environment (`venv/`) is included in the repository for consistency
- All dependencies are pre-installed in the virtual environment
- Playwright browsers are downloaded separately using `playwright install`
- Test reports are generated in the `reports/` directory
- Screenshots and videos from failed tests are saved in respective directories