from setuptools import setup, find_packages

long_description = open("README.md").read()

setup(
        name='servo-lock',
        version='0.0.1.2',
        description='Servo utility for the MG996R; but any servo works.',
        long_description=long_description,
        long_description_content_type="text/markdown",
        author_email='william.wyatt@cgu.edu',
        url='https://github.com/Tsangares/lock_servo',
        include_package_data=True,
        packages=find_packages(),
        install_requires=[
            ],
        entry_points={
            'console_scripts': [
                'servo = src.servo:main',
                ]
            },
        classifiers=[
            "Programming Language :: Python :: 3",
            "License :: OSI Approved :: MIT License",
            "Operating System :: OS Independent",
        ],
        python_requires='>=3.7',
)
