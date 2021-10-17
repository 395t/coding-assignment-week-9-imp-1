from typing import List
import matplotlib.pyplot as plt
import json
from pathlib import Path

__CURR_DIR__ = Path(__file__).resolve().parent

STATS_DIR = __CURR_DIR__.parent / "outputs"

def compare_training_stats(
        training_stats: List[dict],
        labels: List[str],
        metric_to_compare: str = "loss",
        x_label: str = 'epoch',
        y_label='loss',
        legend_loc='upper right',
        title='Loss vs Epoch'
    ):

    metrics = {
        'loss': 1
    }
    metric_key = metrics[metric_to_compare]
    training_stats = training_stats

    metric_values = []
    epochs = []

    for training_stat in training_stats:
        current_metric_values = []
        for stats in training_stat.values():
            [epochs.append(x[0]) for x in stats if x[0] not in epochs]
            [current_metric_values.append(x[metric_key]) for x in stats]

        metric_values.append(current_metric_values)

    for values, label in zip(metric_values, labels):
        plt.plot(epochs, values, '-x', label=label)

    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.legend(loc=legend_loc)
    plt.title(title)

    return plt


def save_plt(plot, filename: str, location: Path = STATS_DIR):
    plot.draw()
    plot.savefig(f'{str(location / filename)}.png')

def load_stats_file(name: str) -> dict:
    for out in (STATS_DIR / f'{name}').glob("*.json"):
        with open(str(out), 'r') as f:
            return json.load(f)


if __name__ == "__main__":
    t0 = load_stats_file("SN_1000_pc_250")
    t1 = load_stats_file("SN_1000_pc_500")
    t2 = load_stats_file("SN_1000_pc_1000")
    t3 = load_stats_file("SN_1000_pc_1500")
    t4 = load_stats_file("SN_1000_pc_2048")

    test = [
        t0,
        t1,
        t2,
        t3,
        t4,
    ]

    labels = [
        "250 Points",
        "500 Points",
        "1000 Points",
        "1500 Points",
        "2048 (all) Points"
    ]

    compare_training_stats(test, labels)
    plt.show()
