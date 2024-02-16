from setuptools import setup


setup(name='mlpro-int-pettingzoo',
version='0.1.0',
description='MLPro: Integration PettingZoo',
author='MLPro Team',
author_mail='mlpro@listen.fh-swf.de',
license='Apache Software License (http://www.apache.org/licenses/LICENSE-2.0)',
packages=['mlpro_int_pettingzoo'],

# Package dependencies for full installation
extras_require={
    "full": [
        "mlpro[full]>=1.3.1",
        "pettingzoo[all]>=1.22.3"
    ],
},

zip_safe=False)