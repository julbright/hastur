

hastur
==================================

A multi-armed bandit library for python.

Implements several different bandit strategies to help select the best configuration for repeated binary testing. Good for testing lots of different configurations or options simultaneously, as opposed to traditional A/B testing

Some example code::

    import random
    from hastur.observations import Observation
    from hastur.arms import Arm
    from hastur.bandits import BayesianBandit

    bb = BayesianBandit()

    bb.add_arm(Arm(), arm_name='my_first_arm')
    bb.add_arm(Arm(), arm_name='my_second_arm')

    for x in range(0,100):

        arm = random.choice([arm for arm in bb.arms])
        value = random.choice([0,1])
        bb.arms[arm].update(Observation(value = value))

    print(bb.valuations)
    >> {'my_first_arm': some_value, 'my_second_arm': some_other_value}
    print(bb.select_arm())
    >> ('some_arm', some_value)

Features
--------

* Multiple bandit selection methods: Greedy, EpsilonGreedy, Bayesian, UCB
* Extensible Observation class for adding metadata to binary results
* Pure python and no dependencies. If you have python 3.5 or above, you're ready to go.

Installation
------------

    Use pip or clone from source::
    
        pip install hastur


Contribute
----------

- Issue tracker: github.com:julbright/hastur/issues
- Source code: github.com:julbright/hastur



Contents
--------

.. toctree::
   :maxdepth: 2

   module
   license
   help
   



Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

