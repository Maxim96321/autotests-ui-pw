import pytest
from pages.courses.create_course_page import CreateCoursePage
from pages.courses.courses_list_page import CoursesListPage


@pytest.mark.regression
@pytest.mark.courses
class TestCourses:

    def test_empty_courses_list(self, courses_list_page_with_state: CoursesListPage):
        courses_list_page_with_state.visit(
            "https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses")

        courses_list_page_with_state.navbar.check_visible("username")
        courses_list_page_with_state.sidebar.check_visible()

        courses_list_page_with_state.toolbar_view.check_visible()
        courses_list_page_with_state.check_visible_empty_view()

    def test_create_course(self, create_course_page: CreateCoursePage, courses_list_page):
        create_course_page.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses/create")
        create_course_page.check_visible_create_course_title()
        create_course_page.check_disabled_create_course_button()
        create_course_page.image_upload_widget.check_visible(is_image_uploaded=False)
        create_course_page.check_visible_create_course_form(title="", max_score="0", min_score="0", description="",
                                                            estimated_time="")
        create_course_page.check_visible_exercises_title()
        create_course_page.check_visible_create_exercise_button()
        create_course_page.check_visible_exercises_empty_view()
        create_course_page.image_upload_widget.upload_preview_image(
            "C:/Cours Playwrite/autotest-ui-pw/testdata/files/IMG_4866.png")
        create_course_page.image_upload_widget.check_visible(is_image_uploaded=True)
        create_course_page.fill_create_course_form(title="Playwright",
                                                   estimated_time="2 weeks",
                                                   description="Playwright",
                                                   max_score="100",
                                                   min_score="10")
        create_course_page.click_create_course_button()

        courses_list_page.toolbar_view.check_visible()
        courses_list_page.course_view.check_visible(index=0, title="Playwright", max_score="100", min_score="10",
                                                    estimated_time="2 weeks")

    def test_edit_course(self, courses_list_page: CoursesListPage, create_course_page: CreateCoursePage):
        create_course_page.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses/create")
        create_course_page.image_upload_widget.upload_preview_image("./testdata/files/IMG_4866.png")
        create_course_page.image_upload_widget.check_visible(is_image_uploaded=True)
        create_course_page.fill_create_course_form(
            title="Playwright",
            estimated_time="2 weeks",
            description="Playwright",
            max_score="100",
            min_score="10"
        )
        create_course_page.click_create_course_button()

        courses_list_page.toolbar_view.check_visible()
        courses_list_page.course_view.check_visible(
            index=0, title="Playwright", max_score="100", min_score="10", estimated_time="2 weeks"
        )
        courses_list_page.course_view.menu.click_edit(index=0)

        create_course_page.fill_create_course_form(
            title="New Playwright",
            estimated_time="3 weeks",
            description="New Playwright",
            max_score="1000",
            min_score="100"
        )
        create_course_page.click_create_course_button()

        courses_list_page.toolbar_view.check_visible()
        courses_list_page.course_view.check_visible(
            index=0, title="New Playwright", max_score="1000", min_score="100", estimated_time="3 weeks"
        )