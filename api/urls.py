from .views import GetUserDetails
from django.urls import path

urlpatterns = [
    path("userlist/", GetUserDetails.as_view(), name='user-details')
]

