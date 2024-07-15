from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in init_hooks/__init__.py
from init_hooks import __version__ as version

setup(
	name="init_hooks",
	version=version,
	description="Make Custom Hooks",
	author="DAS",
	author_email="das@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
