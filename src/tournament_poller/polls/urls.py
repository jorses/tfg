from django.urls import path
from django.conf.urls import url
from . import views
from . import charts

app_name = 'polls'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
    url(r'^charts/simple1.png$', charts.getchart1, name='getchart1'),
    url(r'^charts/simple2.png$', charts.getchart2, name='getchart2'),
]
