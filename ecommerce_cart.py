cart_items = {'k':10000, 'Laptop': 50000, 'Headphones': 2000, 'Mouse': 500, 'Keyboard': 1500}

def cal_tp():
    x = sum(cart_items.values())
    if len(cart_items) >= 5:
        dis = x * 0.1
        print("Total Price:", x - dis)
    else:
        print("Total Price:", x)

cal_tp()
