from pylenium.driver import Pylenium

def test_fill_out_form(py: Pylenium):
    # Open the DemoQA website
    py.visit("https://demoqa.com/")

    # Click on the 'Forms' link within the .category-cards container using XPath
    py.get(".home-body").contains("Forms").click()


    # Click on 'Practice Form'
    py.get(".left-pannel").contains("Practice Form").click()

    # Fill out the form fields
    py.get("#firstName").type("John")
    py.get("#lastName").type("Doe")
    py.get("#userEmail").type("john.doe@example.com")

    # Select gender
    py.get("label[for='gender-radio-1']").click()  # Male
    py.get("#userNumber").type("1234567890")

    # Select date of birth
    py.get("#dateOfBirthInput").click()
    py.get(".react-datepicker__month-select").select_option("August")
    py.get(".react-datepicker__year-select").select_option("1990")
    py.get(".react-datepicker__day--030").click()  # Select a specific day

    # Enter address
    py.get("#currentAddress").type("123 Elm Street")

    # Submit the form
    py.get("#submit").click()

    # Verify successful submission
    py.get(".modal-title").should().contain_text("Thanks for submitting the form")
