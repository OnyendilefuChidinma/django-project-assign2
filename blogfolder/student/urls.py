from django.urls import path
from .home import HomepageView, view_profile, delete_student
# from . import home
from . import views


urlpatterns = [
    
    path('student_dashboard/', HomepageView.as_view(), name='dashboardView'),
    
    # path('profile/<int:student_id>/', view_profile, name='student_profile'),
    path('send_message/', views.send_message, name='send_message'),
    path('<slug:slug>/', view_profile, name='student_profile'),
    path('delete/<slug:slug>/', delete_student, name='delete_student')
]
