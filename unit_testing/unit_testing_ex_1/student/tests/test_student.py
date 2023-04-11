from unittest import TestCase, main
from project.student import Student


class TestStudent(TestCase):

    def setUp(self):
        self.student_wo_course = Student("Sonya")
        self.student_with_course = Student("Sonya", {"python": ["some notes"]})

    def test_initializing(self):
        self.assertEqual("Sonya", self.student_wo_course.name)
        self.assertEqual({}, self.student_wo_course.courses)
        self.assertEqual({"python": ["some notes"]}, self.student_with_course.courses)

    def test_if_notes_are_successfully_added_and_return_correctness(self):
        result_from_method = self.student_with_course.enroll("python", ["additional notes"])
        self.assertEqual("Course already added. Notes have been updated.", result_from_method)

        expected_notes = ["some notes", "additional notes"]
        resultative_notes = self.student_with_course.courses['python']
        self.assertEqual(expected_notes, resultative_notes)

    def test_adding_course_notes_successfully(self):
        result_1 = self.student_with_course.enroll("math", ["operators_notes"], "Y")
        self.assertEqual("Course and course notes have been added.", result_1)
        self.assertEqual(["operators_notes"], self.student_with_course.courses["math"])

        result_2 = self.student_with_course.enroll("english", ["letters"])
        self.assertEqual("Course and course notes have been added.", result_2)
        self.assertEqual(["letters"], self.student_with_course.courses["english"])

    def test_adding_the_course_name_without_adding_notes(self):
        result = self.student_wo_course.enroll("python", "", "no")
        self.assertEqual("Course has been added.", result)
        self.assertEqual([], self.student_wo_course.courses["python"])

    def test_add_notes_on_existing_course(self):
        result = self.student_with_course.add_notes("python", "unittesting")
        self.assertEqual("Notes have been updated", result)
        self.assertEqual(["some notes", "unittesting"], self.student_with_course.courses["python"])

    def test_add_notes_to_non_existing_course_raise_exception(self):
        with self.assertRaises(Exception) as ex:
            self.student_wo_course.add_notes("python", "iterators")
        self.assertEqual("Cannot add notes. Course not found.", str(ex.exception))

    def test_leaving_existing_course(self):
        result = self.student_with_course.leave_course("python")
        self.assertEqual("Course has been removed", result)
        with self.assertRaises(KeyError):
            result = self.student_with_course.courses["python"]

    def test_leaving_non_existing_course_raise_exception(self):
        with self.assertRaises(Exception) as ex:
            self.student_wo_course.leave_course("python")
        self.assertEqual("Cannot remove course. Course not found.", str(ex.exception))

        with self.assertRaises(Exception) as ex:
            self.student_with_course.leave_course("literature")
        self.assertEqual("Cannot remove course. Course not found.", str(ex.exception))

if __name__ == '__main__':
    main()