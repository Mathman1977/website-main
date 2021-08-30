from django.urls import path
from . import views
from .views import HomeView

urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    path('training/<int:pk>', views.training, name="opgavenreeks_training"),
    path('<int:opgavenreeks_id>/resultaten', views.resultaten, name='resultaten'),
    path('<int:opgavenreeks_id>/uitgewerkt/<int:uitw>', views.uitgewerkt, name='uitgewerkt')

    ]
