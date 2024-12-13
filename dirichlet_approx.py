import math

N = 20
alpha = math.sqrt(7)

k_alphas = []

for k in range(N):
    k_alphas.append(k*alpha)

fractionals = [k_alpha - math.floor(k_alpha) for k_alpha in k_alphas]

for fractional1 in fractionals:
    for fractional2 in fractionals:
        if fractional1 != fractional2 and abs(fractional1-fractional2) < (1/N):
            print(fractionals.index(fractional1), fractionals.index(fractional2))