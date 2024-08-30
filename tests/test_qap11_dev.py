from pylenium.driver import Pylenium

# def test_verify_page_title(py: Pylenium):
#     py.visit("https://demoqa.com/")
#     assert py.title() == "DEMOQA"
#     print("Page title is correct.")


def test_navigation_to_elements(py: Pylenium):
    py.visit("https://demoqa.com/")
    elements_card = py.get('div.category-cards div:nth-child(1) div:nth-child(1) h5')
    assert "Elements" in elements_card.text()
    print("Navigated to Elements page successfully and text is correct.")


#app > div > div > div.home-body > div > div:nth-child(1) > div > div.card-body > h5

# def test_verify_text_on_elements_page(py: Pylenium):
#     py.visit("https://demoqa.com/elements")
#     assert py.find("div.main-header").text() == "Elements"
#     print("Text on Elements page is correct.")

# def test_fill_and_submit_form(py: Pylenium):
#     py.visit("https://demoqa.com/forms")
#     py.find("#firstName").type("John")
#     py.find("#lastName").type("Doe")
#     py.find("#userEmail").type("john.doe@example.com")
#     py.find("#age").type("30")
#     py.find("#salary").type("50000")
#     py.find("#department").type("Engineering")
#     py.find("button#submit").click()
#     assert py.find(".modal-body").text() == "Thanks for submitting the form"
#     print("Form submitted successfully.")
#
# def test_date_picker(py: Pylenium):
#     py.visit("https://demoqa.com/widgets")
#     py.find("#datePickerMonthYearInput").click()
#     py.find(".react-datepicker__month-select").select("August")
#     py.find(".react-datepicker__year-select").select("2024")
#     py.find(".react-datepicker__day--015").click()  # Selects the 15th day
#     selected_date = py.find("#datePickerMonthYearInput").get_attribute("value")
#     assert selected_date == "August 15, 2024"
#     print("Date Picker selection is correct.")

if __name__ == "__main__":
    from pylenium import Pylenium
    py = Pylenium()
    test_verify_page_title(py)
    test_navigation_to_elements(py)
    # test_verify_text_on_elements_page(py)
    # test_fill_and_submit_form(py)
    # test_date_picker(py)
