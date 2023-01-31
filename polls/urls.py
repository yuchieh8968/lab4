from django.urls import path
from . import views


app_name = 'polls'
#
# urlpatterns = [
#     # this is a route
#     # path refers what follows a host in a http request
#
#   path('', views.index, name='index'),
#   # want to inspect detail of question whos Id is the number
#   path('<int:question_id>/', views.detail, name = 'detail'),
#   # ex: /polls/5/results/
#   path('<int:question_id>/results/', views.results, name='results'),
#   # ex: /polls/5/vote/
#   path('<int:question_id>/vote/', views.vote, name='vote'),
# ]

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
]