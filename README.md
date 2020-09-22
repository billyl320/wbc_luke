# Experiment for ALL-IDB Data
Includes the experiment performed on the ALL-ODB data.  Includes the code and resulting shape images.  The output is provided in 'output_svm_radial.txt'.  The image processing was performed in Python 3.6.  The modeling was performed in R. 

## Pip3 Packages

Here is a list of the installed versions of the libraries.  Not all of these were used in the analysis on 9/22/2020. 

absl-py (0.9.0) <br />
apturl (0.5.2) <br />
asn1crypto (0.24.0) <br />
astor (0.8.1) <br />
attrs (19.3.0) <br />
beautifulsoup4 (4.6.0) <br />
blinker (1.4) <br />
Brlapi (0.6.6) <br />
certifi (2020.6.20) <br />
cffi (1.14.1) <br />
chardet (3.0.4) <br />
command-not-found (0.3) <br />
cryptography (2.1.4) <br />
cupshelpers (1.0) <br />
cycler (0.10.0) <br />
decorator (4.4.2) <br />
defer (1.0.6) <br />
distro-info (0.18ubuntu0.18.04.1) <br />
feedparser (5.2.1) <br />
gast (0.3.3) <br />
grpcio (1.30.0) <br />
h5py (2.10.0) <br />
html5lib (0.999999999) <br />
httplib2 (0.9.2) <br />
idna (2.10) <br />
imageio (2.9.0) <br />
importlib-metadata (1.7.0) <br />
imutils (0.5.3) <br />
Jinja2 (2.11.2) <br />
Keras (2.2.4) <br />
Keras-Applications (1.0.8) <br />
Keras-Preprocessing (1.1.2) <br />
keyring (10.6.0) <br />
keyrings.alt (3.0) <br />
kiwisolver (1.2.0) <br />
language-selector (0.1) <br />
launchpadlib (1.10.6) <br />
lazr.restfulclient (0.13.5) <br />
lazr.uri (1.0.3) <br />
louis (3.5.0) <br />
lxml (4.2.1) <br />
macaroonbakery (1.1.3) <br />
Mako (1.0.7) <br />
Markdown (3.2.2) <br />
MarkupSafe (1.1.1) <br />
matplotlib (3.3.0) <br />
mock (4.0.2) <br />
more-itertools (8.4.0) <br />
netifaces (0.10.4) <br />
networkx (2.4) <br />
numpy (1.19.1) <br />
oauth (1.0.1) <br />
oauthlib (2.0.6) <br />
olefile (0.45.1) <br />
opencv-python (3.4.0.12) <br />
packaging (20.4) <br />
pandas (1.1.0) <br />
pexpect (4.2.1) <br />
Pillow (7.2.0) <br />
pip (9.0.1) <br />
pluggy (0.13.1) <br />
progressbar2 (3.51.4) <br />
protobuf (3.12.2) <br />
py (1.9.0) <br />
pycairo (1.16.2) <br />
pycparser (2.20) <br />
pycrypto (2.6.1) <br />
pycups (1.9.73) <br />
pygobject (3.26.1) <br />
PyJWT (1.5.3) <br />
pymacaroons (0.13.0) <br />
PyNaCl (1.1.2) <br />
pyparsing (2.4.7) <br />
pyRFC3339 (1.0) <br />
pytest (5.4.3) <br />
python-apt (1.6.5+ubuntu0.3) <br />
python-dateutil (2.8.1) <br />
python-debian (0.1.32) <br />
python-utils (2.4.0) <br />
pytz (2020.1) <br />
PyWavelets (1.1.1) <br />
pyxdg (0.25) <br />
PyYAML (5.3.1) <br />
reportlab (3.4.0) <br />
requests (2.24.0) <br />
requests-unixsocket (0.1.5) <br />
rpy2 (3.0.2) <br />
scikit-image (0.15.0) <br />
scikit-learn (0.19.1) <br />
scipy (1.0.0) <br />
scour (0.36) <br />
screen-resolution-extra (0.0.0) <br />
SecretStorage (2.3.1) <br />
setuptools (49.2.0) <br />
simplegeneric (0.8.1) <br />
simplejson (3.13.2) <br />
six (1.15.0) <br />
system-service (0.3) <br />
systemd-python (234) <br />
tensorboard (1.13.1) <br />
tensorflow-estimator (1.13.0) <br />
tensorflow-gpu (1.13.1) <br />
termcolor (1.1.0) <br />
ubuntu-drivers-common (0.0.0) <br />
ufw (0.36) <br />
unattended-upgrades (0.1) <br />
unity-scope-calculator (0.1) <br />
unity-scope-chromiumbookmarks (0.1) <br />
unity-scope-colourlovers (0.1) <br />
unity-scope-devhelp (0.1) <br />
unity-scope-firefoxbookmarks (0.1) <br />
unity-scope-manpages (0.1) <br />
unity-scope-openclipart (0.1) <br />
unity-scope-texdoc (0.1) <br />
unity-scope-tomboy (0.1) <br />
unity-scope-virtualbox (0.1) <br />
unity-scope-yelp (0.1) <br />
unity-scope-zotero (0.1) <br />
unity-tweak-tool (0.0.7) <br />
urllib3 (1.25.10) <br />
usb-creator (0.3.3) <br />
wadllib (1.3.2) <br />
wcwidth (0.2.5) <br />
webencodings (0.5) <br />
Werkzeug (1.0.1) <br />
wheel (0.34.2) <br />
xkit (0.0.0) <br />
zipp (3.1.0) <br />
zope.interface (4.3.2) <br />

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
