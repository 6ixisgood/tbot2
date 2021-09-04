import math
from tbotapi.api.models import Order, TAExecution, TAAnalysis


def perform_ta_analysis(execution_id):
    exec  = TAExecution.objects.get(id=execution_id)
    analysis = TAAnalysis(execution=exec)

    # get the difference in order price/amount
    analysis.o1_price_d = exec.order_1.price - exec.p_order_1.price
    analysis.o2_price_d = exec.order_2.price - exec.p_order_2.price
    analysis.o3_price_d = exec.order_3.price - exec.p_order_3.price
    analysis.o1_amount_d = exec.order_1.amount - exec.p_order_1.amount
    analysis.o2_amount_d = exec.order_2.amount - exec.p_order_2.amount
    analysis.o3_amount_d = exec.order_3.amount - exec.p_order_3.amount

    # how much we made/lost of the initial currency 
    # TODO work on fees
    starting_amount = exec.order_1.amount * exec.order_1.price \
                if exec.order_1.side == Order.Side.BUY else \
                exec.order_1.amount
    ending_amount = exec.order_3.amount * exec.order_1.price \
                if exec.order_3.side == Order.Side.SELL else \
                exec.order_1.amount
    analysis.payoff = ending_amount - starting_amount 

    # times between orders
    analysis.o1_o2_sec_d = (exec.order_2.timestamp - exec.order_1.timestamp).total_seconds()
    analysis.o2_o3_sec_d = (exec.order_3.timestamp - exec.order_2.timestamp).total_seconds()
    analysis.o1_o3_sec_d = (exec.order_3.timestamp - exec.order_1.timestamp).total_seconds()

    # time from strategy execution til order 1
    analysis.start_sec_d = (exec.order_1.timestamp - exec.timestamp).total_seconds()
    # total execution time
    analysis.full_sec_d = (exec.order_3.timestamp - exec.timestamp).total_seconds()

    analysis.save()
    
    
    

    
    
     
