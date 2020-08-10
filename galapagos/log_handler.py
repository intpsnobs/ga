import numpy as np
import math
import matplotlib.pyplot as plt
from csaps import csaps as CubicSpline
from os import environ



def show_population(population: list, top=10, best=True):
    size_population = len(population)
    print(f"Top {top}:")
    for i in range(size_population if (top > size_population) else top):
        print(f"{population[i][0]}: fit({population[i][1]})")
    print()

    best_individual, best_fitness = population[0]
    if best:
        print("BEST %s: fit(%f) " % (best_individual, best_fitness))
        # show_board(best_individual)

    worst_individual, worst_fitness = population[-1]
    print("WORST %s: fit(%f) " % (worst_individual, worst_fitness))


def show_winner(hist: dict, phenotype: callable):
    with open(f'{environ["OUT_PATH"]}{environ["GA_TITLE"]}.txt', "w") as out_file:
        out_file.write("=============Winner===============\n\n")
        out_file.write("Chromosome: \n%s\n\n" % np.array_str(hist["champion"][0]))
        out_file.write("Fitness: %f\n" % hist["champion"][1])

        out_file.write("\n\n=============Config===============\n\n")
        out_file.write(
            f'Codification: {environ["COD"]} - Bounds = [{environ["LOW"]},{environ["HIGH"]}]\n'
        )
        out_file.write(f'Dimention: {environ["DIM"]}\n')
        out_file.write(f'Population size: {environ["POP"]}\n')
        out_file.write(f'Runs: {environ["RUN"]}\n')
        out_file.write(f'Generations: {environ["GEN"]}\n')
        out_file.write(f'Mutation: {format(float(environ["PM"])*100, ".1f")}%\n')
        out_file.write(f'Crossover: {format(float(environ["PC"])*100, ".1f")}%\n')
        out_file.write(f'Elitism: {"yes" if environ["EL"] == "true" else "no"}\n')

        if phenotype:
            out_file.write("\n\n==================================\n\n")
            out_file.write(phenotype(hist["champion"][0]))


def plot_runs(hist: dict, show=True):
    runs_num = int(environ["RUN"])

    y = runs_num // 2

    x = 2

    fig, axs = plt.subplots(x, y, figsize=(10, 10), constrained_layout=True)
    fig.suptitle(
        "%s | best fit: %.4f" % (environ["GA_TITLE"], hist["champion"][1]), fontsize=16
    )

    run = 0
    for line in axs:
        for ax in line:
            for config in [{'label':'best','color':None}, {'label':'worst','color':'red'}, {'label':'avg','color':'k'}]:
                
                # best = [x[1] for x in hist["runs"][run]["best"]]
                
                w_x = np.arange(len(hist["runs"][run][config['label']]))
                w_y = [x[1] for x in hist["runs"][run][config['label']]]
                w_xs = np.linspace(w_x[0], w_x[-1], 300)
                w_ys = CubicSpline(w_x, w_y, w_xs, smooth=0.33)
                
                # avg = [x for x in hist["runs"][run]["avg"]]
                
                # ax.plot(best, label="best")
                ax.plot(w_xs, w_ys, color=config['color'], label=config['label'], alpha=0.5)
                # ax.plot(avg, color="k", label="avg", alpha=0.6)
            ax.legend()
            ax.set_title(
                "run: %d | best fit: %.4f" % (run + 1, hist["runs"][run]["winner"][1])
            )
            ax.set_xlabel("Generations")
            ax.set_ylabel("Fitness")
            run = run + 1

    plt.savefig(f'{environ["OUT_PATH"]}{environ["GA_TITLE"]}_runs')

    if show:
        plt.show()


def convergence_chart(hist: dict, show=True):
    avg = {"best": [], "avg": [], "worst": [], "best_std": []}
    for i in range(int(environ["GEN"])):
        aux_best = []
        aux_avg = []
        aux_worst = []
        for j in range(int(environ["RUN"])):
            aux_best.append(hist["runs"][j]["best"][i][1])
            aux_worst.append(hist["runs"][j]["worst"][i][1])
            aux_avg.append(hist["runs"][j]["avg"][i][1])

        avg["best"].append(np.average(aux_best))
        avg["avg"].append(np.average(aux_avg))
        avg["worst"].append(np.average(aux_worst))
        avg["best_std"].append(np.std(aux_best))

    fig = plt.figure(figsize=(10, 10))
    fig.canvas.set_window_title(f'{environ["GA_TITLE"]}')
    fig.suptitle(
        "%s | best fit: %.4f" % (environ["GA_TITLE"], hist["champion"][1]), fontsize=16
    )
    plt.title("convergence graph")

    plt.plot(avg["best"], label="best")
    plt.plot(avg["avg"], color="k", label="avg")
    # plt.plot(avg["worst"], color='r', label="worst")

    plt.xlabel("Generations")
    plt.ylabel("Fitness")
    plt.fill_between(
        range(int(environ["GEN"])),
        np.array(avg["best"]) - np.array(avg["best_std"]),
        np.array(avg["best"]) + np.array(avg["best_std"]),
        alpha=0.15,
        label="best_std",
    )
    plt.legend(loc="lower right")

    plt.savefig(f'{environ["OUT_PATH"]}{environ["GA_TITLE"]}_convergence')

    if show:
        plt.show()
