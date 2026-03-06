# SyNCODER

## Project Overview
A DNA codec. (Fill in.)

## Features
Fill in here.
### DDSA Sector 0/1 generator
(Status: incomplete) Generates [sector 0](https://www.snia.org/standards/technology-standards-software/standards-portfolio/dna-data-storage-sector-zero) and [sector 1](https://www.snia.org/standards/technology-standards-software/standards-portfolio/dna-data-storage-sector-one) compliant with the DNA Data Storange Alliance (DDSA) [DNA Archive Rosetta Stone specifiation](https://dnastoragealliance.org/publications/).  Note: The maximum sector 1 size is currenty 325950 bytes.

## Installation
`codec.py` Can be included in a project and used as a local module or installed and used from `pip` :
```
pip install --pre syncoder
```
Note the requirement for the `--pre` flag as there is no official post release yet.

## Usage
To be completed.  For now see `tests/test_codec_pytest.py` for examples

## Testing
It is sufficient to run 
```
pytest
```
from the root directory.  Currently coverage is only for features and parameters in active use.  More tests to come.

## License
BSD-3 clause.  see `LICENSE` file in this directory.
