
from django.urls import path, include
from shop import views
from django.contrib.auth.views import LoginView, LogoutView, PasswordResetView,PasswordResetDoneView, PasswordResetConfirmView,PasswordResetCompleteView
urlpatterns = [
    
    path('furniture/',views.furnitureview.as_view()),
    path('extra/',views.extraview.as_view()),
    path('contact/',views.contactview.as_view()),
    path('aboutus/',views.aboutusview.as_view()),
    path('faq/',views.faqview),
    path('reviews/',views.reviewsview.as_view()),
    path('insertcontact/',views.insertcontact),
    path('blogs/',views.blogview),
    path('blogdetail/<int:id>',views.blogdetailview),
    path('signup/',views.signup),
    path('login/',LoginView.as_view(),name="login"),
    path('logout/',LogoutView.as_view(),name="logout"),
    path('category/',views.categoryview),
    path('product/<int:id>',views.productview),
    path('productdetail/<int:id>',views.productdetailview),
    path('search_res/',views.searchview),
    path('gallery/',views.galleryview),
    path('myorder/',views.myorderview),
    path('insertreview/',views.insertreview),
    path('password-reset/', PasswordResetView.as_view(template_name='registration/password_reset.html'),name='password-reset'),
    path('password-reset/done/', PasswordResetDoneView.as_view(template_name='registration/password_reset_done.html'),name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/', PasswordResetConfirmView.as_view(template_name='registration/password_reset_confirm.html'),name='password_reset_confirm'),
    path('password-reset-complete/',PasswordResetCompleteView.as_view(template_name='registration/password_reset_complete.html'),name='password_reset_complete'),
]