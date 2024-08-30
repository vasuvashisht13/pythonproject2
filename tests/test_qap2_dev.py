def test_google_search(py):
    py.visit("https://google.com")
    py.get("[name='q']").type("Pylenium")
    py.get("[name='btnK']").submit()
    assert py.should().contain_title("Pylenium")