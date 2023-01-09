from django.core.management.base import BaseCommand
from faker import Faker

from home.models import Student


# имя файла является название команды
# from home.signals import student_done


class Command(BaseCommand):

    # описание команды располагается в параметре help
    help = 'Add new student(s) to the system'

    # все аргументы парсяться в этом методе
    def add_arguments(self, parser):

        parser.add_argument('-l', '--len', type=int, default=2)

    # сама логика команды распологается здесь
    def handle(self, *args, **options):

        # для работы с Faker надо его заинициализировать
        faker = Faker()

        # для вывода информации о выполнении команды лучше использовать self.stdout.write вместо print
        # self.stdout.write('Start inserting Students')
        # students = Student.objects.all()
        # for student in students:
        #     print(student.name)
        for _ in range(options['len']):
            self.stdout.write('Start inserting Students')
            student = Student()
            # faker имеет большое количество разной генерируемой информации один из них name()
            student.name = faker.name()
            student.sex = faker.simple_profile()['sex']
            student.address = faker.address()
            student.description = faker.text()

            # student_done.send(sender=Student)
            # student.send_name()
            student.save()
        self.stdout.write('End inserting Students')
