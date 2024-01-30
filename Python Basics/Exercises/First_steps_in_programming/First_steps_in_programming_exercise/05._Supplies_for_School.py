pen = int(input())
markers = int(input())
preparat = int(input())
discount = float(input())

pen_price = pen * 5.80
markers_price = markers * 7.20
preparat_price = preparat * 1.20
discount = discount / 100
sum_all = pen_price + markers_price + preparat_price
sum_discount = sum_all - (sum_all * discount)
print(sum_discount)