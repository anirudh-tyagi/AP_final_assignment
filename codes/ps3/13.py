def reduce(s, k):
    from itertools import combinations

    freq = {}
    for ch in s:
        if ch in freq:
            freq[ch] += 1
        else:
            freq[ch] = 1

    
    best_result = ""
    max_distinct = 0

    def can_form_equal(freq_map, k_left):
        items = list(freq_map.items())
        n = len(items)

        def backtrack(i, current_map, k_left):
            nonlocal best_result, max_distinct

            if i == n:
                counts = [v for v in current_map.values() if v > 0]
                if len(counts) == 0:
                    return
                if all(c == counts[0] for c in counts):
                    if k_left == 0:
                        candidate = ""
                        for ch in s:
                            if current_map[ch] > 0:
                                candidate += ch
                                current_map[ch] -= 1
                        distinct_count = len(set(candidate))
                        if distinct_count > max_distinct:
                            best_result = candidate
                            max_distinct = distinct_count
                return

            ch, count = items[i]
            for remove in range(min(count + 1, k_left + 1)):
                current_map[ch] = count - remove
                backtrack(i + 1, current_map.copy(), k_left - remove)

        backtrack(0, freq.copy(), k)

    can_form_equal(freq, k)
    return best_result

print(reduce('aaabbbccc', 3))