python wavegen.py
SUCCESS=$?

if [ $SUCCESS -eq 0 ];then
   echo "Generated wave. Playing..."
   afplay output/output.wav
else
   echo "Failure you donk."
fi
