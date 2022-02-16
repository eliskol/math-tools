class Permutation:
    def __init__(self, cycle_notation):
        self.transformation_dict = {cycle_notation[i]: cycle_notation[(i + 1) % len(cycle_notation)] for i in range(len(cycle_notation))}
        self.n = max(cycle_notation)

    @classmethod
    def from_dict(cls, dict):
        tuple_rep = (dict[i] for i in range())
        return cls

    def __rmul__(self, second_permutation):
        """right multiplies"""
        transformation_dict = {n: n for n in range(1, max(self.n, second_permutation.n) + 1)}
        for key in self.transformation_dict:
            transformation_dict[key] = self.transformation_dict[key]

        for key in second_permutation.transformation_dict:
            transformation_dict[key] = second_permutation.transformation_dict[transformation_dict[key]]

        return transformation_dict

    def __mul__(self, other):
        return other.__rmul__(self)

    def __call__(self, other):
        return other.__rmul__(self)

sigma = Permutation((1, 2, 3, 4))
sigma2 = Permutation((4, 3, 2, 1))
print(sigma * sigma2)
print(Permutation)