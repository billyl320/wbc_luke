# Classification of White Blood Cell Lerkemia with Low Number of Interpretable and Explainable Features

Provides the experiments for Lamberti 2022 (https://arxiv.org/abs/2201.11864).  Each branch corresponds to a given set of experiments using Python and R. 

## Branches

Each experiment has associated Python and R files.  The general framework to reproduce these experiments is as follows:

1. Download/obtain access to the associated images from their respective owners. 
2. Run the associated Python script: ultima.py.  Note that you need to ensure that the file structure is apporpriate for the given obtained files before running the script.  ultima.py will extract the features from the images.  This will result in several .txt files. 
3. Run the associated R script.  ALL-IBD's file is idb_rf.r.  C-NMC's file is cnmc_rf.r.  Ensure that all the files for each branch are in the same directory that you run the script.

## System Information

Below is the associated information regarding the computer (Ubunutu Nuc) used to run these experiments using lscpu:

Architecture:        x86_64 <br />
CPU op-mode(s):      32-bit, 64-bit <br />
Byte Order:          Little Endian <br />
CPU(s):              4 <br />
On-line CPU(s) list: 0-3 <br />
Thread(s) per core:  2 <br />
Core(s) per socket:  2 <br />
Socket(s):           1 <br />
NUMA node(s):        1 <br />
Vendor ID:           GenuineIntel <br />
CPU family:          6 <br />
Model:               142 <br />
Model name:          Intel(R) Core(TM) i7-7567U CPU @ 3.50GHz <br />
Stepping:            9 <br />
CPU MHz:             510.003 <br />
CPU max MHz:         4000.0000 <br />
CPU min MHz:         400.0000 <br />
BogoMIPS:            6999.82 <br />
Virtualization:      VT-x <br />
L1d cache:           32K <br />
L1i cache:           32K <br />
L2 cache:            256K <br />
L3 cache:            4096K <br />
NUMA node0 CPU(s):   0-3 <br />
