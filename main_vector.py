from playLA.Vector import Vector

if __name__ == "__main__":
    vec = Vector([5,-3])
    print(vec)
    print(len(vec))
    print(vec[0])

    vec2 = Vector([3,1])

    print("{} + {} = {}".format(vec, vec2, vec2 + vec))
    print("{} - {} = {}".format(vec, vec2, vec - vec2))
    print("{} * {} = {}".format(vec, 3, vec * 3))
    print("{} * {} = {}".format(3, vec, 3 * vec))

    print("+{} = {}".format(vec, +vec))
    print("-{} = {}".format(vec, -vec))

    zero2 = Vector.zero(2)
    print(zero2)

    print("{} + {} = {}".format(vec, zero2, vec+zero2))

    print("norm({}) = {}".format(vec, vec.norm()))
    print("norm({}) = {}".format(vec2, vec2.norm()))

    print("normalization({})= {}".format(vec, vec.normalize()))

    print("normalization({})= {}".format(zero2, zero2.normalize()))

