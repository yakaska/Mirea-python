import matplotlib.pyplot as matplotlib
from task3 import d1
from task4 import d2
from task5 import d3
from task6 import d4
from task7 import d5


def visualize(distance_metrics, y, z, move=1):
    moved_z = [i + move for i in z]
    distance_differences = []
    for distance in distance_metrics:
        distance_before_move = distance(y, z)
        distance_after_move = distance(y, moved_z)
        distance_difference = distance_after_move - distance_before_move
        distance_differences.append(distance_difference)
    x = range(0, len(distance_differences))
    figure, axis = matplotlib.subplots()
    # построение гистограммы с подписями
    axis.bar(x, distance_differences)
    axis.set_xticks(x, labels=[f'd_{i + 1}' for i in x])
    matplotlib.show()


y = (1.0, 0.5, 1.0)
z = (0.5, 2.0, 1.0)
visualize([d1, d2, d3, d4, d5], y, z)
visualize([d1, d2, d3, d4, d5], y, z, 0.01)