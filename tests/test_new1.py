from pylenium.driver import Pylenium

def test_demoqa_navigation(py: Pylenium):
    # Open the DemoQA website
    py.visit("https://demoqa.com/")

    # Click on the 'Elements' link using the specific CSS selector
    py.get("div.category-cards div:nth-child(1) div:nth-child(1) div:nth-child(3) h5").click()

    # Click on 'Text Box' using a text-based selector
    py.get("body > div:nth-child(7) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > ul:nth-child(1) > li:nth-child(1)").click()

    # Fill in the 'Full Name' field
    py.get("#userName").should().be_visible().type("John Doe")

    # Verify the 'Full Name' field value
    assert py.get("#userName").get_attribute("value") == "John Doe"
