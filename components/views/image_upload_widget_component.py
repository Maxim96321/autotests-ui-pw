from components.base_component import BaseComponent
from playwright.sync_api import Page, expect

from components.views.emply_view_component import EmptyViewComponent


class ImageUploadWidgetComponent(BaseComponent):
    def __init__(self, page: Page, identifier: str):
        super().__init__(page)

        self.preview_empty_view = EmptyViewComponent(page, identifier)

        self.preview_image = page.get_by_test_id("create-course-preview-image-upload-widget-preview-image")

        self.preview_image_upload_icon = page.get_by_test_id("create-course-preview-image-upload-widget-info-icon")
        self.preview_image_upload_title = page.get_by_test_id(
            "create-course-preview-image-upload-widget-info-title-text")
        self.preview_image_upload_description = page.get_by_test_id(
            "create-course-preview-image-upload-widget-info-description-text")

        self.preview_image_upload_button = page.get_by_test_id(
            "create-course-preview-image-upload-widget-upload-button")
        self.preview_image_remove_button = page.get_by_test_id(
            "create-course-preview-image-upload-widget-remove-button")
        self.preview_image_upload_input = page.get_by_test_id("create-course-preview-image-upload-widget-input")


