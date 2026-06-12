import os
import matplotlib.pyplot as plt

BASE_OUTPUT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "outputs"))


def save_fig(name):
    path = os.path.join(BASE_OUTPUT, "figures", f"{name}.png")
    plt.savefig(path, bbox_inches="tight")
    print(f"Saved figure → {path}")