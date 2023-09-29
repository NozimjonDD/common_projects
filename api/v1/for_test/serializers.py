from rest_framework.serializers import ModelSerializer

from for_test.models import Teacher, Student


class StudentListSerializer(ModelSerializer):
    class Meta:
        model = Student
        fields = [
            'id',
            'teacher',
            'name',
            'course',
        ]
        extra_kwargs = {
            'name': {'required': True},
            'course': {'required': False},
        }


class TeacherCreateSeializer(ModelSerializer):
    # students = serializers.ListField(
    #     child=serializers.DictField(
    #         allow_null=True,
    #     ),
    #     required=False,
    #     write_only=True,
    #     allow_empty=True
    # )

    class Meta:
        model = Teacher
        fields = [
            'id',
            'name',
            'course',
            # 'students'
        ]
        extra_kwargs = {
            'name': {'required': True},
            'course': {'required': True},
        }

    def to_representation(self, instance: Teacher):
        response = super().to_representation(instance)
        response['students'] = StudentListSerializer(instance.student_set.all().order_by('created_at'), many=True).data
        return response
