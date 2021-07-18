from setuptools import find_packages, setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="librenms-handler",
    version="0.3.1",
    author="James Whale",
    author_email="james@james-whale.com",
    description="A Python library to interact with the LibreNMS API (v0)",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/WhaleJ84/librenms_handler",
    project_urls={
        "Bug Tracker": "https://github.com/WhaleJ84/librenms_handler/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ],
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    python_requires=">=3.6",
)

