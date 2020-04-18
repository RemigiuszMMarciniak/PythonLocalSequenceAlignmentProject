#!/bin/bash
echo "Performing tests"

#manual
python3 main.py manual AATCG 1st AACG 2nd -2 t1 t1 SM.txt
python3 main.py manual CGAGTC 1st CTAGG 2nd -2 t2 t2 SM.txt
