import os
import subprocess
import sys


def install_libraries():
    # Baca isi lib.txt untuk mendapatkan daftar library yang diperlukan
    with open('lib.txt') as f:
        required_libraries = [line.strip() for line in f if line.strip()]

    # Periksa apakah proyek berjalan di dalam virtual environment (venv)
    in_venv = hasattr(os, 'real_prefix') or (
        hasattr(sys, 'base_prefix') and sys.base_prefix != sys.prefix)

    if in_venv:
        # Instalasi library yang diperlukan jika belum terinstal
        for library in required_libraries:
            try:
                subprocess.check_call(['pip', 'install', library])
                print(f'Library {library} telah diinstal.')
            except subprocess.CalledProcessError as e:
                print(f'Error installing {library}: {e}')
    else:
        print('Proyek tidak berjalan dalam virtual environment (venv). Silakan aktifkan venv terlebih dahulu.')


if __name__ == '__main__':
    install_libraries()
