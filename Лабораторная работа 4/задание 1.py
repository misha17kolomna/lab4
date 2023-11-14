import json
with open('input.json') as file:
    ij = json.load(file)
total = 0
for znachenie in ij:
    score = znachenie.get('score', 0)
    weight = znachenie.get('weight', 0)
    total += score * weight
total = round(total, 3)
print(total)