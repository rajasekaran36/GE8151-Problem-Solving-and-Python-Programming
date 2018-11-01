l = [fact**2 for fact in range(10) if (fact%2 == 0)]
print(l)

l = ["{}--{}".format(ele,"True") for ele in range(10) if (ele%2 == 0)]
print(l)

l = [ele**3 for ele in range(10)]
print(l)