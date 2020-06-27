n = int(input())
stack_array, model_array = list(), list()

# model array
for i in range(n):
    m = int(input())
    model_array.append(m)

for i in range(len(model_array) - 1):
    if model_array[i] - model_array[i + 1] == -1:
        print("NO")

j = 1
for model in model_array:

    if model >= j:
        while j <= model:
            stack_array.append(j)
            print("+")
            j = j + 1
    else:
        stack_array.pop()
        print("-")

for i in range(n):
    stack_array.append(i)
    j = i
    if stack_array[j] == model_array[i]:
        stack_array.pop()



