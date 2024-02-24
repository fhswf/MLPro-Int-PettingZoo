.. MLPro Documentations documentation master file, created by
   sphinx-quickstart on Wed Sep 15 12:06:53 2021.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

MLPro-Int-PettingZoo - Integration between PettingZoo and MLPro
==============================================================

Welcome to MLPro-Int-PettingZoo, an extension to MLPro to integrate the PettingZoo package.
MLPro is a middleware framework for standardized machine learning in Python. It is 
developed by the South Westphalia University of Applied Sciences, Germany, and provides 
standards, templates, and processes for hybrid machine learning applications. PettingZoo, in 
turn, provides a diverse suite of environments for multi-agent reinforcement learning.

MLPro-Int-PettingZoo offers wrapper classes that allow the reuse of environments from PettingZoo in MLPro,
or the other way around.


**Preparation**
   Before running the examples, please install the latest versions of MLPro, PettingZoo, and MLPro-Int-PettingZoo as follows:

   .. code-block:: bash

      pip install mlpro-int-pettingzoo[full] --upgrade


**See also**
   - `MLPro - Machine Learning Professional <https://mlpro.readthedocs.io>`_ 
   - `MLPro-OA - Sub-framework for online machine learning <https://mlpro.readthedocs.io/en/latest/content/03_machine_learning/mlpro_oa/main.html>`_
   - `PettingZoo - An API standard for multi-agent reinforcement learning <https://pettingzoo.farama.org/index.html>`_ 
   - `Further MLPro extensions <https://mlpro.readthedocs.io/en/latest/content/04_extensions/main.html>`_
   - `MLPro-Int-PettingZoo on GitHub <https://github.com/fhswf/MLPro-Int-PettingZoo>`_


.. toctree::
   :hidden:
   :maxdepth: 2
   :caption: Home

   self


.. toctree::
   :maxdepth: 2
   :caption: Example Pool
   :glob:

   content/01_example_pool/*


.. toctree::
   :maxdepth: 2
   :caption: API Reference
   :glob:

   content/02_api/*


.. toctree::
   :maxdepth: 2
   :caption: About
   :glob:

   content/03_about/*
