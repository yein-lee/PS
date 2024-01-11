from itertools import combinations, product


def get_sums(dice):
    all_combinations = product(*dice)
    return [sum(combination) for combination in all_combinations]


def solution(dice):
    n = len(dice)
    best_choice, max_wins = None, 0

    for a_comb in combinations(range(n), n//2):
        a_indices = [i for i in a_comb]
        b_indices = [i for i in range(n) if i not in a_indices]

        a_comb_sums = sorted(get_sums([dice[i] for i in a_indices]))
        b_comb_sums = sorted(get_sums([dice[i] for i in b_indices]))

        a_pointer, b_pointer, wins = 0, 0, 0
        while a_pointer < len(a_comb_sums) and b_pointer < len(b_comb_sums):
            if a_comb_sums[a_pointer] > b_comb_sums[b_pointer]:
                wins += len(a_comb_sums) - a_pointer
                b_pointer += 1
            else:
                a_pointer += 1

        if wins > max_wins:
            best_choice, max_wins = a_comb, wins

    return sorted([x + 1 for x in best_choice])