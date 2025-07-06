# Stop Loss Order

## When I am trying to exit my position or place a Stop-Loss order, why is it being rejected?

It may happen if you have a pending Stop-Loss (SL) or an exit order already. With an already pending stop-loss or exit order, you will need extra funds to be able to place a duplicate SL/exit order. If you do not have this extra fund in your account, then your duplicate exit order will get rejected. That’s why we inform you while exiting if there’s a Pending SL/exit order against a position, to avoid any duplicate orders and rejections.

---

## My Stop-Loss (SL) order was triggered but it did not get executed. Why did this happen?

There could be 2 major reasons behind this:
The asset may be lacking a buyer/seller at the defined stop-loss limit price due to a lack of market depth. Orders are queued while they are being purchased or sold.
a. For example:
Let’s say there are 50 buyers and 100 sellers who are waiting to trade on a scrip at ₹90. Upon reaching ₹90, the first 50 sellers’ orders will be executed, and the remaining 50 sellers will have to wait for new buyers. In case you are one of those remaining 50 sellers, your
sell order
will remain pending if there are no corresponding buyers and vice versa.
The price movement during high volatility does not fulfill certain criteria e.g. suppose you have placed a
sell stop-loss
with trigger Price at
₹100
and limit price at ₹100. Now imagine that the LTP touched ₹100 (here, the SL would be triggered) and quickly went below ₹100 due to high volatility. The limit price of ₹100 means the stop-loss order would get executed at only ₹100 or more. Now this order will be pending as price is below Rs 100 and execution will happen only when price has reached or crossed Rs 100. Hence your stop-loss order was not executed.
Due to this reason, we recommend keeping a sufficient gap between the trigger price and limit price to increase the chances of Stop Loss execution during high volatility.
Note:
In order to increase the chances of execution, we keep the default value of the limit price 2 ticks away from the trigger price. This is done so that if the LTP moves rapidly after triggering the order, the limit price shouldn’t be a hindrance and the order should still get executed. Also, if you change the pre-set limit price and bring it closer to the Trigger Price, the chances of execution can reduce in cases of volatility.

---

## My stop-loss order got triggered even though the predefined Trigger Price had not appeared. Why?

Chances are that the market price did hit the stop-loss price, albeit momentarily and without you being able to spot it at that moment. Within a second, prices can change multiple times and not all of them are relayed to the Brokers by Exchange, especially during high volatility. As a result, such momentary price fluctuations are not seen anywhere.
Price matching and execution of the orders  is done by the Exchanges and not the Broker.

---

## What is Stop Loss?

Stop-loss is a tool that investors use to minimise the loss in a trade. Some traders define it as an advance order, which triggers an automatic closure of an open position when the stock price reaches the trigger price level.
Stop loss helps minimise losses but also limit profits from a trade.

---

## What is Trailing Stop Loss?

A Trailing Stop-loss is an order that lets you set a maximum value or percentage of loss you can incur on a trade. If the securiy price rises or falls in your favour, the trigger price jumps with it at the set value or percentage. If the security price rises or falls against you, the trigger price stays in place depending on the nature of the order.

---

## How does a Stop-loss get triggered?

Stop-loss can be your real saviour during a volatile market condition. A price level set at the beginning of the trade allows traders to close their position automatically when the stop-loss is reached. Squaring off takes place at the next price available at the trigger price level and helps limit losses.

---

## What is the 1% rule of trading?

The 1% rule defines the maximum limit of risk one can take in a trade or the risk-per-trade. It implies adjusting your position so that total loss doesn’t cross 1% of your trade value when the stop-loss is triggered. The 1% rule helps avoid significant losses.

---

## Can I use stop-loss in trading with the AngelOne Trading app?

You can place a Stop loss order  in AngelOne mobile app by following the below simple steps:
Visit the AngelOne app and select the stock to Buy/Sell
Select quantity of the trade
Set’ Trigger price’
Enter the price where you want to place stop-loss
Confirm the stop-loss price, click on “Buy/Sell” and confirm the order

---

