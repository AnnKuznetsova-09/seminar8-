#!/user/bin/python3
seq1 = input()
seq2 = input()
def find_seq(seq_first, seq_second):
    len1 = len(seq_first)
    len2 = len(seq_second)
    max_matches = 0
    best_positions = []
    for i in range(len1 - len2 + 1):
        piece = seq_first[i : i + len2]
        count = 0
        for j in range(len2):
            if piece[j] == seq_second[j]:
                count += 1
        if count > max_matches:
            max_matches = count
            best_positions = [i]
        elif count == max_matches:
            best_positions.append(i)
    print("Максимум совпадений:", max_matches)
    print("Начала участков:", best_positions)
    print("Координаты (начало, конец):")
    for start in best_positions:
        end = start + len2 - 1
        print(f"({start}, {end})")
find_seq(seq1, seq2)
