from django.http import HttpResponse
from django.shortcuts import render, redirect

from home.forms import StudentForm
from home.models import Student


def show_all_students(request):
    """
    Show all students in template
    """
    # выбрать всех студентов из таблицы students(джанго сама
    # дописывает `s` в окончании таблицы, но модели всегда должны
    # быть в единственном числе)
    students = Student.objects.all()

    # для рендеринга темплейта нужно использовать render
    # эта функция принимает минимум два параметра request, template_name
    return render(
        request=request,
        template_name='index.html',
        context={
            'students': students,
        }
    )


def create_student(request):
    """
    Create student by student's name
    """
    # все GET параметры хранятся в request.GET
    student_name_from_request = request.GET.get('name')

    if not student_name_from_request:
        return HttpResponse('Student name missing')

    # Чтобы создать нового юзера нужно инициализировать Модель
    student = Student()
    # далее сохраняем параметры в объект модели
    student.name = student_name_from_request
    # сохранение
    student.save()

    return HttpResponse('Student {} have been created'.format(student.name))


def create_student_by_form(request):
    """
    Create student by Django Forms
    """
    if request.method == 'GET':
        # генерируем форму
        student_form = StudentForm()

        # добавляем форму в контекст
        context = {
            'student_form': student_form,
        }

        return render(request, 'student_form.html', context=context)

    elif request.method == 'POST':

        # получаем данные с формы
        student_form = StudentForm(request.POST)
        # сохраняем данные в таблицу
        # если все валидно
        if student_form.is_valid():
            student_form.save()

        return redirect('/students/form/create')


def update_student(request, id):
    if request.method == 'GET':
        student = Student.objects.get(id=id)

        student_form = StudentForm(instance=student)

        context = {
            'student_id': student.id,
            'form': student_form,
        }

        return render(
            request,
            'update.html',
            context=context
        )

    elif request.method == 'POST':

        student = Student.objects.get(id=id)

        student_form = StudentForm(request.POST, instance=student)

        if student_form.is_valid():
            student_form.save()

        return redirect(f'/students/update/{student.id}')