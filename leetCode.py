nums = list(map(int, input().split()))
hasil = float('-inf') 
hasil2 = float('-inf')
for num in nums:
    if num > hasil:
        hasil2 = hasil
        hasil = num
    elif num > hasil2:
        hasil2 = num
akhir = (hasil-1) * (hasil2-1)
print(akhir)