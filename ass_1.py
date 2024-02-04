def find_pairs_with_sum(arr, target_sum):
    pairs = []
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] + arr[j] == target_sum:
                pairs.append((arr[i], arr[j]))
    return pairs

def calculate_range(real_numbers):
    if len(real_numbers) < 3:
        return "Range determination not possible"
    return max(real_numbers) - min(real_numbers)

def highest_occurrence(input_string):
    char_count = {}
    for char in input_string:
        if char.isalpha():
            char_count[char] = char_count.get(char, 0) + 1
    max_char = max(char_count, key=char_count.get)
    max_count = char_count[max_char]
    return max_char, max_count

def matrix_power(matrix, power):
    result_matrix = matrix.copy()
    for _ in range(power - 1):
        result_matrix = [[sum(a * b for a, b in zip(row, col)) for col in zip(*matrix)] for row in result_matrix]
    return result_matrix

# Main program
if __name__ == "__main__":
    # Example
    arr_for_pairs = [2, 7, 4, 1, 3, 6]
    target_sum_for_pairs = 10
    result_pairs = find_pairs_with_sum(arr_for_pairs, target_sum_for_pairs)
    result_pairs_count = len(result_pairs)
    
    if result_pairs_count > 0:
        print(f"1) Number of pairs with sum {target_sum_for_pairs}: {result_pairs_count}")
        print(f"Pairs with sum {target_sum_for_pairs}: {result_pairs}")
    else:
        print(f"1) No pairs found with sum {target_sum_for_pairs}")

    real_numbers_list = [5, 3, 8, 1, 0, 4]
    result_range = calculate_range(real_numbers_list)
    print(f"2) Range of the real numbers list: {result_range}")

    square_matrix_A = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    power_m = 3
    result_matrix_power = matrix_power(square_matrix_A, power_m)
    print(f"3) Matrix raised to the power {power_m}:\n{result_matrix_power}")

    input_str = "hippopotamus"
    max_char, occurrence_count = highest_occurrence(input_str)
    print(f"4) The highest occurring character is '{max_char}' with occurrence count {occurrence_count}")
