print('=====MIMO COD=====')
s = 600
jeans_sold = 500
target = 500
target_hit = jeans_sold == target
print('hit jean sale target :')
print(target_hit)
current_stock = stock - jeans_sold
in_stock = current_stock != 0
print('jeans in stock:')
print(in_stock)