from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, mixins, filters
from rest_framework.permissions import IsAuthenticated
from .filters import DoctorFilterSet

# from yaml import serialize

from .models import Doctor, Patient, Service, Visit
from rest_framework.response import Response

from .permissions import DoctorAccessPermissions
from .serializers import DoctorListSerializer, DoctorRetrieveSerializer, DoctorCreateSerializer, DoctorUpdateSerializer, \
    PatientListSerializer, PatientDetailedSerializer, PatientCreateOrUpdateSerializer
from .serializers import ServiceRetrieveSerializer, ServiceCreateSerializer, ServiceUpdateSerializer, ServiceListSerializer
from .serializers import VisitRetrieveSerializer, VisitCreateSerializer, VisitUpdateSerializer, VisitListSerializer

class DoctorView(
    viewsets.GenericViewSet,
    mixins.ListModelMixin,
    mixins.UpdateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.CreateModelMixin,
    mixins.DestroyModelMixin
):

    lookup_field = 'id'
    permission_classes = [IsAuthenticated, DoctorAccessPermissions]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['first_name', 'last_name', 'speciality']
    filterset_class = DoctorFilterSet

    def get_action_permissions(self):
        if self.action in ('list', 'retrieve'):
            self.action_permissions = ['view_doctor', ]
        elif self.action == 'list_patient':
            self.action_permissions = ['view_patient', ]
        else:
            self.action_permissions = []

    def get_serializer_class(self):
        if self.action == 'list':
            return DoctorListSerializer
        if self.action == 'retrieve':
            return DoctorRetrieveSerializer
        if self.action == 'create':
            return DoctorCreateSerializer
        if self.action == 'update':
            return DoctorUpdateSerializer
        if self.action == 'list_patient':
            return PatientListSerializer

    def get_queryset(self):
        if self.action == 'list_patient':
            return Patient.objects.prefetch_related(
                'visits'
            ).all()
        return Doctor.objects.all()

    def list_patient(self, request, id):
        queryset = self.get_queryset().filter(visits__doctor_id=id).all()
        serializer = self.get_serializer(queryset, many=True)

        return Response(data=serializer.data)

class ServiceView(
    viewsets.GenericViewSet,
    mixins.ListModelMixin,
    mixins.UpdateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.CreateModelMixin,
    mixins.DestroyModelMixin
):

    lookup_field = 'id'

    def get_serializer_class(self):
        if self.action == 'list':
            return ServiceListSerializer
        if self.action == 'retrieve':
            return ServiceRetrieveSerializer
        if self.action == 'create':
            return ServiceCreateSerializer
        if self.action == 'update':
            return ServiceUpdateSerializer

    def get_queryset(self):
        return Service.objects.all()

class VisitView(
    viewsets.GenericViewSet,
    mixins.ListModelMixin,
    mixins.UpdateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.CreateModelMixin,
    mixins.DestroyModelMixin
):

    lookup_field = 'id'

    def get_serializer_class(self):
        if self.action == 'list':
            return VisitListSerializer
        if self.action == 'retrieve':
            return VisitRetrieveSerializer
        if self.action == 'create':
            return VisitCreateSerializer
        if self.action == 'update':
            return VisitUpdateSerializer

    def get_queryset(self):
        return Visit.objects.all()

class PatientViews(
    viewsets.GenericViewSet,
    mixins.ListModelMixin,
    mixins.UpdateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.CreateModelMixin,
    mixins.DestroyModelMixin
):
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['gender']
    search_fields = ['first_name', 'last_name']

    def get_action_permissions(self):
        if self.action in ('list', 'retrieve'):
            self.action_permissions = ['view_patient', ]
        elif self.action == 'create':
            self.action_permissions = ['add_patient', ]
        elif self.action == 'update':
            self.action_permissions = ['change_patient', ]
        elif self.action == 'destroy':
            self.action_permissions = ['delete_patient', ]


    def get_serializer_class(self):
        if self.action == 'list':
            return PatientListSerializer
        if self.action == 'retrieve':
            return PatientDetailedSerializer
        if self.action == 'create':
            return PatientCreateOrUpdateSerializer
        if self.action == 'update':
            return PatientCreateOrUpdateSerializer

    def get_queryset(self):
        return Patient.objects.all()










# from rest_framework import generics
#
# from .models import Service
# from .serializers import ServiceSerializer
# from .models import Doctor
# from .serializers import DoctorSerializer
# from .models import Patient
# from .serializers import PatientSerializer
# from .models import Visit
# from .serializers import VisitSerializer
#
# class ServiceListCreateView(generics.ListCreateAPIView):
#     queryset = Service.objects.all()
#     serializer_class = ServiceSerializer
#
# class DoctorListCreateView(generics.ListCreateAPIView):
#     queryset = Doctor.objects.all()
#     serializer_class = DoctorSerializer
#
# class PatientListCreateView(generics.ListCreateAPIView):
#     queryset = Patient.objects.all()
#     serializer_class = PatientSerializer
#
# class VisitListCreateView(generics.ListCreateAPIView):
#     queryset = Visit.objects.all()
#     serializer_class = VisitSerializer