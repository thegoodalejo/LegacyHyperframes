#!/bin/sh
# Regenera la música del recorrido desde el mp3 de la pista (SPEC §0.1, la edición de Academia, al cuadro):
#   pista 14,05–46,04 + 22,01–fin, con un cruce triangular de 30 ms (la costura cae en el 31,96–31,99 del video).
#   sh _gen/musica.sh      (desde recorrido-comunicaciones/)  → assets/musica/product-launch-recorrido.wav (95,997 s)
set -e
ffmpeg -hide_banner -y -i assets/musica/product-launch-the-mountain.mp3 -filter_complex \
  "[0:a]atrim=start=14.05:end=46.04,asetpts=PTS-STARTPTS[a];[0:a]atrim=start=22.01,asetpts=PTS-STARTPTS[b];[a][b]acrossfade=d=0.03:c1=tri:c2=tri[m]" \
  -map "[m]" -ar 44100 -c:a pcm_s16le assets/musica/product-launch-recorrido.wav
ffprobe -v error -show_entries format=duration -of csv=p=0 assets/musica/product-launch-recorrido.wav
