import setuptools


with open("README.md", "r") as setup:
    long_description = setup.read()

setuptools.setup(
    name="pydolphin",
    version="0.1.1",
    author="Dhruv Maaniya (@midnightmadwalk)",
    author_email="midnightmadwalk@gmail.com",
    description="a convenient solution to heroku web apps / APIs.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/dolphinorg/dolphin",
    license="MIT",
    packages=setuptools.find_packages(),
    include_package_data=True,
    install_requires=['aiohttp', 'apscheduler'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
