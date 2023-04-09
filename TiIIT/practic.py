y=[10175,9744,9499,9000,8631]
x=[480,460,440,420,400]

print(sum([y[c]*x[c] for c in range(5)]) / sum([x[c]**2 for c in range(5)]))