# Compact Runge-Kutta Flux Reconstruction methods for non-conservative hyperbolic equations

[![License: MIT](https://img.shields.io/badge/License-MIT-success.svg)](https://opensource.org/licenses/MIT)
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.17827346.svg)](https://zenodo.org/doi/10.5281/zenodo.17827346)

This repository contains information and code to reproduce the results
presented in the article
```bibtex
@online{babbar2025crknoncons,
  title={Compact Runge-Kutta Flux Reconstruction methods for non-conservative hyperbolic equations},
  author={Babbar, Arpit and Ranocha, Hendrik},
  year={2025},
  month={12},
  eprint={?},
  eprinttype={arxiv},
  eprintclass={math.NA}
}
```

If you find these results useful, please cite the article mentioned above.
If you use the implementations provided here, please **also** cite this repository as
```bibtex
@misc{babbar2025crknonconsrepro,
  title={Reproducibility repository for
         "Compact Runge-Kutta Flux Reconstruction methods for non-conservative hyperbolic equations"},
  author={Babbar, Arpit and Ranocha, Hendrik},
  year={2025},
  howpublished={\url{https://github.com/Arpit-Babbar/paper_crk_nonconservative}},
  doi={10.5281/zenodo.17827346}
}
```

## Abstract

Compact Runge-Kutta (cRK) Flux Reconstruction (FR) methods are a variant of RKFR methods for hyperbolic conservation laws with a compact stencil including only immediate neighboring finite elements.
We extend cRKFR methods to handle hyperbolic equations with stiff source terms and non-conservative products.
To handle stiff source terms, we use IMplicit EXplicit (IMEX) time integration schemes such that the implicitness is local to each solution point, and thus does not increase inter-element communication.
Although non-conservative products do not correspond to a physical flux, we formulate the scheme using *numerical fluxes* at element interfaces.
We use similar numerical fluxes for a lower order finite volume scheme on subcells of each element, which is then blended with the high order cRKFR scheme to obtain a robust scheme for problems with non-smooth solutions.
Combined with a *flux limiter* at the element interfaces, the subcell based blending scheme preserves the physical admissibility of the solution, e.g., positivity of density and pressure for compressible Euler equations.
The procedure thus leads to an admissibility preserving IMEX cRKFR scheme for hyperbolic equations with stiff source terms and non-conservative products.
The capability of the scheme to handle stiff terms is shown through numerical tests involving Burgers' equations, reactive Euler's equations, the ten moment problem.
The non-conservative treatment is tested using variable advection equations, shear shallow water equations, the GLM-MHD, and the multi-ion MHD equations.

## Numerical experiments

In order to generate the results from this repository, you need to install [Julia](https://julialang.org).
We recommend using `juliaup`, as detailed in the official website [https://julialang.org](https://julialang.org).

The results have been generated using Julia version 1.10.10, and we recommend installing the same.
Once you have installed Julia, you can clone this repository, enter this directory and start the executable `julia` with the following steps

```shell
git clone https://github.com/Arpit-Babbar/paper_crk_nonconservative
cd paper_crk_nonconservative
julia --project=. --threads=auto
```

Then enter the following commands to generate all the data, and plot the 1-D results

```julia
julia> include("run_all.jl") # Generate all data
julia> include("plot_all_1d.jl") # Plot 1-D figures
```

If you wish to visualize the 2D figures, you need [ParaView](https://www.paraview.org) and its command line version `pvpython`.
Then, in your shell, you can run

```shell
bash plot_all_2d.sh
```

All the figures are now ready and available in the home directory of the repository

## Authors

- [Arpit Babbar](https://babbar.dev) (Johannes Gutenberg University Mainz, Germany)
- [Hendrik Ranocha](https://ranocha.de) (Johannes Gutenberg University Mainz, Germany)


## License

The code in this repository is published under the MIT license, see the `LICENSE` file.


## Disclaimer

Everything is provided as is and without warranty. Use at your own risk!
