"""Минимальный пакет онлайн школы."""

from .students import Student
from .courses import Course
from .tests import Test
from .school import School

__all__ = ["Student", "Course", "Test", "School"]
