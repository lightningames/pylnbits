# pylnbits

Pull Requests are Welcome!

An asyncio/aiohttp python library of methods for accessing [lnbits](https://github.com/lnbits/lnbits/) API or your own install. For use when building front end or app layer projects with lnbits. 

## Read the Docs

https://lightningames.github.io/pylnbits/

See also [Powered-by-LNBits](https://github.com/lnbits/lnbits/wiki/Powered-by-LNbits) for more resources. 
This project, [pylnbits](https://github.com/lightningames/pylnbits), is also listed on the Powered by LNbits wiki. 

## Updating the docs

See mkdocs for guidance on how to update docs and also https://github.com/lightningames/pylnbits/blob/main/mkdocs.yml


deploy to github pages: 

https://www.mkdocs.org/user-guide/deploying-your-docs/#github-pages


```
mkdocs gh-deploy
```

## Getting Started

### With Poetry

poetry version at least 1.4.2

```
git clone https://github.com/lightningames/pylnbits
poetry install
```

### With Virtual Env

version at least python3.8

```
git clone https://github.com/lightningames/pylnbits
cd pylnbits
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
pip install -e .
```

Copy config_sample.yml to config.yml and update the variables with your lnbits install:

```
lnbits_url: "https://lnbits.com"
in_key: "fill in with your Invoice Key here"
admin_key: "fill with your admin key here "
```

Run tests in tests directory to see sample usage.

NOTE: This is experimental software. The only modules & Extensions covered presently are: 

- User Wallet 
- User Manager
- LNURLp
- LNURLw
- LndHub
- Invoices

If you would like to contribute, please feel free to make a pull request. 


## Library Installation

current release is 0.0.8, tested to LNBits 0.11.2

```
pip install pylnbits
````

https://pypi.org/project/pylnbits/

## Other

Check linting and formatting
`pre-commit run -a`

Build for distribution
`python3 setup.py build`

Also see Tutorials for build to release on PyPi for uploading distribution archives
https://packaging.python.org/en/latest/tutorials/packaging-projects/



Run Examples

See the `tests` directory for working examples
