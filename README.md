# Experiment for ALL-IDB Data
Includes the experiment performed on the ALL-ODB data.  Includes the code and resulting shape images.  The output is provided in 'output_svm_radial.txt'.  The image processing was performed in Python 3.6.  The modeling was performed in R. 

## Pip3 Packages

Here is a list of the installed versions of the libraries.  Not all of these were used in the analysis on 9/22/2020. 

absl-py (0.9.0)
apturl (0.5.2)
asn1crypto (0.24.0)
astor (0.8.1)
attrs (19.3.0)
beautifulsoup4 (4.6.0)
blinker (1.4)
Brlapi (0.6.6)
certifi (2020.6.20)
cffi (1.14.1)
chardet (3.0.4)
command-not-found (0.3)
cryptography (2.1.4)
cupshelpers (1.0)
cycler (0.10.0)
decorator (4.4.2)
defer (1.0.6)
distro-info (0.18ubuntu0.18.04.1)
feedparser (5.2.1)
gast (0.3.3)
grpcio (1.30.0)
h5py (2.10.0)
html5lib (0.999999999)
httplib2 (0.9.2)
idna (2.10)
imageio (2.9.0)
importlib-metadata (1.7.0)
imutils (0.5.3)
Jinja2 (2.11.2)
Keras (2.2.4)
Keras-Applications (1.0.8)
Keras-Preprocessing (1.1.2)
keyring (10.6.0)
keyrings.alt (3.0)
kiwisolver (1.2.0)
language-selector (0.1)
launchpadlib (1.10.6)
lazr.restfulclient (0.13.5)
lazr.uri (1.0.3)
louis (3.5.0)
lxml (4.2.1)
macaroonbakery (1.1.3)
Mako (1.0.7)
Markdown (3.2.2)
MarkupSafe (1.1.1)
matplotlib (3.3.0)
mock (4.0.2)
more-itertools (8.4.0)
netifaces (0.10.4)
networkx (2.4)
numpy (1.19.1)
oauth (1.0.1)
oauthlib (2.0.6)
olefile (0.45.1)
opencv-python (3.4.0.12)
packaging (20.4)
pandas (1.1.0)
pexpect (4.2.1)
Pillow (7.2.0)
pip (9.0.1)
pluggy (0.13.1)
progressbar2 (3.51.4)
protobuf (3.12.2)
py (1.9.0)
pycairo (1.16.2)
pycparser (2.20)
pycrypto (2.6.1)
pycups (1.9.73)
pygobject (3.26.1)
PyJWT (1.5.3)
pymacaroons (0.13.0)
PyNaCl (1.1.2)
pyparsing (2.4.7)
pyRFC3339 (1.0)
pytest (5.4.3)
python-apt (1.6.5+ubuntu0.3)
python-dateutil (2.8.1)
python-debian (0.1.32)
python-utils (2.4.0)
pytz (2020.1)
PyWavelets (1.1.1)
pyxdg (0.25)
PyYAML (5.3.1)
reportlab (3.4.0)
requests (2.24.0)
requests-unixsocket (0.1.5)
rpy2 (3.0.2)
scikit-image (0.15.0)
scikit-learn (0.19.1)
scipy (1.0.0)
scour (0.36)
screen-resolution-extra (0.0.0)
SecretStorage (2.3.1)
setuptools (49.2.0)
simplegeneric (0.8.1)
simplejson (3.13.2)
six (1.15.0)
system-service (0.3)
systemd-python (234)
tensorboard (1.13.1)
tensorflow-estimator (1.13.0)
tensorflow-gpu (1.13.1)
termcolor (1.1.0)
ubuntu-drivers-common (0.0.0)
ufw (0.36)
unattended-upgrades (0.1)
unity-scope-calculator (0.1)
unity-scope-chromiumbookmarks (0.1)
unity-scope-colourlovers (0.1)
unity-scope-devhelp (0.1)
unity-scope-firefoxbookmarks (0.1)
unity-scope-manpages (0.1)
unity-scope-openclipart (0.1)
unity-scope-texdoc (0.1)
unity-scope-tomboy (0.1)
unity-scope-virtualbox (0.1)
unity-scope-yelp (0.1)
unity-scope-zotero (0.1)
unity-tweak-tool (0.0.7)
urllib3 (1.25.10)
usb-creator (0.3.3)
wadllib (1.3.2)
wcwidth (0.2.5)
webencodings (0.5)
Werkzeug (1.0.1)
wheel (0.34.2)
xkit (0.0.0)
zipp (3.1.0)
zope.interface (4.3.2)

## lscpu

Below is the output of my Ubuntu machine where the experiments were performed on 9/22/2020.  

Architecture:        x86_64
CPU op-mode(s):      32-bit, 64-bit
Byte Order:          Little Endian
CPU(s):              8
On-line CPU(s) list: 0-7
Thread(s) per core:  2
Core(s) per socket:  4
Socket(s):           1
NUMA node(s):        1
Vendor ID:           GenuineIntel
CPU family:          6
Model:               42
Model name:          Intel(R) Core(TM) i7-2600 CPU @ 3.40GHz
Stepping:            7
CPU MHz:             1922.294
CPU max MHz:         3800.0000
CPU min MHz:         1600.0000
BogoMIPS:            6784.93
Virtualization:      VT-x
L1d cache:           32K
L1i cache:           32K
L2 cache:            256K
L3 cache:            8192K
NUMA node0 CPU(s):   0-7
