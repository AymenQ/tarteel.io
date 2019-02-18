from django.urls import path, include

from rest_framework import routers
from . import views

router = routers.DefaultRouter()

router.register('recordings', views.AnnotatedRecordingViewSet)
# And all new api endpoints, e.g.:
#router.register('evaluations', views.EvaluationViewSet)
#router.register('demographics', views.DemographicViewSet)

urlpatterns = [
    path('', include(router.urls))
]
