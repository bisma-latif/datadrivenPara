from pytest import mark

class Testsbasic:

    def test_check_basic_search(test_data):
        print(f"{test_data} tested")

    @mark.skip
    def test_for_specific_browser(self, browser):
        browser.get("https://google.com")
        print("done")
