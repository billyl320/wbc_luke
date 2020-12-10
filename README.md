# Experiment for ALL-IDB Data
Includes the experiment performed on the C-NMC data.  Includes the code and resulting shape images.  The output is provided in 'output_svm_radial.txt'.  The image processing was performed in Python 3.6.9.  The modeling was performed in R. Information about packages and R version are provided in 'output_svm_radial.txt'.  Information about the original data is found here: https://wiki.cancerimagingarchive.net/display/Public/C_NMC_2019+Dataset%3A+ALL+Challenge+dataset+of+ISBI+2019

## Pip3 Packages

Here is a list of the installed versions of the libraries.  Not all of these were used in the analysis on 10/7/2020. 

absl-py (0.9.0)<br />
apturl (0.5.2)<br />
asn1crypto (0.24.0)<br />
astor (0.8.1)<br />
attrs (19.3.0)<br />
awscli (1.14.44)<br />
beautifulsoup4 (4.9.1)<br />
botocore (1.8.48)<br />
Brlapi (0.6.6)<br />
bs4 (0.0.1)<br />
certifi (2018.1.18)<br />
cffi (1.14.0)<br />
chardet (3.0.4)<br />
colorama (0.3.7)<br />
command-not-found (0.3)<br />
cryptography (2.1.4)<br />
cupshelpers (1.0)<br />
cycler (0.10.0)<br />
decorator (4.4.1)<br />
defer (1.0.6)<br />
distro (1.0.1)<br />
distro-info (0.18ubuntu0.18.04.1)<br />
docutils (0.14)<br />
evdev (0.7.0)<br />
gast (0.3.3)<br />
google-pasta (0.2.0)<br />
grpcio (1.28.1)<br />
h5py (2.10.0)<br />
httplib2 (0.9.2)<br />
idna (2.6)<br />
imageio (2.6.1)<br />
importlib-metadata (1.6.0)<br />
Jinja2 (2.11.2)<br />
jmespath (0.9.3)<br />
joblib (0.14.1)<br />
Keras (2.3.1)<br />
Keras-Applications (1.0.8)<br />
Keras-Preprocessing (1.1.0)<br />
keyring (10.6.0)<br />
keyrings.alt (3.0)<br />
kiwisolver (1.1.0)<br />
language-selector (0.1)<br />
launchpadlib (1.10.6)<br />
lazr.restfulclient (0.13.5)<br />
lazr.uri (1.0.3)<br />
louis (3.5.0)<br />
lutris (0.5.6)<br />
lxml (4.5.1)<br />
macaroonbakery (1.1.3)<br />
Mako (1.0.7)<br />
Markdown (3.2.1)<br />
MarkupSafe (1.1.1)<br />
matplotlib (3.1.3)<br />
more-itertools (8.2.0)<br />
netifaces (0.10.4)<br />
networkx (2.4)<br />
numpy (1.18.4)<br />
oauth (1.0.1)<br />
olefile (0.45.1)<br />
opencv-python (4.2.0.34)<br />
packaging (20.3)<br />
pandas (0.25.3)<br />
pexpect (4.2.1)<br />
Pillow (7.0.0)<br />
pip (9.0.1)<br />
pluggy (0.13.1)<br />
protobuf (3.11.3)<br />
py (1.8.1)<br />
pyasn1 (0.4.2)<br />
pycairo (1.16.2)<br />
pycparser (2.20)<br />
pycrypto (2.6.1)<br />
pycups (1.9.73)<br />
Pygments (2.2.0)<br />
pygobject (3.26.1)<br />
pymacaroons (0.13.0)<br />
PyNaCl (1.1.2)<br />
pyparsing (2.4.7)<br />
pyRFC3339 (1.0)<br />
pytest (5.4.1)<br />
python-apt (1.6.5+ubuntu0.2)<br />
python-dateutil (2.8.1)<br />
python-debian (0.1.32)<br />
pytz (2019.3)<br />
PyWavelets (1.1.1)<br />
pyxdg (0.25)<br />
PyYAML (5.3.1)<br />
reportlab (3.4.0)<br />
requests (2.18.4)<br />
requests-unixsocket (0.1.5)<br />
roman (2.0.0)<br />
rpy2 (3.0.2)<br />
rsa (3.4.2)<br />
s3transfer (0.1.13)<br />
scikit-image (0.16.2)<br />
scikit-learn (0.22.1)<br />
scipy (1.0.0)<br />
scour (0.36)<br />
screen-resolution-extra (0.0.0)<br />
SecretStorage (2.3.1)<br />
setproctitle (1.1.10)<br />
setuptools (46.1.3)<br />
simplegeneric (0.8.1)<br />
simplejson (3.13.2)<br />
six (1.14.0)<br />
sklearn (0.0)<br />
soupsieve (2.0.1)<br />
ssh-import-id (5.7)<br />
system-service (0.3)<br />
systemd-python (234)<br />
tensorboard (1.14.0)<br />
tensorflow (1.14.0)<br />
tensorflow-estimator (1.14.0)<br />
termcolor (1.1.0)<br />
tzlocal (2.0.0)<br />
ubuntu-drivers-common (0.0.0)<br />
ufw (0.36)<br />
unattended-upgrades (0.1)<br />
urllib3 (1.22)<br />
usb-creator (0.3.3)<br />
wadllib (1.3.2)<br />
wcwidth (0.1.9)<br />
Werkzeug (1.0.1)<br />
wheel (0.34.2)<br />
wrapt (1.12.1)<br />
xkit (0.0.0)<br />
zipp (3.1.0)<br />
zope.interface (4.3.2)<br />

## lscpu

Below is the output of my Ubuntu Nuc machine where the experiments were performed on 12/4/2020.  

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
