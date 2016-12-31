

$project
==================================

A multi-armed bandit library for python.

Implements several different bandit strategies to help select the best configuration for repeated binary testing. Good for testing lots of different configurations or options simultaneously, as opposed to traditional A/B testing

Some example code::

    import random
    from $project.observations import Observation
    from $project.arms import Arm
    from $project.bandits import BayesianBandit
    
    bb = BayesianBandit()
    
    my_first_arm = bb.add_arm('my_first_arm')
    my_second_arm = bb.add_arm('my_second_arm')

    for x in range(0,100):
        arm = random.choice([my_first_arm, my_second_arm])
        value = random.choice([0,1])
        bb.arms[arm].update(Observation(value = value))

    print(bb.valuations)
    >> {'my_first_arm': some_value, 'my_second_arm': some_other_value}
    print(bb.select_arm())
    >> 'some_arm'

Features
--------

* Multiple bandit selection methods: Greedy, EpsilonGreedy, Bayesian, UCB
* Extensible Observation class for adding metadata to binary results
* Pure python and no dependencies. If you have python 3.4 or above, you're ready to go.

Installation
------------

Easy!::

    pip install $project


Contribute
----------

- Issue tracker: github.com:julbright/$project/issues
- Source code: github.com:julbright/$project



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

