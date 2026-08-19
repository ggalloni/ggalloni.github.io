---
layout: page
permalink: /research/
title: research
description: Optimal estimation and exact likelihoods for the large-scale CMB, and the statistics of primordial gravitational waves.
nav: true
nav_order: 1
toc:
  sidebar: left
---

## Estimation and likelihood methodology

The largest angular scales of the CMB carry the cleanest information about inflation, and
they are exactly where the standard analysis machinery is weakest. Pseudo-$$C_\ell$$
estimators lose optimality when the sky is cut, and Gaussian likelihood approximations
break down when the number of modes is small.

I work on the alternative: optimal (quadratic maximum-likelihood) estimators and exact
likelihoods, built to handle the sky as it actually arrives. Concretely, that means
estimation for arbitrarily many correlated spin-0 and spin-2 fields on a cut sky, with
general non-diagonal noise covariances; harmonic-space likelihoods validated against
pixel-based ground truth rather than against each other; and instrumental effects —
including time-domain filtering — carried through the estimator as response operators, so
that spectra come out unbiased without a simulation-calibrated transfer function.

This line of work is implemented in [CosmoForge](https://github.com/ggalloni/CosmoForge).

## Primordial gravitational waves

A detection of primordial B modes would fix the energy scale of inflation. Getting there
means being honest about what the data constrain and what the parametrisation does. I have
worked on joint constraints on the amplitude and tilt of the tensor spectrum, $$(r, n_t)$$,
combining CMB data with direct gravitational-wave interferometry and marginalising over the
tilt rather than fixing it — and then on separating the prior-driven part of the resulting
bound from the data-driven part, by adding a frequentist profile-likelihood axis alongside
the Bayesian one.

## Stochastic gravitational-wave backgrounds

A cosmological gravitational-wave background is a second, independent view of the same
primordial fluctuations the CMB shows us. I work on its angular statistics: the correlators
induced by a dipolar modulation of the primordial field, minimum-variance joint estimators
across the GW and CMB channels, and angular power spectra and two-point functions on the
cut sky. This is also a route into the CMB's large-scale anomalies, and into tests of the
statistical isotropy of the Universe that do not rest on the CMB alone.

## Collaborations

I am a member of **LiteBIRD**, the JAXA-led CMB satellite mission, where I lead the
power-spectrum-estimation and likelihood effort and sit on the Interim Governance Board;
and of the **Simons Observatory**, where I lead the LT1 subgroup of the Likelihood and
Theory group and maintain SOLikeT.

My work has also taken me to IJCLab (Université Paris-Saclay/CNRS) as a visiting
researcher for four months, and repeatedly to Kavli IPMU and KEK in Japan under the MSCA
project CMB-INFLATE.
