import numpy as np

water_height = np.array([4.01, 4.03, 4.27, 4.29, 4.19,
                         4.15, 4.16, 4.23, 4.29, 4.19,
                         4.00, 4.22, 4.25, 4.19, 4.10,
                         4.14, 4.03, 4.23, 4.08, 14.20,
                         14.03, 11.20, 8.19, 6.18, 4.04,
                         4.08, 4.11, 4.23, 3.99, 4.23])

print(np.mean(water_height))

sorted_data = np.sort(water_height)
print(sorted_data)

print(np.median(sorted_data))

print(f'\n{np.percentile(water_height, 75)}')

print(np.std(water_height))