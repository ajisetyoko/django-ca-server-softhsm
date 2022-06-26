from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import KeyManagement, Test, LoginView
from knox import views as knox_views

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
        view=Test.as_view(),
        name="test_authentication",
    ),
    path(r"login/", LoginView.as_view(), name="knox_login"),
    path(r"logout/", knox_views.LogoutView.as_view(), name="knox_logout"),
    path(r"logoutall/", knox_views.LogoutAllView.as_view(), name="knox_logoutall"),
]
