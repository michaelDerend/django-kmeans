import os
import sys
import subprocess


def install_libraries():
    # Baca isi lib.txt untuk mendapatkan daftar library yang diperlukan
    with open('installed_packages.txt') as f:
        required_libraries = f.read().splitlines()

    # Periksa apakah proyek berjalan di dalam virtual environment (venv)
    in_venv = hasattr(os, 'real_prefix') or (
        hasattr(sys, 'base_prefix') and sys.base_prefix != sys.prefix)

    if in_venv:
        installed_libraries = subprocess.check_output(['pip', 'list']).decode()
        installed_libraries = [line.split(
            ' ')[0] for line in installed_libraries.split('\n')[2:]]

        # Instalasi library yang diperlukan jika belum terinstal
        for library in required_libraries:
            if library not in installed_libraries:
                subprocess.call(['pip', 'install', library])
                print(f'Library {library} telah diinstal.')
    else:
        print('Proyek tidak berjalan dalam virtual environment (venv). Silakan aktifkan venv terlebih dahulu.')


if __name__ == '__main__':
    install_libraries()
