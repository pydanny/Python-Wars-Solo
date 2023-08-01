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

## 1. Create a git tag and push to github

```
git tag MAJOR.MINOR.PATCH
git push --tags
```

## 2. Generate release

1. Go to tag on Github: 

https://github.com/pydanny/Python-Wars-Solo/releases/tag/MAJOR.MINOR.PATCH

2. Click `Create release from tag` button

3. Click `Generate release notes` button

4. Copy/paste release notes into changelog.md

## 3. Install latest `build` and `twine` packages

```
pip install -U build
```

## 4. Build wheel and source distributions

```
python -m build --sdist
```

## 5. Upload to PyPI

```
python -m twine upload dist/* --verbose --repository Python-Wars-Solo
```

