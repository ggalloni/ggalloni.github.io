---
layout: page
permalink: /software/
title: software
description: Open-source software is the through-line of my work — every first-author paper of mine comes with public analysis code.
nav: true
nav_order: 3
---

Three collaborations run analyses on code I architect or maintain.

## Frameworks I lead

### [CosmoForge](https://github.com/ggalloni/CosmoForge)

A general-purpose framework for optimal estimation and exact Gaussian likelihood analysis on
the sphere, for an arbitrary number of correlated spin-0 and spin-2 fields. Three
pip-installable packages — CosmoCore, QUBE and PICSLike — with general non-diagonal noise
covariances handled through Sherman–Morrison–Woodbury. Existing optimal estimators in the
field are private, single-experiment and single-field; this one is none of those.

*Lead developer and architect.* It supplies the estimation behind the LiteBIRD paper
validating the mission's likelihood, and is the estimator under test on filtered Simons
Observatory data.

### [CHARM-Like](https://github.com/ggalloni/CHARM-Like)

Angular power-spectrum CMB analysis in a multi-field setting: from $$N$$ correlated Gaussian
fields — T, E, B, frequency channels or data splits — it computes the posterior on the
reionization optical depth $$\tau$$ and the tensor-to-scalar ratio $$r$$. The code behind
[Galloni et al. (2025)](https://arxiv.org/abs/2505.24829).

*Sole author.*

## Collaboration infrastructure I maintain

### [SOLikeT](https://github.com/simonsobs/SOLikeT)

The Simons Observatory likelihood and theory framework — the single point through which the
collaboration's CMB *and* large-scale-structure likelihoods are built and validated. Used
beyond SO, including in ACT DR6 parameter pipelines.

*Maintainer.* I led the restructuring of the LAT MFLike likelihood and contributed the
single-field likelihood infrastructure.

### [litebird_sim](https://github.com/litebird/litebird_sim)

The LiteBIRD Simulation Framework: the end-to-end infrastructure modelling the data
acquisition of all three LiteBIRD instruments, and the environment in which the mission's
analysis choices are tested before launch.

*One of three principal developers by contribution, and one of its maintainers*, holding
ownership of the repository in the LiteBIRD GitHub organisation and of the package on PyPI.

## Contributions and smaller tools

[**Cobaya**](https://github.com/CobayaSampler/cobaya) — the field's standard sampling
framework. I contributed the
[profile-likelihood sampler](https://github.com/ggalloni/profiler).

[**LiLit**](https://github.com/ggalloni/LiLit) — a likelihood generator for CMB forecasting.

[**lack_of_correlation_with_GWs**](https://github.com/ggalloni/lack_of_correlation_with_GWs)
— analysis code for [Galloni et al. (2023)](https://arxiv.org/abs/2305.18184): angular power
spectra and two-point functions of a gravitational-wave background on the cut sky, with a
mask-deconvolution generalisation.

I also wrote the LiteBIRD-internal package for the mission's likelihood studies, which lives
inside the collaboration.
