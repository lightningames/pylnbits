# Reference

This part of the project documentation focuses on
an **information-oriented** approach. Use it as a
reference for the technical implementation of the
`pylnbits` project code.

::: pylnbits

::: pylnbits.config

::: pylnbits.user_wallet

::: pylnbits.user_manager

::: pylnbits.lnurl_p

::: pylnbits.lnurl_w

::: pylnbits.lndhub

--

## Project layout

    mkdocs.yml    # The configuration file.
    docs/
        index.md  # The documentation homepage.
        ...       # Other markdown pages, images and other files.
    config_sample.yml
    pylnbits/
        __init__.py
        config.py
        lndhub.py
        lnurl_p.py
        lnurl_w.py
        user_manager.py
        user_wallet.py
        utils.py
    tests/
        __init__.py
        test_lndhub.py
        test_lnurlp.py
        test_lnurlw.py
        test_usermanager.py
        test_userwallet.py
