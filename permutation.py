class Permutation:
    def __init__(self, transformation_dict):
        self.transformation_dict = transformation_dict
        self.n = max(transformation_dict.keys())

    @classmethod
    def from_tuple(cls, cycle):
        transformation_dict = {
            cycle[i]: cycle[(i + 1) % len(cycle)] for i in range(len(cycle))
        }
        return cls(transformation_dict)

    def __rmul__(self, second_permutation):
        """right multiplies"""
        transformation_dict = {
            n: n for n in range(1, max(self.n, second_permutation.n) + 1)
        }
        for key in self.transformation_dict:
            transformation_dict[key] = self.transformation_dict[key]

        for key in second_permutation.transformation_dict:
            transformation_dict[key] = second_permutation.transformation_dict[
                transformation_dict[key]
            ]

        return transformation_dict

    def __mul__(self, other):
        return other.__rmul__(self)

    def __call__(self, num):
        if num in self.transformation_dict:
            return self.transformation_dict[num]
        return num


sigma = Permutation.from_tuple((1, 2, 3, 4))
print(sigma(1))  # applies the cycle to 1
