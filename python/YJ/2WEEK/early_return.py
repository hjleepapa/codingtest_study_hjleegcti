# 총 가격이 100이상인 경우, 10% 할인
def total_price(quantity, price):
    total = quantity * price
    
    if total > 100:
        return total * 0.9
    return total

print(total_price(4,50))