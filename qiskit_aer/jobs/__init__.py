# -*- coding: utf-8 -*-

# This code is part of Qiskit.
#
# (C) Copyright IBM 2018, 2019.
#
# This code is licensed under the Apache License, Version 2.0. You may
# obtain a copy of this license in the LICENSE.txt file in the root directory
# of this source tree or at http://www.apache.org/licenses/LICENSE-2.0.
#
# Any modifications or derivative works of this code must retain this
# copyright notice, and modified files need to carry a notice indicating
# that they have been altered from the originals.
"""
================================================
Aer Jobs (:mod:`qiskit_aer.jobs`)
================================================

.. currentmodule:: qiskit_aer.jobs

This module contains classes and functions to manage Aer jobs.

Classes
=======

The following are the classes used to manage job submissions.

.. autosummary::
    :toctree: ../stubs/

    AerJob
    AerJobSet

"""

from .aerjob import AerJob
from .aerjobset import AerJobSet
from .utils import split_qobj