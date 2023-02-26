@pytest.mark.regression
# тест вне класса: отступа нет
def test_student_can_see_lesson_name_in_lesson_in_course_after_joining(self, driver):
    # все строки внутри теста с отступом
    page = CoursePromoPage(url=self.course.url, driver=driver)
    page.open()


class TestLessonNameInCourseForTeacher():
    @pytest.mark.regression
    # тест внутри класса, нужен дополнительный отступ
    def test_teacher_can_see_lesson_name_in_lesson_in_course(self, driver):
        # еще один отступ для каждой строки, и так с любым уровнем вложенности
        page = LessonPlayerPage(url=self.lesson_url, driver=driver)
        page.open()
        try:
            # плюс один отступ на каждый уровень вложенности
            dangerous_function()
        except:
            close_something()
