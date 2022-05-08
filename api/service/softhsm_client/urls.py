from django.urls import path
from .views import KeyManagement, TestAuthentication

app_name = "softhsm_client"
urlpatterns = [
    path(
        "key-management/dummy/",
        view=KeyManagement.as_view(),
        name="softhsm_client_hello",
    ),
    path(
        "test-authentication/test",
        view=TestAuthentication.as_view(),
        name="test_authentication",
    ),
]
