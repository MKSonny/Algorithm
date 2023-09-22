def knapsack_bruteforce(items, capacity):
    num_items = len(items)
    best_value = 0
    best_combination = []

    for i in range(2**num_items):
        combination = []
        total_weight = 0
        total_value = 0

        for j in range(num_items):
            if (i >> j) & 1:
                combination.append(items[j])
                total_weight += items[j]["weight"]
                total_value += items[j]["value"]

        if total_weight <= capacity and total_value > best_value:
            best_value = total_value
            best_combination = combination

    return best_value, best_combination

# 물건 A, B, C를 딕셔너리로 표현
item_A = {"name": "A", "weight": 10, "value": 60}
item_B = {"name": "B", "weight": 20, "value": 100}
item_C = {"name": "C", "weight": 30, "value": 120}

items = [item_A, item_B, item_C]
knapsack_capacity = 50

max_value, best_combination = knapsack_bruteforce(items, knapsack_capacity)

print("최대 가치:", max_value)
print("선택한 물건:", [item["name"] for item in best_combination])
