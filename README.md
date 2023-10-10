# K-MEANS use Django

Web application to cluster data only use csv file upload.

[![Django CI](https://github.com/dkzhen/django-kmeans/actions/workflows/django.yml/badge.svg)](https://github.com/dkzhen/django-kmeans/actions/workflows/django.yml) [![license](https://img.shields.io/github/license/dkzhen/django-kmeans.svg)]()

## Usage

1. upload your file csv and apply
2. select clustering
3. input number of clusters
4. click start and system automatically create clusters results

## Installation

> [!IMPORTANT]
> Please install required libraries.

### required

- [Python 3.12.0 or latest](https://www.python.org/downloads/)

1. Clone repository

```console
  git clone https://github.com/dkzhen/django-kmeans
```

OR

```console
https://github.com/dkzhen/django-kmeans/releases
```

2. install dependencies

```python
  pip install -r requirements.txt
```

3. run your application

```python
  python manage.py  runserver
```

## List dependency versions

```console
$ bundle dependencies versions
+---------------------------+---------+
| pip                       | Version |
+---------------------------+---------+
| cycler                    | 0.10.0  |
| Django                    | 2.2.12  |
| joblib                    | 1.0.0   |
| kiwisolver                | 1.3.1   |
| matplotlib                | 3.3.3   |
| numpy                     | 1.19.5  |
| pandas                    | 1.2.0   |
| Pillow                    | 8.1.0   |
| pyparsing                 | 2.4.7   |
| python-dateutil           | 2.8.1   |
| pytz                      | 2020.5  |
| scikit-learn              | 0.24.0  |
| scipy                     | 1.6.0   |
| seaborn                   | 0.11.1  |
| six                       | 1.15.0  |
| sqlparse                  | 0.4.1   |
| threadpoolctl             | 2.1.0   |
| django-active-link        | 0.1.8   |
+---------------------------+---------+
```

## Team
* Dani 
* Putra
