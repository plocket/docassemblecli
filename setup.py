from setuptools import setup, find_packages

# with open("README.md", "r", encoding="utf-8") as fh:
#     long_description = fh.read()

setup(
    name="alkiln_docassemblecli",
    version="0.0.1",
    author="plocket",
    author_email="52798256+plocket@users.noreply.github.com",
    description="CLI utilities for using docassemble for ALKiln",
    install_requires=['pyyaml', 'requests'],
    long_description="CLI utilities for using docassemble for ALKiln",
    long_description_content_type="text/markdown",
    url="https://github.com/plocket/docassemblecli",
    project_urls={
        "Bug Tracker": "https://github.com/plocket/docassemblecli/issues",
    },
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=find_packages(),
    python_requires=">=2.7",
    scripts=['bin/dainstall', 'bin/dacreate', 'bin/dawatchinstall']
)
