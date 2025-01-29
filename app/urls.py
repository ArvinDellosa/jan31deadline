from django.urls import path
from .views import HomePageView, AboutPageView, RegisterPageView, LoginPageView, BlogListView

urlpatterns = [
    path('', HomePageView.as_view(), name="home"),
    path('about/', AboutPageView.as_view(), name="about"),
    path('blog/', BlogListView.as_view(), name="blog"),
    path('register/', RegisterPageView.as_view(), name="register"),
    path('login/', LoginPageView.as_view(), name="login"),
]