# Gmail E2E Test Plan

## Testing Strategy Overview

This document outlines the comprehensive testing strategy for Gmail end-to-end automation using a **hybrid approach** that combines dedicated authentication testing with integrated workflow validation.

## Testing Approach Rationale

### Why Hybrid Testing?

**Dedicated Authentication Tests** provide:
- ✅ Isolated debugging of login issues
- ✅ Comprehensive edge case coverage
- ✅ Fast feedback loops
- ✅ Clear error identification

**Integrated Workflow Tests** provide:
- ✅ Real-world user scenario validation
- ✅ Performance testing with authentication overhead
- ✅ Complete user journey verification
- ✅ End-to-end system validation

## Test Suite Architecture

### 1. Foundation Tests (Implemented)

#### Smoke Tests (`tests/test_smoke.py`)
- **Purpose**: Verify basic system availability
- **Scope**: Page loading, element presence
- **Execution**: Fast, runs first in pipeline
- **Markers**: `@pytest.mark.smoke`

### 2. Authentication Tests (Planned)

#### Dedicated Login Tests (`tests/test_login.py`)
**Test Cases:**
```python
@pytest.mark.login
def test_gmail_login_valid_credentials()
    # Verify successful login with valid email/password

@pytest.mark.login  
def test_gmail_login_invalid_email()
    # Verify proper error handling for invalid email

@pytest.mark.login
def test_gmail_login_invalid_password()
    # Verify proper error handling for wrong password

@pytest.mark.login
def test_gmail_login_app_specific_password()
    # Verify login with app-specific password

@pytest.mark.login
def test_gmail_login_two_factor_authentication()
    # Verify 2FA authentication flow

@pytest.mark.login
def test_gmail_session_persistence()
    # Verify session maintains across page reloads

@pytest.mark.login
def test_gmail_logout_functionality()
    # Verify proper logout and session termination
```

**Coverage Areas:**
- Valid credentials authentication
- Invalid credentials error handling
- App-specific password authentication
- Two-factor authentication flows
- Session management and persistence
- Logout functionality
- Error message validation
- Security timeout handling

### 3. Email Workflow Tests (Planned)

#### Email Composition Tests (`tests/test_email_compose.py`)
**Test Cases:**
```python
@pytest.mark.email
def test_compose_basic_email(authenticated_page)
    # Login → Compose → Send basic email

@pytest.mark.email
def test_compose_email_with_attachment(authenticated_page)
    # Login → Compose → Add attachment → Send

@pytest.mark.email
def test_save_draft(authenticated_page)
    # Login → Compose → Save as draft → Verify saved

@pytest.mark.email
def test_compose_with_formatting(authenticated_page)
    # Login → Compose with rich text → Send
```

#### Email Search Tests (`tests/test_email_search.py`)
**Test Cases:**
```python
@pytest.mark.email
def test_search_by_sender(authenticated_page)
    # Login → Search emails by sender

@pytest.mark.email
def test_search_by_subject(authenticated_page)
    # Login → Search emails by subject

@pytest.mark.email
def test_advanced_search_filters(authenticated_page)
    # Login → Use advanced search options
```

#### Email Management Tests (`tests/test_email_management.py`)
**Test Cases:**
```python
@pytest.mark.email
def test_archive_email(authenticated_page)
    # Login → Select email → Archive

@pytest.mark.email
def test_organize_with_labels(authenticated_page)
    # Login → Apply labels to emails

@pytest.mark.email
def test_delete_email(authenticated_page)
    # Login → Delete email → Verify removal
```

### 4. Shared Utilities (Planned)

#### Authentication Fixtures (`tests/fixtures/auth_fixtures.py`)
```python
@pytest.fixture
def authenticated_page(page, test_credentials):
    """Provides a page already logged into Gmail"""
    # Handles login process
    # Returns authenticated page ready for email operations

@pytest.fixture
def login_page(page):
    """Provides a page at the Gmail login screen"""
    # Navigates to login page
    # Returns page ready for authentication testing

@pytest.fixture
def fresh_inbox(authenticated_page):
    """Provides authenticated page with clean inbox state"""
    # Ensures consistent test data state
```

## Test Execution Strategy

### Test Pyramid Implementation

```
    /\     E2E Workflow Tests (Few)
   /  \    - Complete user journeys
  /____\   - Login + Email operations
 /      \  
/________\  Integration Tests (Some)
           - Authentication flows
           - Individual feature testing
           
_______________ Unit/Smoke Tests (Many)
               - Page loading
               - Element presence
```

### Test Markers and Organization

```python
# pytest.ini markers
markers =
    smoke: Basic functionality verification
    login: Authentication and session tests  
    email: Email workflow functionality
    compose: Email composition features
    search: Email search functionality
    management: Email organization features
    slow: Tests that take longer to execute
```

### Execution Priorities

1. **Smoke Tests** - Run first, fail fast
2. **Authentication Tests** - Verify login before workflows
3. **Workflow Tests** - Full feature validation
4. **Performance Tests** - Login overhead validation

## Test Data Management

### Test Accounts
- **Primary Test Account**: Main Gmail account for testing
- **Secondary Test Account**: For email sending/receiving tests
- **App-Specific Passwords**: For authentication testing

### Test Data Strategy
- **Cleanup**: Automated cleanup after each test
- **Isolation**: Each test operates independently
- **Fixtures**: Shared test data through pytest fixtures

## Implementation Priority

### Phase 1: Foundation (✅ Complete)
- Smoke tests
- Basic page validation
- Test infrastructure setup

### Phase 2: Authentication (🔄 Next)
- Dedicated login tests
- Authentication fixtures
- Session management

### Phase 3: Core Workflows (📋 Planned)
- Email composition
- Basic email operations
- Search functionality

### Phase 4: Advanced Features (📋 Future)
- Email management
- Advanced search
- Performance testing

## Success Criteria

### Authentication Tests
- ✅ All login scenarios pass
- ✅ Error handling validated
- ✅ Session management verified
- ✅ Security features tested

### Workflow Tests  
- ✅ End-to-end user journeys validated
- ✅ Performance benchmarks met
- ✅ Real-world scenarios covered
- ✅ Integration points verified

### Overall Suite
- ✅ Fast feedback (< 5 minutes for critical path)
- ✅ Comprehensive coverage (>90% critical features)
- ✅ Reliable execution (>95% pass rate)
- ✅ Clear error reporting and debugging