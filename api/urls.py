from django.contrib import admin
from django.urls import path

from .views import DoctorView, AnalyticsView
from .views import ServiceView
from .views import VisitView
from .views import PatientViews
# from rest_framework.authtoken import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,)

urlpatterns = [
    path(
        'doctor/',
        DoctorView.as_view({
            'get': 'list',
            'post': 'create'
        })
    ),
    path(
        'doctor/<int:id>/',
        DoctorView.as_view({
            'get': 'retrieve',
            'put': 'update',
            'delete': 'destroy'
        })
    ),
    path(
        'doctor/<int:id>/patient',
        DoctorView.as_view({
            'get': 'list_patient',
        })
    ),
    path(
        'patient/',
        PatientViews.as_view({
            'get': 'list',
            'post': 'create'
        })
    ),
    path(
        'patient/<int:id>/',
        PatientViews.as_view({
            'get': 'retrieve',
            'put': 'update',
            'delete': 'destroy'
        })
    ),
    path(
        'service/',
        ServiceView.as_view({
            'get': 'list',
            'post': 'create'
        })
    ),
    path(
        'service/<int:id>/',
        ServiceView.as_view({
            'get': 'retrieve',
            'put': 'update',
            'delete': 'destroy'
        })
    ),
    path(
        'analytics/',
        AnalyticsView.as_view({
            'get': 'get_analytics',
        })
    ),
    path(
        'visit/',
        VisitView.as_view({
            'post': 'create'
        })
    ),
    path(
        'visit/<int:id>/rating',
        VisitView.as_view({
            'put': 'set_rating'
        })
    ),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]










# from .views import DoctorListCreateView
# from .views import ServiceListCreateView
# from .views import PatientListCreateView
# from .views import VisitListCreateView
#
# urlpatterns = [
#     path('service/', ServiceListCreateView.as_view()),
#     path('doctor/', DoctorListCreateView.as_view()),
#     path('patient/', PatientListCreateView.as_view()),
#     path('visit/', VisitListCreateView.as_view())
# ]