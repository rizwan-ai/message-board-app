# from django.urls import path
# from . import views

# urlpatterns = [
#     path("", views.index, name="home"),
# ]

# .........

# from django.urls import path
# from .views import HomePageView

# urlpatterns = [
#     path("", HomePageView.as_view(), name="index"),
# ]


# ...

from django.urls import path
from .views import ListPageView

urlpatterns = [
    path("", ListPageView.as_view(), name="index"),
]
