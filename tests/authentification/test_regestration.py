import pytest
from pages.authentification.registration_page import RegistrationPage
from pages.dashboard.dashboard_page import DashboardPage


@pytest.mark.regression
@pytest.mark.regestration
class TestRegistration:
    def test_successful_registration(self, dashboard_page: DashboardPage, registration_page: RegistrationPage):
        registration_page.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")
        registration_page.registration_form.fill(email="user.name@gmail.com", username="max", password="password")
        registration_page.click_registration_button()
        dashboard_page.dashboard_toolbar_view_component.check_visible()
