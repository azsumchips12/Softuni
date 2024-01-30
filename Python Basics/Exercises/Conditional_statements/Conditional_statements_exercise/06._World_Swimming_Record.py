record_seconds = float(input())
metres = float(input())
one_metres = float(input())

all_time = metres * one_metres
slow = (metres // 15) * 12.5
whole_time = all_time + slow

diff = abs(whole_time - record_seconds)

if whole_time < record_seconds:
    print(f'Yes, he succeeded! The new world record is {whole_time:.2f} seconds.')

else:
    print(f'No, he failed! He was {diff:.2f} seconds slower.')