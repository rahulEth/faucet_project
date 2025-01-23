from django.urls import path, include

urlpatterns = [
    path('faucet/', include('faucet_app.urls')),
]
