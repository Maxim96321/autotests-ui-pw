from enum import Enum


class AllureEpic(str, Enum):
    LMS = "Lms system"
    STUDENT = "Student system"
    ADMINISTRATION = "Administration system"
