import allure


class TestJenkins:

    def test_01(self):
        assert 0

    @allure.severity("critical")
    def test_02(self):
        assert 1

    def test_03(self):
        assert 1

if __name__ == '__main__':
    print("11")