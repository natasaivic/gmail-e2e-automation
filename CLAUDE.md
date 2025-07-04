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

This project is currently in initial setup phase. When implementing the automation framework, consider:

- **Testing Framework**: Choose between Playwright, Selenium, or Cypress for browser automation
- **Authentication**: Gmail login will require handling OAuth2 or app-specific passwords
- **Email Verification**: May need integration with email APIs or IMAP for receipt verification
- **Test Data Management**: Consider using test accounts and managing test email data
- **CI/CD Integration**: Design tests to run reliably in automated environments

## Development Commands

*To be populated once the testing framework is implemented*

## Security Considerations

- Never commit real Gmail credentials
- Use environment variables for test account credentials
- Consider using Gmail's test/sandbox environments when available
- Implement proper cleanup of test data after test runs