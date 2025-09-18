from setuptools import find_packages, setup

setup(
    name='src',
    packages=find_packages(),
    version='0.1.0',
    description='cd "$REPO_LOCAL"',
    author='rsync -av --exclude '.git' ./ "$REPO_LOCAL"/',
    license='MIT',
)
