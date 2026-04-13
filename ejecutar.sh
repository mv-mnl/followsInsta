#!/bin/bash
python3 analyze_instagram.py
# tiempo de espera de 5 segundos
sleep 5
python3 open_profiles.py


sleep 5
shopt -s extglob
rm -rf !(.git|.gitignore|analyze_instagram.py|open_profiles.py|README.md|*.sh) 
shopt -u extglob 
echo "Limpieza completada: Solo quedan tus archivos de código y configuración."

