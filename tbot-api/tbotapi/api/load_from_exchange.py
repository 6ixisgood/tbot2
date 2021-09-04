import ccxt
from tbotapi.api.models import Exchange, Currency, Market, Account
API_SECRET='LwrTJib0RwRax8lSSkfNHahT6Dzsgj9cEdSVOJNNvEKTldC8P/5+6ua+'
API_KEY='73dOs+9pInQ26vTGWN8k/O8L6VK+0vdXJlcpLv5mVFtn8HCYWZHm3Lls2aDD6sxiOJy1keKV/mALtfe4MXFcMQ=='

def get_exchanges():
    # get a set of the exchanges in acvtive accounts
    exchanges = set()
    for account in Account.objects.all():
        exchanges.add(account.exchange)
    return exchanges

def load_currencies():
    # go through each exchange supported and load the currencies
    for e_id in get_exchanges():
        exchange = eval(f'ccxt.{e_id}()') 
        exchange.load_markets() 
        for key, val in exchange.currencies.items():
            c = Currency(name=val.get('name') or 'None', 
                         code=val.get('code') or 'None', 
                         active=val.get('active') or False,
                         fee=val.get('fee') or 0,
                         precision=val.get('precision') or 8,
                         limits_amount_min=val['limits']['amount']['min'],
                         limits_amount_max=val['limits']['amount']['max'],
                         exchange=e_id)
            c.save()
 
def load_markets():
    # go through each exchange supported and load the currencies
    for e_id in get_exchanges():
        exchange = eval(f'ccxt.{e_id}()')
        exchange.load_markets()
        for key, val in exchange.markets.items():
            print(val)
            m = Market(symbol=val.get('symbol') or '', 
                       active=val.get('active') or False,
                       base=Currency.objects.get(code=val.get('base') or ''), 
                       quote=Currency.objects.get(code=val.get('quote') or ''),
                       precision_price=val['precision']['price'],
                       precision_amount=val['precision']['amount'],
                       limits_amount_min=val['limits']['amount']['min'] or 0,
                       limits_amount_max=val['limits']['amount']['max'] or 9999999999,
                       limits_price_min=val['limits']['price']['min'] or 0,
                       limits_price_max=val['limits']['price']['max'] or 9999999999,
                       limits_cost_min=val['limits']['cost']['min'] or 0,
                       limits_cost_max=val['limits']['cost']['max'] or 9999999999,
                       exchange=e_id)
            m.save()       
    
