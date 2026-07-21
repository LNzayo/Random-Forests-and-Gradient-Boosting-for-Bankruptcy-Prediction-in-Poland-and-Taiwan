```python id="d2k8ma"
from setuptools import find_packages, setup

setup(
    name="bankruptcy-prediction",
    version="1.0.0",
    description="Random Forests and Gradient Boosting for Bankruptcy Prediction in Poland and Taiwan",
    author="Luzuko Nzayo",
    packages=find_packages(),
    install_requires=[
        "numpy",
        "pandas",
        "scikit-learn",
        "matplotlib",
        "seaborn",
        "imbalanced-learn",
    ],
    python_requires=">=3.10",
)
```
