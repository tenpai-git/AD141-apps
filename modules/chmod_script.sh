#!/bin/bash

read -p "How many exercises in this chapter?: " EX
read -p "What chapter number is this?: " CH

echo "Creating Practice Python Generator File"
touch practice.py
echo "#!/usr/bin/python3" >> practice.py

for PRAC in $(seq 1 $EX); do
      echo "Generating Practice File $PRAC for Chapter $CH"
      cp practice.py practice$CH-$PRAC.py
      chmod +x practice$CH-$PRAC.py
done

echo "Removing Practice Python Generator File"
rm practice.py
echo "Cleanup Complete, Files Generated"
