from unittest import TestCase

from project.student_report_card import StudentReportCard

class StudentReportTest(TestCase):
    def setUp(self):
        self.card = StudentReportCard("Sonya", 11)

    def test_init_correctness(self):
        self.assertEqual("Sonya", self.card.student_name)
        self.assertEqual(11, self.card.school_year)
        self.assertEqual({}, self.card.grades_by_subject)

    def test_school_year_raises(self):
        with self.assertRaises(ValueError) as error:
            self.card = StudentReportCard("Sonya", 22)
        self.assertEqual("School Year must be between 1 and 12!", str(error.exception))

        with self.assertRaises(ValueError) as error:
            self.card = StudentReportCard("Sonya", -1)
        self.assertEqual("School Year must be between 1 and 12!", str(error.exception))

    def test_successful_year_setting(self):
        self.card.school_year = 1
        self.assertEqual(1, self.card.school_year)

        self.card.school_year += 1
        self.assertEqual(2, self.card.school_year)

        self.card.school_year = 12
        self.assertEqual(12, self.card.school_year)

    def test_student_name_raises(self):
        with self.assertRaises(ValueError) as error:
            self.card = StudentReportCard("", 12)
        self.assertEqual("Student Name cannot be an empty string!", str(error.exception))

    def test_successful_name_setting(self):
        self.card.student_name = "Sonya"
        self.assertEqual("Sonya", self.card.student_name)

        self.card.student_name = "  Sonya "
        self.assertEqual("  Sonya ", self.card.student_name)

    def test_add_grade_by_subject(self):
        self.assertEqual({}, self.card.grades_by_subject)
        self.card.add_grade("Math", 6.00)
        self.assertEqual({"Math": [6.00]}, self.card.grades_by_subject)

        self.card.add_grade("Math", 5.50)
        self.assertEqual({"Math": [6.00, 5.50]}, self.card.grades_by_subject)

        self.card.add_grade("History", 5.00)
        self.assertEqual({"Math": [6.00, 5.50], "History": [5.00]}, self.card.grades_by_subject)

    def test_average_grade_return_report_for_each_subject(self):
        self.card.add_grade("Math", 6.00)
        self.card.add_grade("Math", 5.00)
        self.card.add_grade("History", 6.00)
        result = self.card.average_grade_by_subject()

        self.assertEqual("Math: 5.50\n"
                         "History: 6.00", result)

    def test_average_grade_for_all_subjects_return_str(self):
        self.card.add_grade("Math", 6.00)
        self.card.add_grade("Math", 5.00)
        self.card.add_grade("History", 6.00)
        result = self.card.average_grade_for_all_subjects()

        self.assertEqual(f"Average Grade: 5.67", result)

    def test_repr_return_report_student_grades(self):
        self.card.add_grade("Math", 6.00)
        self.card.add_grade("Math", 5.00)
        self.card.add_grade("History", 6.00)

        result = repr(self.card)
        expected = "Name: Sonya\n" \
                 "Year: 11\n" \
                 "----------\n" \
                 "Math: 5.50\nHistory: 6.00\n" \
                 "----------\n" \
                 "Average Grade: 5.67"

        self.assertEqual(expected, result)