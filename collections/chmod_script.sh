#!/bin/bash

for PRAC in $(seq 1 6); do
      cp practice3.py practice3-$PRAC.py
      chmod +x practice3-$PRAC.py
done
