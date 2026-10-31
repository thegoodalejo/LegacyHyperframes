#!/bin/sh
# Rehace la música de «Kingdom en un minuto» desde el mp3 de la pista (SPEC §0.1), con dos costuras medidas y cruces triangulares de 30 ms
# que terminan 10 ms antes de la cabeza de compás (el ataque entra entero):
#   pista 14,05–30,04  → video 0–16      entrada (4 s) + primera subida (8 s) + medio respiro (4 s)
#   pista 34,01–72,04  → video 16–54     segunda subida (16–32) + clímax (32–48) + seis segundos de la salida (48–54)
#   pista 82,01–fin    → video 54–58     el último acorde, que se apaga solo debajo del cierre
#   sh _gen/musica.sh      (desde clip-sitio-en-un-minuto/)  → assets/musica/product-launch-minuto.wav (58,0 s)
set -e
ffmpeg -hide_banner -loglevel error -y -i assets/musica/product-launch-the-mountain.mp3 -filter_complex \
  "[0:a]atrim=start=14.05:end=30.04,asetpts=PTS-STARTPTS[a];\
[0:a]atrim=start=34.01:end=72.04,asetpts=PTS-STARTPTS[b];\
[0:a]atrim=start=82.01,asetpts=PTS-STARTPTS[c];\
[a][b]acrossfade=d=0.03:c1=tri:c2=tri[ab];[ab][c]acrossfade=d=0.03:c1=tri:c2=tri[m]" \
  -map "[m]" -ar 44100 -c:a pcm_s16le assets/musica/product-launch-minuto.wav
ffprobe -v error -show_entries format=duration -of csv=p=0 assets/musica/product-launch-minuto.wav
