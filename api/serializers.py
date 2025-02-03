from jsonschema.exceptions import ValidationError
from rest_framework import serializers

from .models import Doctor, Schedule
from .models import Service
from .models import Patient
from .models import Visit
from .models import Specialization




# class ServiceSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Service
#         fields = '__all__'

class DoctorListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = '__all__'

class DoctorRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = '__all__'

class DoctorCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = '__all__'

class DoctorUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = ['speciality', 'contact_info']

class PatientListSerializer(serializers.Serializer):
        id = serializers.IntegerField()
        full_name = serializers.CharField()
        date_of_birth = serializers.DateField()
        gender = serializers.CharField()

class PatientDetailedSerializer(PatientListSerializer):
    contact_info = serializers.CharField()

class PatientCreateOrUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = '__all__'

class ServiceRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = '__all__'

class ServiceCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = '__all__'

class ServiceUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = '__all__'
class ServiceListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = '__all__'



class VisitRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Visit
        fields = '__all__'

# class VisitCreateSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Visit
#         fields = '__all__'

class VisitUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Visit
        fields = '__all__'

class VisitListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Visit
        fields = '__all__'





class VisitCreateSerializer(serializers.ModelSerializer):
    def validate_schedule(self, value):
        visit_count = value.visits.count()
        if 3 <= visit_count:
            raise ValidationError('Превышено количество мест')
        return value

    class Meta:
        model = Visit
        fields = ['patient', 'service', 'schedule']

class ScheduleSerializer(serializers.ModelSerializer):
    def validate(self, attrs):
        attrs = super().validate(attrs)
        timestamp_start, timestamp_end = attrs['timestamp_start'], ['timestamp_end']

        exists = Schedule.objects.filter(
            timestamp_start__lte=timestamp_start,
            timestamp_end__gte=timestamp_end
        ).exists()

        if exists:
            raise ValidationError("Уже есть запись на это время, произошла накладка")

class VisitRatingSerializer(serializers.ModelSerializer):
    rating = serializers.IntegerField(min_value=0, max_value=10)

    def validate_rating(self, value):
        if self.instance.rating_set:
            raise ValidationError("Вы уже ставили рейтинг")

    class Meta:
        model = Visit
        fields = ['rating']




















# class PatientSerializer(serializers.Serializer):
#     class Meta:
#         model = Patient
#         fields = '__all__'
#




# class VisitSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Visit
#         fields = '__all__'
#
# class SpecializationSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Specialization
#         fields = '__all__'
