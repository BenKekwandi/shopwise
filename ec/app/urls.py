from django.contrib import admin
from django.urls import path
from .  import views
from .forms import LoginForm,MyPasswordResetForm
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_view

urlpatterns = [
    path('',views.home),
    path('category/<slug:val>/',views.CategoryView.as_view(),name="category"),
    path('profile/',views.ProfileView.as_view(),name="profile"),
    path('wishlist/',views.WishListView.as_view(),name='wishlist'),
    path('add-to-wishlist/<int:id>',views.addToWishList),
    path('remove-from-wishlist/<int:id>',views.removeFromWishList),
    path('registration/',views.CustomerRegistrationView.as_view(),name='customerregistration'),
    path('accounts/login/',auth_view.LoginView.as_view(template_name='app/login.html',authentication_form=LoginForm),name='login'),
    path('accounts/logout/', views.logout, name='logout'),
    path('password-reset/',auth_view.PasswordResetView.as_view(template_name='app/password_reset.html',form_class=MyPasswordResetForm),name='password_reset'),
    path('search',views.search, name="search"),
    path('all-products',views.showAllProducts, name="all-products"),
    path('product/<int:id>',views.showProduct),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)