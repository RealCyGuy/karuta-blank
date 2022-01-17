# karuta-blank

Efficiently blank karuta sketches.

**Disclaimer: It's not my fault if you get sketch banned or even blacklisted from the bot. I got sketch banned. This is just for archive purposes. Use at your own risk.**

## Installation

- Install [python 3](https://www.python.org/downloads/)
- Download this git repo
- Install requirements with `pip install -r requirements.txt`

## Usage

- Fill out `.env` with your variables.
  - `FRAME`: explosion, festivus, carnations, or ed3. Explosion covers the most.
  - `COLOUR`: Any accepted colour in hex format. #ffffff = white.
  - `URL`: Karuta sketch url. Example: `https://karuta.xyz/api/studio/j93bxdnpoy7hwd7z9575vnnog355r75l`
  - `AUTHORIZATION`: Sketch auth key. You can get by pressing `f12` and going to application tab > local storage > authorization.
- Run `blank.py`.
- Copy to sketch website console and run it.
- Refresh sketch page.
