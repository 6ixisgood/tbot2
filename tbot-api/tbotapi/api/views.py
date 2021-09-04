from django.contrib.auth.models import User, Group
from rest_framework import viewsets
#from rest_framework import permissions
from tbotapi.api.models import Exchange, Account, Currency, Market, Order, Trade, \
        TAStrategy, TAExecution, TAAnalysis
from tbotapi.api.serializers import UserSerializer, GroupSerializer, \
        ExchangeSerializer, AccountSerializer, CurrencySerializer, \
        MarketSerializer, OrderSerializer, TradeSerializer, \
        TAStrategySerializer, TAExecutionSerializer, TAAnalysisSerializer, \
        AccountSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
#    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
#    permission_classes = [permissions.IsAuthenticated]


# class ExchangeViewSet(viewsets.ModelViewSet):
#     """
#     API endpoint that allows Exchanges to be viewed or edited.
#     """
#     queryset = Exchange.objects.all()
#     serializer_class = UserSerializer
##     permission_classes = [permissions.IsAuthenticated]


class AccountViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Accounts to be viewed or edited.
    """
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
#    permission_classes = [permissions.IsAuthenticated]


class CurrencyViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Currencies to be viewed or edited.
    """
    queryset = Currency.objects.all()
    serializer_class = CurrencySerializer
#    permission_classes = [permissions.IsAuthenticated]


class MarketViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Markets to be viewed or edited.
    """
    queryset = Market.objects.all()
    serializer_class = MarketSerializer
#    permission_classes = [permissions.IsAuthenticated]


class OrderViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Orders to be viewed or edited.
    """
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
#    permission_classes = [permissions.IsAuthenticated]


class TradeViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Trades to be viewed or edited.
    """
    queryset = Trade.objects.all()
    serializer_class = TradeSerializer
#    permission_classes = [permissions.IsAuthenticated


class TAStrategyViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Trades to be viewed or edited.
    """
    queryset = TAStrategy.objects.all()
    serializer_class = TAStrategySerializer
#    permission_classes = [permissions.IsAuthenticated


class TAExecutionViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Trades to be viewed or edited.
    """
    queryset = TAExecution.objects.all()
    serializer_class = TAExecutionSerializer
#    permission_classes = [permissions.IsAuthenticated


class TAAnalysisViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Trades to be viewed or edited.
    """
    queryset = TAAnalysis.objects.all()
    serializer_class = TAAnalysisSerializer
#    permission_classes = [permissions.IsAuthenticated


class AccountViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Trades to be viewed or edited.
    """
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
#    permission_classes = [permissions.IsAuthenticated







def load_currencies(request):
    pass

def load_markets(request):
    pass

