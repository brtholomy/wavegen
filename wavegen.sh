#!/bin/bash
# wavegen

# dir is in .gitignore
[[ -d ./output ]] || mkdir output

python wavegen.py
SUCCESS=$?

if [ $SUCCESS -eq 0 ]; then
   echo "Generated wave. Playing..."
   open output/output.wav
else
   echo "Failure you donk."
fi
