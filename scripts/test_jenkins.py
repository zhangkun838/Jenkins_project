import allure


class TestJenkins:

    def test_01(self):
        assert 1

    @allure.severity("critical")
    def test_02(self):
        allure.attach(body="jeitu", name="test_02的文字描述：", attachment_type=allure.attachment_type.TEXT)
        assert 0
        allure.attach(body=self.driver.get_screenshot_as_png(), name="test_02的截图：",
                      attachment_type=allure.attachment_type.PNG)

    def test_03(self):
        assert 1
