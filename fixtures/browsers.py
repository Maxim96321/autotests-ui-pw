import pytest
from playwright.sync_api import Page, Playwright
from _pytest.fixtures import SubRequest
from pages.authentification.registration_page import RegistrationPage
import allure
from config import settings
from tools.playwright.mocks import mock_static_resources


@pytest.fixture
def chromium_page(request: SubRequest, playwright: Playwright) -> Page:
    browser = playwright.chromium.launch(headless=settings.headless)
    context = browser.new_context(record_video_dir=settings.videos_dir)
    context.tracing.start(screenshots=True, snapshots=True, sources=True)
    page = context.new_page()
    mock_static_resources(page)

    yield page

    context.tracing.stop(path=f'./tracing/{request.node.name}.zip')
    #context.tracing.stop(path=settings.tracing_dir.joinpath(f'{test_name}.zip'))
    browser.close()
    allure.attach.file(f'./tracing/{request.node.name}.zip', name='trace', extension='zip')
    allure.attach.file(page.video.path(), name="video", attachment_type=allure.attachment_type.WEBM)


@pytest.fixture(scope="session")
def initialize_browser_state(playwright: Playwright):
    browser = playwright.chromium.launch(headless=settings.headless)
    context = browser.new_context()

    page = context.new_page()
    mock_static_resources(page)

    registration_page = RegistrationPage(page=page)
    registration_page.visit('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration')
    registration_page.registration_form.fill(email='user.@gmail.com', username='username', password='password')
    registration_page.click_registration_button()

    context.storage_state(path="browser-state.json")
    browser.close()


@pytest.fixture()
def chromium_page_with_state(initialize_browser_state, request: SubRequest, playwright: Playwright) -> Page:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context(storage_state=settings.browser_state_file, record_video_dir=settings.videos_dir)

    context.tracing.start(screenshots=True, snapshots=True, sources=True)
    page = context.new_page()

    yield page
    context.tracing.stop(path=f'./tracing/{request.node.name}.zip ')
    browser.close()
    allure.attach.file(f'./tracing/{request.node.name}.zip', name='trace', extension='zip')
    allure.attach.file(page.video.path(), name="video", attachment_type=allure.attachment_type.WEBM)
