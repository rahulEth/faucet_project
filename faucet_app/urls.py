from django.urls import path
from . import views

urlpatterns = [
    path('fund/', views.FaucetFundView.as_view(), name='faucet-fund'),
    path('stats/', views.FaucetStatsView.as_view(), name='faucet-stats'),
]
