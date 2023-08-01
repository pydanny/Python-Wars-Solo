# Releases

Follow these steps for pyproject.toml based projects.

## 0. Configure API token for the project

Howto Reference: https://pypi.org/manage/account/#api-tokens

My `.pypirc` file:

```
[distutils]
index-servers =
    pypi
    Python-Wars-Solo

[pypi]
repository = https://upload.pypi.org/legacy/

[Python-Wars-Solo]
repository = https://upload.pypi.org/legacy/
username = __token__
password = pypi_API_TOKEN_HERE


```

## 1. Install latest `build` and `twine` packages

```
pip install -U build
```

## 2. Build wheel and source distributions

```
python -m build --sdist
```

## 3. Upload to PyPI

```
python -m twine upload dist/* --verbose --repository Python-Wars-Solo
```
