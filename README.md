# Animexx Utilities

It's not easy to use, yet, but good enough for automating some stuff.

Get the required values from your browser session.

Example, assuming `12345` is your Animexx user ID, `21d6f40cfb511982e4424e0e250a9557` is the `PHPSESSION` cookie and `d56b699830e77ba53855679cb1d252da` is the `autologin` cookie:
```sh
cd animexx-utils
./ktfetch --user 12345 --session 21d6f40cfb511982e4424e0e250a9557 --login d56b699830e77ba53855679cb1d252da
```
