
results = []
while True:
    question = input("Give me a number or type x to get the sum: ")
    if question == "x":
        break
    else:
        results.append(int(question))
print(sum(results))

