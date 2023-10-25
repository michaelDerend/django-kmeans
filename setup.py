import os
import subprocess
import sys
import random
import string
# ANSI escape codes untuk warna


def kmeans():
    print('''
\u001b[31m ___   _     \u001b[33m __   __\u001b[32m _______\u001b[34m _______\u001b[35;1m __    _\u001b[37;1m _______ 
\u001b[31m|   | | |    \u001b[33m|  |_|  \u001b[32m|       \u001b[34m|   _   \u001b[35;1m|  |  | \u001b[37;1m|       |
\u001b[31m|   |_| |\u001b[30;1m____\u001b[33m|       \u001b[32m|    ___\u001b[34m|  |_|  \u001b[35;1m|   |_| \u001b[37;1m|  _____|
\u001b[31m|      _|\u001b[30;1m____\u001b[33m|       \u001b[32m|   |___\u001b[34m|       \u001b[35;1m|       \u001b[37;1m| |_____ 
\u001b[31m|     |_     \u001b[33m|       \u001b[32m|    ___\u001b[34m|       \u001b[35;1m|  _    \u001b[37;1m|_____  |
\u001b[31m|    _  |    \u001b[33m| ||_|| \u001b[32m|   |___\u001b[34m|   _   \u001b[35;1m| | |   \u001b[37;1m|_____| |
\u001b[31m|___| |_|    \u001b[33m|_|   |_\u001b[32m|_______\u001b[34m|__| |__\u001b[35;1m|_|  |__\u001b[37;1m|_______|
'''+'\u001b[0m')


def logo():
    print('\u001b[32m'+'''
                                    (((((((((                                   
                                 (((((((((((((((                                
                                (((((((((((((((((                               
                                (((((((((((((((((                               
        &&&&&&&&&&           ,//(((((((((((((((((                               
      &&&&&&&&&&&&&&   ///////   (((((((((((((((                                
    /&&&&&&&&&&&&&&&&///          //((((((((( ////                              
    &&&&&&&&&&&&&&&&&&          ////             ///.                           
    /&&&&&&&&&&&&&&&&          ///                 ////                         
      &&&&&&&&&&&&&&//////   ///       ///            ///.                      
        &&&&&&&&&//      //////   /////////////         ////                    
                 ///      /// //////////////////           ///.((((((((((       
                   ///  ///.    /////////////////            ((((((((((((((     
                    //////      ///////////////////////////(((((((((((((((((    
                     ////       *///////////////           ((((((((((((((((((   
                   ///////*       /////////////            ,((((((((((((((((    
                  ///    ///           ///                   ((((((((((((((     
        %%%%%%%%%#/       ///.         ///                 ///.(((((((((.       
      %%%%%%%%%%%%%%        ///        ///              ////                    
    /%%%%%%%%%%%%%%%%        ///.      ///            ////                      
    %%%%%%%%%%%%%%%%%%         ///     ///          ///                         
    /%%%%%%%%%%%%%%%%           ///    ///       ////                           
      %%%%%%%%%%%%%%//////        //&&&&&&&&&  ////                             
        %%%%%%%%%.       //////  &&&&&&&&&&&&&&&                                
                              //&&&&&&&&&&&&&&&&&                               
                                &&&&&&&&&&&&&&&&&                               
                                &&&&&&&&&&&&&&&&&                               
                                 &&&&&&&&&&&&&&&                                
                                    &&&&&&&&&                                   
'''+'\u001b[0m')


def creditInstall():
    print("+--------------------------------------------+")
    print("|  "+'\u001b[33m'"Congratulation!!" +
          '\u001b[0m'" All library installed    |")
    print("|  Silahkan Jalankan " +
          '\u001b[31m'"'python setup.py -dev'"+'\u001b[0m'"  |")
    print("|                                            |")
    print("|  Created By:                               |")
    print("|  * Dani Kurniawan                          |")
    print("|  * Putra Al Fathurrizqi                    |")
    print("|  * Christofer Derend N                     |")
    print("|  * Mohammad Alfin B                        |")
    print("+--------------------------------------------+"+'\u001b[0m')


def creditRun():
    print("+--------------------------------------------+")
    print("|  "+'\u001b[33m'"Congratulation!!" +
          '\u001b[0m'" Project berjalan normal  |")
    print("|                                            |")
    print("|  * untuk dev  " +
          '\u001b[31m'"'python manage.py runserver'"+'\u001b[0m'" |")
    print("|  * untuk run  " +
          '\u001b[31m'"'python setup.py -dev'"+'\u001b[0m'"       |")
    print("|  * untuk stop  " +
          '\u001b[31m'"'CTRL + C'"+'\u001b[0m'"                  |")
    print("|                                            |")
    print("|  Created By:                               |")
    print("|  * Dani Kurniawan                          |")
    print("|  * Putra Al Fathurrizqi                    |")
    print("|  * Christofer Derend N                     |")
    print("|  * Mohammad Alfin B                        |")
    print("+--------------------------------------------+"+'\u001b[0m')


def running_command(command):
    subprocess.call(command)


def generate_random_string():
    characters = string.ascii_letters + string.digits + string.punctuation
    random_string = ''.join(random.choice(characters) for _ in range(50))
    return random_string


def migrate():
    running_command(["py", "manage.py", "migrate"])


def running_server():
    running_command(["py", "manage.py", "runserver"])


def cek_instalasi_venv():
    # Mengecek apakah folder 'venv' sudah ada dalam direktori proyek
    if not os.path.exists('venv'):
        print("Virtual environment ('venv') belum terinstal. Memulai proses instalasi...")

        # Menjalankan perintah untuk membuat virtual environment
        try:
            subprocess.run(['python', '-m', 'venv', 'venv'], check=True)
            print('\u001b[32;1m' +
                  "Virtual environment telah berhasil diinstal."+'\u001b[0m')
        except subprocess.CalledProcessError as e:
            print(f"Error saat mencoba menginstal virtual environment: {e}")
    else:
        print("+---------------------------------------------------------------------+")
        print("| Virtual environment ('venv') sudah terinstal dalam folder project.  |")
        print("| Silahkan masuk ke venv dengan menjalankan " +
              '\u001b[33m'"'venv\\Scripts\\activate'"+'\u001b[0m'+"   |")
        print("+---------------------------------------------------------------------+")


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
                print('\u001b[33m' +
                      'Library '+library+' telah diinstal.'+'\u001b[0m')
            except subprocess.CalledProcessError as e:
                print(f'Error installing {library}: {e}')
        migrate()
        logo()
        kmeans()
        creditInstall()

    else:
        print(
            '\u001b[31m'+'Proyek tidak berjalan dalam virtual environment (venv). Silakan aktifkan venv terlebih dahulu.'+'\u001b[0m')
        cek_instalasi_venv()


if 'secret-key' in sys.argv:
    print(
        '\u001b[33;1m'+'+------------------------------------------------------------------------+')
    print("|  "+'\u001b[36;1m'"Your Secret key:"+'\u001b[0m'+'\u001b[33;1m'+" '{key}' |".format(
        key=generate_random_string()))
    print(
        '+------------------------------------------------------------------------+'+'\u001b[0m')

elif '-dev' in sys.argv:
    kmeans()
    creditRun()
    running_command(["py", "manage.py", "runserver"])
else:
    install_libraries()
