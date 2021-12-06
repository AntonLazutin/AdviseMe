from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('signup/', views.signup_page, name="signup"),
    # path('create_msg/', views.create_message, name="msg"),
    path('logout/', views.logout_view, name="logout"),
    path('login/', views.login_page, name="login"),
    path('create_review/', views.create_review, name="create_review"),
    path('review_detail/<int:review_id>/', views.review_page, name="review_page"),
    path('profile/<int:user_id>/', views.profile, name='profile'),
    path('profile/', views.profile, name='profile'),
    path('search/', views.SearchResultsView.as_view(), name="search")
]
