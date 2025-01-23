from rest_framework import serializers

from .models import Doctor
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

class VisitCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Visit
        fields = '__all__'

class VisitUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Visit
        fields = '__all__'

class VisitListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Visit
        fields = '__all__'




















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