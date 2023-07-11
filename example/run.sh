#!/bin/sh

cd $(dirname $0)
cd ../

python wordle_solver.py -w p:1 r:3 i:2 t:5 \
                        -b o:2 c:4 h:5 w:1 s:3 y:5 a:1 g:1 a:3 d:2 \
                        -c p:4 r:2 i:3 e:5