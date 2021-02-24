# contribution-graph-plotter

Plots **anything** into a [GitHub contribution graph](https://docs.github.com/en/github/setting-up-and-managing-your-github-profile/viewing-contributions-on-your-profile). 🌟

<img src="./examples/python.svg" height="250">
<img src="./examples/mewtwo.svg" height="250">
<img src="./examples/me.svg" height="250">

Takes a two-dimensional iterable and converts it into a [Scalable Vector Graphics](https://docs.github.com/en/github/setting-up-and-managing-your-github-profile/viewing-contributions-on-your-profile).

## Installation

```sh
pip install contribution-graph-plotter
```

## Usage

```py
>>> from numpy.random import randint
>>> from contribution_graph_plotter import plot

# `plot` function expects a 2d iterable or `numpy.ndarray` with values in range(0, 5)
>>> img = randint(low=0, high=4, size=(10, 10))
>>> plot(img, "graph.svg")
```

For a more interesting example, please refer to [notebooks/example.py](./notebooks/example.py).

## Converting

- For converting from `.svg` to `.png`, I recommend [cloudconvert.com](https://cloudconvert.com/svg-to-png) with the the engine set to `chrome`

## Acknowledgements

- The `.svg` template for the graphs was extracted using [svg-screenshots](https://github.com/felixfbecker/svg-screenshots)
