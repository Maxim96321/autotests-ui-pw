from playwright.sync_api import Page

from pages.base_page import BasePage


class CreateCoursePage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        self.create_course_title = page.get_by_test_id("create-course-toolbar-title-text")
        self.create_course_button = page.get_by_test_id("create-course-toolbar-create-course-button")

        self.preview_image = page.get_by_test_id("create-course-preview-image-upload-widget-preview-image")
        self.preview_empty_icon = page.get_by_test_id("create-course-preview-empty-view-icon")
        self.preview_empty_title = page.get_by_test_id("create-course-preview-empty-view-title-text")
        self.preview_empty_description = page.get_by_test_id("create-course-preview-empty-view-description-text")

        self.preview_image_upload = page.get_by_test_id("create-course-preview-image-upload-widget-info-icon")
        self.preview_image_upload_title = page.get_by_test_id(
            "create-course-preview-image-upload-widget-info-title-text")
        self.preview_image_upload_description = page.get_by_test_id(
            "create-course-preview-image-upload-widget-info-description-text")

        self.preview_image_upload_button = page.get_by_test_id(
            "create-course-preview-image-upload-widget-upload-button")
        self.preview_image_remove_button = page.get_by_test_id(
            "create-course-preview-image-upload-widget-remove-button")
        self.preview_image_upload_input = page.get_by_test_id("create-course-preview-image-upload-widget-input")

