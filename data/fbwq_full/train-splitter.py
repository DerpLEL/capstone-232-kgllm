with open('train.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()

total_lines = len(lines)
n = 1445061

final = [lines[i * n:(i + 1) * n] for i in range((total_lines + n - 1) // n)]

for index, i in enumerate(final, 1):
    with open(f"train-{index}.txt", 'w', encoding='utf-8') as f:
        f.write(''.join(i))
