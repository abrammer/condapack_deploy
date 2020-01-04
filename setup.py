from setuptools import setup


setup(name='condapack_deploy_example',
      version='0.0.3',
      description='Example of deploying conda based python app',
      packages=['demo_app'],
      entry_points = {
        'console_scripts': ['run_example=demo_app.demo:main'],
      },
)
