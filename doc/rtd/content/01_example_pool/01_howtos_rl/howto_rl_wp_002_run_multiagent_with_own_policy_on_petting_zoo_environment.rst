.. _Howto WP RL 002:
Howto RL-WP-002: Run Multi-Agent on PettingZoo Environment
======================================================================


**Executable code**

.. literalinclude:: ../../../../../test/howtos/rl/howto_rl_wp_002_run_multiagent_with_own_policy_on_petting_zoo_environment.py
	:language: python

We use the Petting Zoo environment `Pistonball <https://pettingzoo.farama.org/environments/butterfly/pistonball/>`_ as default testing environment in this example.
However, in step 3.3 you can also change the environment into `Connect Four <https://pettingzoo.farama.org/environments/classic/connect_four/#connect-four>`_.


**Results**

By running the example code, the environment window appears and the runtime log is dumped to the terminal.

.. code-block:: bash

    YYYY-MM-DD  HH:MM:SS.SSSSSS  I  Petting Zoo Env Env "connect_four_v3": Instantiated 
    YYYY-MM-DD  HH:MM:SS.SSSSSS  I  Petting Zoo Env Env "connect_four_v3": Instantiated 
    YYYY-MM-DD  HH:MM:SS.SSSSSS  I  Petting Zoo Env Env "connect_four_v3": Operation mode set to 0 
    YYYY-MM-DD  HH:MM:SS.SSSSSS  I  Multi-Agent Connect4_Agents: Instantiated 
    YYYY-MM-DD  HH:MM:SS.SSSSSS  I  Multi-Agent Connect4_Agents: Adaptivity switched on 
    YYYY-MM-DD  HH:MM:SS.SSSSSS  I  Policy DiscRandPolicy: Instantiated 
    YYYY-MM-DD  HH:MM:SS.SSSSSS  I  Policy DiscRandPolicy: Adaptivity switched on 
    YYYY-MM-DD  HH:MM:SS.SSSSSS  I  Agent Agent_0: Instantiated 
    YYYY-MM-DD  HH:MM:SS.SSSSSS  I  Agent Agent_0: Adaptivity switched on 
    YYYY-MM-DD  HH:MM:SS.SSSSSS  I  Policy DiscRandPolicy: Adaptivity switched on 
    YYYY-MM-DD  HH:MM:SS.SSSSSS  I  Agent Agent_0: Adaptivity switched on 
    YYYY-MM-DD  HH:MM:SS.SSSSSS  I  Policy DiscRandPolicy: Adaptivity switched on 
    YYYY-MM-DD  HH:MM:SS.SSSSSS  I  Multi-Agent Connect4_Agents: Agent 0 Agent_0 added. 
    YYYY-MM-DD  HH:MM:SS.SSSSSS  I  Policy DiscRandPolicy: Instantiated 
    YYYY-MM-DD  HH:MM:SS.SSSSSS  I  Policy DiscRandPolicy: Adaptivity switched on 
    YYYY-MM-DD  HH:MM:SS.SSSSSS  I  Agent Agent_1: Instantiated 
    YYYY-MM-DD  HH:MM:SS.SSSSSS  I  Agent Agent_1: Adaptivity switched on 
    YYYY-MM-DD  HH:MM:SS.SSSSSS  I  Policy DiscRandPolicy: Adaptivity switched on 
    YYYY-MM-DD  HH:MM:SS.SSSSSS  I  Agent Agent_1: Adaptivity switched on 
    YYYY-MM-DD  HH:MM:SS.SSSSSS  I  Policy DiscRandPolicy: Adaptivity switched on 
    YYYY-MM-DD  HH:MM:SS.SSSSSS  I  Multi-Agent Connect4_Agents: Agent 1 Agent_1 added. 
    YYYY-MM-DD  HH:MM:SS.SSSSSS  I  RL-Scenario Connect Four V3: Instantiated 
    YYYY-MM-DD  HH:MM:SS.SSSSSS  I  RL-Scenario Connect Four V3: Operation mode set to 0 
    YYYY-MM-DD  HH:MM:SS.SSSSSS  I  RL-Scenario Connect Four V3: Process time 0:00:00 : Scenario reset with seed 1 
    YYYY-MM-DD  HH:MM:SS.SSSSSS  I  Multi-Agent Connect4_Agents: Init vizualization for all agents... 
    ....
    YYYY-MM-DD  HH:MM:SS.SSSSSS  I  Multi-Agent Connect4_Agents: Start vizualization for all agents... 
    YYYY-MM-DD  HH:MM:SS.SSSSSS  I  RL-Scenario Connect Four V3: Process time 0:00:12 End of processing


**Cross Reference**

    - :ref:`API Reference <api_basics>`