# K-MEANS Algorithm

Web aplikasi untuk mengcluster / mengelompokan data secara dinamis dari file csv.

[![Django CI](https://github.com/dkzhen/django-kmeans/actions/workflows/django.yml/badge.svg)](https://github.com/dkzhen/django-kmeans/actions/workflows/django.yml) [![license](https://img.shields.io/github/license/dkzhen/django-kmeans.svg)](https://github.com/dkzhen/django-kmeans/blob/main/LICENSE) [![python](https://img.shields.io/badge/Python-3.9-3776AB.svg?style=flat&logo=python&logoColor=blue)](https://www.python.org) ![contributor](https://img.shields.io/github/contributors/dkzhen/django-kmeans?color=purple) ![size](https://img.shields.io/github/repo-size/dkzhen/django-kmeans?color=orange) [![GitHub last commit](https://img.shields.io/github/last-commit/dkzhen/django-kmeans.svg?style=flat)]() [![GitHub commit activity (branch)](https://img.shields.io/github/commit-activity/t/dkzhen/django-kmeans)]() [![Open Source](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://opensource.org/) [![GitHub forks](https://img.shields.io/github/forks/dkzhen/django-kmeans?color=tomato)]() ![PyPI - Status](https://img.shields.io/pypi/status/plotly) ![GitHub Release Date - Published_At](https://img.shields.io/github/release-date/dkzhen/django-kmeans)

## Technology

![Django](https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white) ![Bootstrap](https://img.shields.io/badge/bootstrap-%238511FA.svg?style=for-the-badge&logo=bootstrap&logoColor=white) ![Chart.js](https://img.shields.io/badge/chart.js-F5788D.svg?style=for-the-badge&logo=chart.js&logoColor=white) ![Matplotlib](https://img.shields.io/badge/Matplotlib-%23ffffff.svg?style=for-the-badge&logo=Matplotlib&logoColor=black) ![NumPy](https://img.shields.io/badge/numpy-%23013243.svg?style=for-the-badge&logo=numpy&logoColor=white) ![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white) ![Plotly](https://img.shields.io/badge/Plotly-%233F4F75.svg?style=for-the-badge&logo=plotly&logoColor=white) ![scikit-learn](https://img.shields.io/badge/scikit--learn-%23F7931E.svg?style=for-the-badge&logo=scikit-learn&logoColor=white) ![Gunicorn](https://img.shields.io/badge/gunicorn-%298729.svg?style=for-the-badge&logo=gunicorn&logoColor=white)

## Usage

1. upload your file csv and apply
2. select clustering
3. input number of clusters
4. click start and system automatically create clusters results

## Installation | cara install

> [!IMPORTANT]
> Please install required libraries.

### required

- [Python 3.9.0 or latest](https://www.python.org/downloads/)

1. Clone repo github ini

```console
  git clone https://github.com/dkzhen/django-kmeans
```

atau bisa download bundle projectnya pastikan download yang terbaru / latest

```console
https://github.com/dkzhen/django-kmeans/releases/latest
```

- setelah di download projectnya diektrak terlebih dahulu rar/zip
- buka folder project tadi di vscode

![image.png](https://github.com/dkzhen/django-kmeans/blob/main/utils/images/dir.jpg)

2. Setting environment || membuat env

- buka terminal di vscode ( powershell / cmd / gitbash)
- ketikkan perintah dibawah

```python
  python setup.py secret-key
```

![image.png](https://github.com/dkzhen/django-kmeans/blob/main/utils/images/secretkey.jpg)

Note: Salin kode random tersebut , cari file env.example diproject

- rename env.example menjadi .env
- pastekan kode random diatas di SECRET_KEY = paste disini!

![image.png](https://github.com/dkzhen/django-kmeans/blob/main/utils/images/env.jpg)

3. install dependencies || install perpustakaan python

- buat virtual env , ketikan perintah dibawah

```python
  python setup.py
```

Note : jika belum pernah membuat maka akan diinstal otomatis

![image.png](https://github.com/dkzhen/django-kmeans/blob/main/utils/images/novenv.jpg)

Note : Jika sudah terinstall maka akan muncul prompt seperti dibawah

![image.png](https://github.com/dkzhen/django-kmeans/blob/main/utils/images/venv.jpg)

- masuk ke dalam mode venv

```python
  venv\Scripts\activate
```

Note : untuk keluar dari mode venv cukup ketikkan 'deactivate'

- pastikan anda sudah dalam venv ada label (venv) dikiri

![image.png](https://github.com/dkzhen/django-kmeans/blob/main/utils/images/labelvenv.jpg)

- ketikkan kode dibawah , maka secara otomatis library akan terinstall

```python
  python setup.py
```

- jika berhasil maka akan muncul prompt seperti dibawah

![image.png](https://github.com/dkzhen/django-kmeans/blob/main/utils/images/instal.jpg)

4. run your application | jalankan aplikasi

- jalankan aplikasi dengan perintah berikut

```python
  python setup.py -dev
```

![image.png](https://github.com/dkzhen/django-kmeans/blob/main/utils/images/run.jpg)

- buka browser kunjungi alamat dibawah

```python
  http://127.0.0.1:8000
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

[![GitHub followers](https://img.shields.io/github/followers/dkzhen.svg?style=social&label=dkzhen)](https://github.com/dkzhen) [![GitHub followers](https://img.shields.io/github/followers/arthur-son.svg?style=social&label=arthur-son)](https://github.com/arthur-son) [![GitHub followers](https://img.shields.io/github/followers/michaelDerend.svg?style=social&label=michaelDerend)](https://github.com/michaelDerend)

## Version

[![GitHub Release](https://img.shields.io/github/v/release/dkzhen/django-kmeans.svg)](https://github.com/dkzhen/django-kmeans/releases/latest)
