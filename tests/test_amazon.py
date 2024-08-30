def test_about_menu_has_3_links(py):
    py.visit("https://qap.dev")

    # Find the 'About' link and hover over it
    about = py.get("a[href='/about']")
    about.hover()

    # Find the dropdown menu that appears after hovering
    dropdown_menu = py.get(".Header-nav-folder")

    # Assert that there are 3 links in the dropdown menu
    assert dropdown_menu.find("a").should().have_length(3)
