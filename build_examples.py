from dp import optimal_events
examples = (
        [1, -4, -1, 4, 5, -4, 6, 7, -2],
        [-1, -2, 0, -4, 2, 0, 4, 5],
        [1, 2, 3, -1, -2, -3, -4, -5, 0, 1, 3, 5, 1, 0],
    )
with open("examples.tex", "w") as f:
    for ex in examples:
        print(r'\mintinline{{python3}}{{optimal_events({})}} $\to$ \mintinline{{python3}}{{{}}}\par'.format(ex, optimal_events(ex)), file=f)
