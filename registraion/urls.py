from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path("",views.Home_page,name='home-page'),
    path("add-student/",views.AddStudent_page,name="add-student"),
    path("view-student/",views.ViewStudent_page,name='view-student'),
    path("<int:id>/",views.Delete,name='delete-student'),
    path("<int:student_id>",views.profile_page,name='profile-page'),
    path('notification/<int:notification_id>',views.notification_page,name='notification-page'),
    path('search/',views.Search_page,name="search-page"),
    path('edit/<int:student_id>',views.Edit_page,name='edit-page'),
    path('registeration/',views.RegisterView,name='registration-page'),
    path('login/',views.LoginView,name='login-page'),
    path('logout/',views.LogoutView,name='logout'),
    path('reset-password',views.forgotPassword,name='reset-password')
]
if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )
