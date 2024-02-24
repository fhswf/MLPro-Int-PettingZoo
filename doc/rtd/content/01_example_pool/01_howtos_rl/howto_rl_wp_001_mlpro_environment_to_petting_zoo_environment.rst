.. _Howto WP RL 001:
Howto RL-WP-001: MLPro Environment to PettingZoo Environment
======================================================================


**Executable code**

.. literalinclude:: ../../../../../test/howtos/rl/howto_rl_wp_001_mlpro_environment_to_petting_zoo_environment.py
	:language: python



**Results**

The Bulk Good Laboratory Plant (BGLP) environment will be wrapped to a PettingZoo compliant environment. 


.. code-block:: bash

    YYYY-MM-DD  HH:MM:SS.SSSSSS  I  Environment BGLP: Instantiated 
    YYYY-MM-DD  HH:MM:SS.SSSSSS  I  Environment BGLP: Instantiated 
    YYYY-MM-DD  HH:MM:SS.SSSSSS  I  Environment BGLP: Operation mode set to 0 
    YYYY-MM-DD  HH:MM:SS.SSSSSS  I  Environment BGLP: Reset 
    Starting API test
    ...
    Passed API test
    test completed
    
There are several lines of action processing logs due to the API tests. When there is no detected failure, the environment is successfully wrapped.


**Cross Reference**

    - :ref:`API Reference <api_basics>`