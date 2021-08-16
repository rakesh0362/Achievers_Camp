from django.urls import path
from . import views

app_name = 'achievers'
urlpatterns = [
    path('', views.CurrentAffairsView.as_view(), name='currentaffairs_list'),

    path('vocab/', views.WordMeaning.as_view(), name='vocab'),
    path('examnotification/', views.ExamNotificationView.as_view(),
         name='examnotification'),
    path('<slug:slug>/examnotification/', views.ExamNotificationDetails.as_view(),
         name='examnotification_details'),
    path('examanalysis/', views.ExamAnalysisView.as_view(),
         name='examanalysis'),
    path('<slug:slug>/examanalysis/', views.ExamAnalysisDetails.as_view(),
         name='examanalysis_details'),

    path('<slug:slug>/', views.CurrentAffairsDetails.as_view(), name='detailed_list'),

    #path('vocab/', views.vocabularyView, name='vocabu'),
    #     path('<str:standard>/<slug:slug>/',
    #          views.LessonListView.as_view(), name='lesson_list'),
    #     path('<str:standard>/<str:slug>/create/',
    #          views.LessonCreateView.as_view(), name='lesson_create'),
    #     path('<str:standard>/<str:subject>/<slug:slug>/',
    #          views.LessonDetailView.as_view(), name='lesson_detail'),
    #     path('<str:standard>/<str:subject>/<slug:slug>/update/',
    #          views.LessonUpdateView.as_view(), name='lesson_update'),
    #     path('<str:standard>/<str:subject>/<slug:slug>/delete/',
    #          views.LessonDeleteView.as_view(), name='lesson_delete'),

]
