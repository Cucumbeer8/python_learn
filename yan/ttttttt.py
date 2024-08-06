import numpy as np
from scipy.stats import ks_2samp, entropy
from collections import defaultdict


def process_logs(filename):
    # Словари для хранения данных
    data = defaultdict(lambda: defaultdict(lambda: defaultdict(list)))

    # Чтение файла
    with open(filename, 'r') as file:
        for line in file:
            try:
                n, test_id, ind, feat = line.strip().split()
                n = int(n)
                test_id = int(test_id)
                ind = int(ind)
                feat = float(feat)

                data[n][test_id][ind].append(feat)
            except ValueError:
                # Пропускаем некорректные строки
                continue

    # Набор фичей с багом
    bugged_features = set()

    # Проверка распределений
    for n in data:
        if 1 in data[n] and 2 in data[n]:
            indices = set(data[n][1].keys()) & set(data[n][2].keys())

            for ind in indices:
                feats_1 = np.array(data[n][1][ind])
                feats_2 = np.array(data[n][2][ind])

                # Проверка распределений с использованием теста Колмогорова-Смирнова
                if len(feats_1) > 1 and len(feats_2) > 1:
                    # Используем KS-тест
                    ks_stat, ks_p_value = ks_2samp(feats_1, feats_2)

                    # Используем энтропию для сравнения распределений
                    hist_1, _ = np.histogram(feats_1, bins=50, density=True)
                    hist_2, _ = np.histogram(feats_2, bins=50, density=True)

                    # Избегаем нулевых значений при расчете энтропии
                    hist_1 = hist_1[hist_1 > 0]
                    hist_2 = hist_2[hist_2 > 0]

                    entropy_1 = entropy(hist_1)
                    entropy_2 = entropy(hist_2)

                    # Проверка на значимые различия
                    if ks_p_value < 0.05 or abs(entropy_1 - entropy_2) > 0.1:
                        bugged_features.add(ind)

    # Проверка, что найдены фичи с багом
    if not bugged_features:
        print("No features with detected bugs.")
    else:
        # Вывод результатов
        result = sorted(bugged_features)[:10]
        print(",".join(map(str, result)))


if __name__ == "__main__":
    process_logs('dataset.txt')
