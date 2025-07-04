import pytest
import time
from playwright.sync_api import Page, expect

@pytest.mark.smoke
def test_gmail_page_loads(page: Page, gmail_base_url: str):
    """
    Smoke test: Verify Gmail page loads successfully.
    
    This is the foundational test that ensures:
    1. Browser can navigate to Gmail
    2. Page loads without errors
    3. Basic Gmail elements are present
    """
    # Navigate to Gmail
    page.goto(gmail_base_url)
    
    # Verify page loads successfully
    expect(page).to_have_title("Gmail")
    
    # Verify Gmail sign-in elements are present
    # Check for either the sign-in heading or email input field
    sign_in_heading = page.locator("h1:has-text('Sign in')")
    email_input_locator = page.locator("input[type='email']")
    
    # At least one of these should be visible
    assert sign_in_heading.is_visible() or email_input_locator.is_visible(), \
        "Neither sign-in heading nor email input field is visible"
    
    # Verify URL is either Gmail or Google accounts (expected redirect)
    assert "gmail.com" in page.url or "accounts.google.com" in page.url, \
        f"Expected URL to contain 'gmail.com' or 'accounts.google.com', got: {page.url}"
    
    # Take screenshot for verification
    page.screenshot(path="screenshots/gmail_page_loads.png")
    
    # Pause for 5 seconds to view results before browser closes
    print("🔍 Pausing for 5 seconds to view results...")
    time.sleep(5)

@pytest.mark.smoke
def test_gmail_page_basic_elements(page: Page, gmail_base_url: str):
    """
    Smoke test: Verify basic Gmail page elements are present.
    
    This test ensures critical page elements load correctly.
    """
    # Navigate to Gmail
    page.goto(gmail_base_url)
    
    # Wait for page to load
    page.wait_for_load_state("networkidle")
    
    # Check for Google branding or Gmail logo
    google_logo = page.locator("img[alt*='Google'], img[alt*='Gmail']")
    expect(google_logo).to_be_visible()
    
    # Verify page is responsive
    assert page.viewport_size["width"] > 0, "Page width should be greater than 0"
    assert page.viewport_size["height"] > 0, "Page height should be greater than 0"
    
    # Pause for 5 seconds to view results before browser closes
    print("🔍 Pausing for 5 seconds to view basic elements...")
    time.sleep(5)