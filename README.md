# pylnbits

Pull Requests are Welcome!

An asyncio/aiohttp python library of methods for accessing [lnbits](https://github.com/lnbits/lnbits/) API or your own install. For use when building front end or app layer projects with lnbits. 

## Getting Started

version at least python3.8

```
git clone https://github.com/lightningames/pylnbits
cd pylnbits
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
pip install -e .
```

This is experimental software. The only modules & Extensions covered presently are: 

- User Wallet 
- User Manager
- LNURLp
- LNURLw
- LndHub

If you would like to contribute, please feel free to make a pull request. 


## Library Installation

current release is 0.0.3
only effective up to LNBITS commit 
https://github.com/lnbits/lnbits-legend/commit/e46e881663eb4d70b691e09ac1c97eecd6b547b8

```
pip install pylnbits
````

https://pypi.org/project/pylnbits/

## Other

Check linting and formatting
`pre-commit run -a`

Build for distribution
`python3 setup.py build`



Run Tests

```
TBD
TBD
```
