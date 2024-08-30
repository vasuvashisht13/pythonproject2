def test_element_is_visible(py):
    py.visit("https://qap.dev")
    assert py.get("a[href='/about']").should().be_visible()