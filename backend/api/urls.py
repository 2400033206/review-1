from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import StudentViewSet, CounsellorViewSet, AppointmentViewSet

router = DefaultRouter()
router.register('students', StudentViewSet)
router.register('counsellors', CounsellorViewSet)
router.register('appointments', AppointmentViewSet)

urlpatterns = [
    path('', include(router.urls)),
]