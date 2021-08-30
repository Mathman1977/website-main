from django.urls import path
from . import views
from .views import HomeView

urlpatterns = [
    # path('', HomeView.as_view(), name="home"),
    # path('', views.index, name='index'),
    # # path('<int:reeks_id>/', views.detail, name='detail'),
    # # path('<int:reeks_id>/training/<int:opgave_id>', views.training, name='training'),
    # path('<str:reeks_titel>/training/', views.training, name='training'),
    # path('<int:reeks_id>/resultaten', views.resultaten, name='resultaten'),
    # path('<int:reeks_id>/uitgewerkt/<int:opgave_id>', views.uitgewerkt, name='uitgewerkt')
    ]
