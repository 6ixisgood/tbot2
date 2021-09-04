from tbotapi.api.models import Exchange, Account, Currency, Market, Order, Trade, \
        TAStrategy, TAExecution, TAAnalysis
from django.contrib.auth.models import User, Group
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']


class ExchangeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Exchange
        fields = '__all__'


class AccountSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Account


class CurrencySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Currency
        fields = '__all__'


class MarketSerializer(serializers.HyperlinkedModelSerializer):
    base = serializers.StringRelatedField() 
    quote = serializers.StringRelatedField()
    
    class Meta:
        model = Market
        fields = '__all__'


class OrderSerializer(serializers.HyperlinkedModelSerializer):
    timestamp = serializers.DateTimeField()
    market = serializers.StringRelatedField()
    class Meta:
        model = Order
        fields = '__all__'


class TradeSerializer(serializers.HyperlinkedModelSerializer):
    timestamp = serializers.DateTimeField()
    class Meta:
        model = Trade
        fields = '__all__'


class TAStrategySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TAStrategy
        fields = '__all__'


class TAExecutionSerializer(serializers.HyperlinkedModelSerializer):
    order_1 = OrderSerializer(read_only=True)
    order_2 = OrderSerializer(read_only=True)
    order_3 = OrderSerializer(read_only=True)
    strategy = serializers.StringRelatedField(read_only=True)
    class Meta:
        model = TAExecution 
        fields = '__all__'


class TAAnalysisSerializer(serializers.HyperlinkedModelSerializer):
    execution = TAExecutionSerializer(read_only=True) 
    class Meta:
        model = TAAnalysis
        fields = '__all__'
