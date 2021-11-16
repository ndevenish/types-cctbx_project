from setuptools import find_packages, setup

print(find_packages(where="src"))

setup(
    name="cctbx-project-stubs",
    author="Nicholas Devenish",
    version="0.1",
    packages=[
        "cctbx-stubs",
        "libtbx-stubs",
        "scitbx-stubs",
        "boost_adaptbx-stubs",
        "iotbx-stubs",
        "rstbx-stubs",
    ],
    package_dir={"": "src"},
)
