from rest_framework.serializers import ModelSerializer

from for_test.models import RequestCheckingCreation


class SiteRequestCheckingCreationSeializer(ModelSerializer):
    class Meta:
        model = RequestCheckingCreation
        fields = [
            'id',
            'cross_id',
            'cross_setting_id',
            'cross_title',
            'data',
        ]

    def create(self, validated_data):
        print(validated_data)
        # phase_direction_numbers = json.loads(validated_data.pop('phase_direction_numbers', []))
        instance = super().create(validated_data)
        return instance
