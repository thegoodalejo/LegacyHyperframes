#!/bin/sh
# Regenera assets/musica/product-launch-recorrido.wav desde el mp3 (SPEC §0.1; la misma edición de recorrido-academia y recorrido-equipos):
# pista 14,05–46,04 + 22,01–fin con 30 ms de cruce = 95,997 s. Uso, desde recorrido-mi-iglesia/:  sh _gen/musica.sh
ffmpeg -hide_banner -y -i assets/musica/product-launch-the-mountain.mp3 -filter_complex \
  "[0:a]atrim=start=14.05:end=46.04,asetpts=PTS-STARTPTS[a];[0:a]atrim=start=22.01,asetpts=PTS-STARTPTS[b];[a][b]acrossfade=d=0.03:c1=tri:c2=tri[m]" \
  -map "[m]" -ar 44100 -c:a pcm_s16le assets/musica/product-launch-recorrido.wav
ffprobe -v error -show_entries format=duration -of csv=p=0 assets/musica/product-launch-recorrido.wav   # 95.997
