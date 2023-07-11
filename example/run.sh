#!/bin/sh

cd $(dirname $0)
cd ../

python wordle_solver.py -w t:1 a:5 t:3 a:4 t:2 a:3 c:1 \
                        -b o:2 n:3 g:4 v:1 i:2 l:5 s:1 r:4 k:5 d:3 \
                        -c a:2 e:4 t:5 \