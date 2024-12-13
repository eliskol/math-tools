n=2747
e=13
p=41
q=67
phi_n=(p-1)*(q-1)
e_inv=2437
# for i in range(1,phi_n):
#     if (e*i)%phi_n==1:
#         print(i)
message=[2206,755,436,1165,1737]
for num in message:
    # print(num)
    print((num**e_inv)%n)