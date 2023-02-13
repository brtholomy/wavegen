python3.11 wavegen.py
SUCCESS=$?

if [ $SUCCESS -eq 0 ];then
   echo "Generated wave. Playing..."
   afplay output.wav
else
   echo "Failure you donk."
fi
