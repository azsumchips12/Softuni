naylon = float(input())
paint = float(input())
razreditel = int(input())
hours = int(input())

naylo_price = (naylon + 2) * 1.5
paint_price = (paint + 1.1) * 14.5
razreditel_price = razreditel * 5
sum_all = naylo_price + paint_price + razreditel_price + 0.40
maistors = (sum_all * 0.30) * hours
final_price = sum_all + maistors

print(final_price)