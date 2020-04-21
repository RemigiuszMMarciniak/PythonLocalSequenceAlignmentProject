#!/bin/bash
echo "Performing 6 tests"

#manual
python3 main.py manual GCAGTC 1st CTAGG 2nd -2 t1 t1 SM.txt
python3 main.py manual GCAGTC 1st CTAGG 2nd -2 t2 t2 SMMATCH2MISMATCH0.txt
python3 main.py manual GCAGTC 1st CTAGG 2nd 1 t3 t3 SMMATCH2MISMATCH0.txt
python3 main.py manual GCAGTC 1st CTAGG 2nd -1 t4 t4 SMMATCH2MISMATCH5.txt
python3 main.py manual GCAGTC 1st CTAGG 2nd -1 t5 t5 SMMATCH1MISMATCH-1.txt
python3 main.py manual GCAGTC 1st CTAGG 2nd -1 t6 t6 SM.txt

#real data
python3 main.py file RNHGBB1.txt HSHGBB1.txt -2 t7 t7 SM.txt
python3 main.py file RNHGBB1.txt HSHGBG1.txt -2 t8 t8 SM.txt
python3 main.py file HSHGBG1.txt HSHGBB1.txt -2 t9 t9 SM.txt