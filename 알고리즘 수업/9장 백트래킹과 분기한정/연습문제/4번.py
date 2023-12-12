def backtrack_subset(target_sum, current_set, remaining_elements, results):
    if sum(current_set) == target_sum:
        results.append(current_set[:])

    for i, element in enumerate(remaining_elements):
        current_set.append(element)
        backtrack_subset(target_sum, current_set, remaining_elements[i + 1:], results)
        current_set.pop()

# 주어진 집합과 목표 합에 대한 부분집합 찾기
def find_subsets(target_sums, input_set):
    subsets_for_sums = {sum_val: [] for sum_val in target_sums}
    results = []

    for target_sum in target_sums:
        backtrack_subset(target_sum, [], input_set, results)
        subsets_for_sums[target_sum] = results
        results = []

    return subsets_for_sums

# 테스트
input_set = [1, 3, 4, 5]
target_sums = [11, 9, 5]

subsets = find_subsets(target_sums, input_set)

# 결과 출력
for target_sum, subset_list in subsets.items():
    print(f"합이 {target_sum}인 부분집합:")
    for subset in subset_list:
        print(subset)
    print()

def count_terminal_nodes(target_sum, current_set, remaining_elements, results):
    if sum(current_set) == target_sum:
        results.append(current_set[:])
        return 1

    count = 0
    for i, element in enumerate(remaining_elements):
        current_set.append(element)
        count += count_terminal_nodes(target_sum, current_set, remaining_elements[i + 1:], results)
        current_set.pop()

    return count

def calculate_pruning_ratio(target_sums, input_set):
    total_terminal_nodes = 0
    pruned_terminal_nodes = 0

    for target_sum in target_sums:
        results = []
        total_terminal_nodes += count_terminal_nodes(target_sum, [], input_set, results)
        print(total_terminal_nodes)
        pruned_terminal_nodes += len(results)

    pruning_ratio = pruned_terminal_nodes / total_terminal_nodes if total_terminal_nodes > 0 else 0
    return pruning_ratio

# 테스트
pruning_ratio = calculate_pruning_ratio(target_sums, input_set)
print(f"가지치기된 단말 노드의 비율: {pruning_ratio}")