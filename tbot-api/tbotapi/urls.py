from django.urls import include, path
from rest_framework import routers
from tbotapi.api import views
from django.contrib import admin
from django.urls import path

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'trades', views.TradeViewSet)
router.register(r'orders', views.OrderViewSet)
router.register(r'currencies', views.CurrencyViewSet)
router.register(r'markets', views.MarketViewSet)
router.register(r'accounts', views.AccountViewSet)
router.register(r'strategy/strategies', views.TAStrategyViewSet)
router.register(r'strategy/executions', views.TAExecutionViewSet)
router.register(r'strategy/analysis', views.TAAnalysisViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
