from setuptools import setup


setup(name='mlpro-int-pettingzoo',
version='1.0.1',
description='MLPro: Integration PettingZoo',
author='MLPro Team',
author_mail='mlpro@listen.fh-swf.de',
license='Apache Software License (http://www.apache.org/licenses/LICENSE-2.0)',
packages=['mlpro_int_pettingzoo'],

# Package dependencies for full installation
extras_require={
    "full": [
        "mlpro[full]>=1.4.0",
        "pygame>=2.1.3",
        "pymunk>=6.4.0",
        "pettingzoo>=1.25.0"
    ],
},

zip_safe=False)