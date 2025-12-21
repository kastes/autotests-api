import pytest


@pytest.mark.smoke
class TestLogin:
    @pytest.mark.smoke
    def test_valid_login(self):
        pass

    @pytest.mark.regression
    def test_invalid_login(self):
        pass


@pytest.mark.regression
class TestRegistration:
    @pytest.mark.regression
    def test_valid_registration(self):
        pass

    @pytest.mark.smoke
    def test_invalid_registration(self):
        pass


@pytest.mark.smoke
@pytest.mark.regression
class TestCheckout:
    @pytest.mark.smoke
    @pytest.mark.regression
    def test_valid_checkout(self):
        pass

    def test_invalid_checkout(self):
        pass


def test_search():
    pass
