from setuptools import setup, find_packages

setup(
 name="dab_project",
 version="0.0.1",
 description="contained herein code in ./src directory of project",
 author="jwk",
 packages=find_packages(where="./src"),
 package_dir={"":"./src"},
 install_requires=["setuptools"],
 entry_points={"packages": ["main=dab_project.main:main"]}
)