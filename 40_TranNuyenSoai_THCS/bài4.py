n = int(input("Nhập n: "))

print("Các số nguyên tố nhỏ hơn", n, "là:")

for num in range(2, n):
    isPrime = True
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            isPrime = False
            break
    if isPrime:
        print(num, end=" ")