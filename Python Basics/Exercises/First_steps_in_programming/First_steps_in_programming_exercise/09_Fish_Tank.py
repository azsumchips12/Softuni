Length = int(input())
Width = int(input())
Height = int(input())
Percentage = float(input())

volume = Length * Width * Height
litres = volume * 0.001
prost = Percentage / 100
litres_needed = litres * (1-prost)
print(litres_needed)