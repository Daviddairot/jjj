from django.urls import include, path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.index, name="index"),
    path('next_page/', views.next_page, name='next_page'),
    path('next/', views.login_view, name='next'),  # 'next' is the login page
    path('vote/', views.vote, name='vote'),
    path('res/', views.end, name='end'),
    #path('vote_submit/', views.vote_submit, name='vote_submit'),
    path('close/', views.close, name='close'),
    path('upload/', views.upload, name = 'upload' ),
    path('candidate_list/', views.candidate_list, name = 'candidate_list' ),
    path('delete_candidate/<str:position>/<int:candidate_id>/', views.delete_candidate, name='delete_candidate'),
    path('custom_signup/', views.custom_signup, name = 'custom_signup'),
    path('custom_login/', views.custom_login, name = 'custom_login')

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
