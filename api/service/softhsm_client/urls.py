from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import KeyManagement, TestAuthentication

app_name = "softhsm_client"

router = DefaultRouter()
router.register(r"key", KeyManagement, basename="key")

urlpatterns = [
    path(
        "",
        include(router.urls),
        name="softhsm_client_hello",
    ),
    path(
        "test-authentication/test",
        view=TestAuthentication.as_view(),
        name="test_authentication",
    ),
]
