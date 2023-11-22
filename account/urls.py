from django.urls import path
from . import views

urlpatterns = [
    path('me/', views.UserInfoView.as_view(), name='user-detail'),
    path('update/', views.UserUpdateView.as_view(), name='user-update'),
    path('register/', views.UserCreateView.as_view(), name='user-create'),
    path('login/', views.UserLoginView.as_view(), name='user-login'),
    path('courses/', views.UserCoursesView.as_view(), name='user-courses'),
    path('saved-books/', views.UserSavedBooksView.as_view(),
         name='user-saved-books'),
    path('saved-courses/', views.UserSavedCoursesView.as_view(),
         name='user-saved-courses'),
    path('cart/', views.UserCartView.as_view(), name='user-cart'),
    path('enroll/<pk>', views.EnrollCourseView.as_view(), name='enroll-course'),
]
