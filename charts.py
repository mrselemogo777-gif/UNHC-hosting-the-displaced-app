import matplotlib.pyplot as plt

from config import CHART_COLOR_ABS, CHART_COLOR_PC

def top_hosts_chart(big, metric, view):
    top = big.nlargest(12, metric)[["country_name", metric]].set_index("country_name")
    color = CHART_COLOR_ABS if view == "Absolute" else CHART_COLOR_PC
    fig, ax = plt.subplots(figsize=(10, 6))
    top.plot(kind="barh", ax=ax, legend=False, color=color)
    ax.invert_yaxis()
    ax.set_xlabel("")
    ax.set_title("")
    ax.grid(axis="x", alpha=.25)
    for spine in ("top", "right"):
        ax.spines[spine].set_visible(False)
    return fig, top
