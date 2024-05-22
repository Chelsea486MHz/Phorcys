# Installation

*Phorcys* has been tested on Ubuntu 23.10.

## System requirements

On Debian-like systems:

`$ sudo apt-get install python3 python3-pip python3-dev protobuf-compiler build-essential`

## Install the package in a venv

*Note: as the package isn't uploaded yet, this method is currently unvailable.*

Create your virtualenv:

`$ sudo apt-get virtualenv`

Install *Phorcys*:

```
$ python3 -m venv phorcys_venv
$ source phorcys_venv/bin/activate
$ pip install phorcys
```

## Pull the Docker image

*Note: as the image isn't uploaded yet, this method is currently unvailable.*

## Build the Phorcys Docker container

*Note: The Docker integration is not implemented yet, this method is currently unvailable.*

If you're afraid of a payload compromising your system during decoding, you might want to run Phorcys in a container.

As compression-based logic bombs are capable of impacting your host, a Docker Compose file is provided, setting up the container with a configurable memory limit to mitigate such attack.

Run the following command at the root of this repository to build the Phorcys container:

```
$ docker build -t phorcys -f Docker/Dockerfile .
```

## Arguments reference

```
$ phorcys_decode.py -h
usage: phorcys_decode.py [-h] [-y YARA_FILE] [-f FLOW_FILE] [-b BINARY_FILE]
                         [-p]

Recursive network payloads decoder.

optional arguments:
  -h, --help      show this help message and exit
  -y YARA_FILE    path to file containing Yara rules
  -f FLOW_FILE    path to the MITM dump (.flow)
  -b BINARY_FILE  path to the file containing the payload to decode
  -p              list loaded plugins
```