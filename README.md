## Description

*Phorcys* is a recursive payload decoder. It will recursively decode and inspect binary and text content.

As an example, it is able to decode a `base64` encoded JSON field which has been compressed in `gzip` and encoded in `base64`. *Phorcys* creates either a tree or a forest depending on input format. In case of a binary file,

You will get a tree in which the root corresponds to the format/algorithm detected from the file content. Then, each child  corresponds to the format/algorithm detected from the content extracted/decoded by the parent node. In case of a `.flow` file, each root corresponds to a single flow.

*Phorcys* is the analysis engine of [PiPrecious](https://github.com/PiRanhaLysis/PiPrecious).

## Supported encoding protocols

* base64
* bzip
* css
* gzip
* html
* http headers
* json
* lzma
* multipart
* protobuf
* text (utf-8)
* urlencoded
* zlib

## Usage 

It can be fed with a `.flow` file (from `mitmdump`) or with a binary file. In the case of a `.flow` file, *Phorcys*  will, for each flow, recursively decompress/decode:

* URLs
* request payloads
* response payloads

## Examples

See the following documents for usage examples:

* [Binary file example](doc/example_bin.md)
* [Yara rules example](doc/example_yara.md)
* [Flow file example](doc/example_flow.md)

## Installation

See the [installation guide](doc/install.md).

