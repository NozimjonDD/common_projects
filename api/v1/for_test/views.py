from django.shortcuts import render
from rest_framework.exceptions import ValidationError
from rest_framework.generics import (
    CreateAPIView, UpdateAPIView
)
from rest_framework.permissions import AllowAny

from api.v1.for_test.serializers import TeacherCreateSeializer
from for_test.models import *


# class TeacherCreateAPIView(CreateAPIView):
#     permission_classes = [AllowAny, ]
#     queryset = Teacher.objects.all()
#     serializer_class = TeacherCreateSeializer


def home(request):
    return render(request, 'index.html')


class TeacherCreateAPIView(CreateAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherCreateSeializer

    def post(self, request, *args, **kwargs):
        students = self.request.data.get('students')
        instance = self.create(request, *args, **kwargs)

        teacher = self.queryset.last()
        Student.objects.bulk_create(
            [Student(**{'teacher': teacher, 'name': student.get('name'), 'course': student.get('course')})
             for student in students], batch_size=2
        )

        return instance


class TeacherUpdateAPIView(UpdateAPIView):
    permission_classes = [AllowAny, ]
    queryset = Teacher.objects.all()
    serializer_class = TeacherCreateSeializer

    def put(self, request, *args, **kwargs):
        students = self.request.data.get('students')
        instance = self.update(request, *args, **kwargs)

        students_list = []
        print(self.get_object())
        for student_item in students:
            print(student_item.get('id'))
            # student = self.get_object().student_set.get(id=student_item.get('id'))
            if not student_item.get('name') or student_item.get('course'):
                raise ValidationError("sz name yoki course maydonlaridan birini to'ldirmadiz")
            else:
                student, created = self.get_object().student_set.get_or_create(id=student_item.get('id'),
                                                                               defaults=dict(
                                                                                   name=student_item.get('name'),
                                                                                   course=student_item.get('course')))

            print(created)
            print(student.name)
            print(student_item, "==================")
            student.name = student_item.get('name')
            student.course = student_item.get('course')
            students_list.append(student)

        Student.objects.bulk_update(
            students_list,
            fields=['name', 'course'],
            # batch_size=4
        )

        return instance
