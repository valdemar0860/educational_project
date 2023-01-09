from django.db.models.signals import pre_save, pre_delete
from django.dispatch import receiver, Signal

from home.models import Student


@receiver(pre_save, sender=Student)
def normalize_name(sender, instance, **kwargs):
    instance.normalized_name = instance.name.lower()


@receiver(pre_delete, sender=Student)
def normalize_name(sender, instance, **kwargs):
    # print('delete student')
    # return None
    print(f'delete student {instance.id}')
    raise Exception('don`t delete')

# student_done = Signal()
#
#
# @receiver(student_done)
# def send_name(sender):
#     print("Student already done")
