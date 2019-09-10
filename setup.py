import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="FirstPythonPackage",
    version="1.0.0",
    author="jirikadlec2",
    author_email="jirikadlec2@example.com",
    description="my first python package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/jirikadlec2/first-python-package",
    packages=setuptools.find_packages(),
    install_requires=["numpy"],
    package_data={"FirstPythonPackage": ["data.json"]},
    classifiers=[
        "Development Status :: 3 - Alpha"
    ],
)
