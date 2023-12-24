from django.urls import path
from .views import AirplaneView


urlpatterns = [
    path('airplane/', AirplaneView.as_view(), name='airplane-api'),
]
