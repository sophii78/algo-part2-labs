def build_transition_table(needle):
    m = len(needle)
    alphabet = set(needle)
    tf = [{} for _ in range(m + 1)]

    for state in range(m + 1):
        for char in alphabet:
            next_state = min(m, state + 1)
            while next_state > 0:
                if needle[:next_state] == (needle[:state] + char)[-next_state:]:
                    break
                next_state -= 1
            tf[state][char] = next_state

    return tf


def search_finite_automata(haystack, needle):
    if not needle:
        return []

    m = len(needle)
    n = len(haystack)
    tf = build_transition_table(needle)

    indices = []
    state = 0

    for i in range(n):
        char = haystack[i]
        state = tf[state].get(char, 0)

        if state == m:
            indices.append(i - m + 1)

    return indices


text = "АБАБАКАНАБАБА"
pattern = "АБА"
result = search_finite_automata(text, pattern)

print(f"Текст: {text}")
print(f"Паттерн: {pattern}")
print(f"Індекси входжень: {result}")
