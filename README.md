# cp

the most seemless, blazing-fast way to solve competitive programming problems.

tailored for `C++` devs using `helix-editor`.

## prerequisites:

- [helix](https://helix-editor.com/)
- [python 3.13](https://www.python.org/)
- [ubuntu 24.04](https://ubuntu.com/) (i never tested on other os, so... good luck lol.)

## installation:

### create python venv:
```
python -m venv .venv
.venv/bin/pip install -r requirements.txt
```

### install clangd & clang-format:
```
sudo apt install clangd clang-format
```

### install hx-lsp:
```
# install rust
# ref: https://www.rust-lang.org/tools/install
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
. "$HOME/.cargo/env"

cargo install --force hx-lsp
```

> _more setup instructions coming soon._

## precompile debug.h:

```
g++ -std=c++20 -O2 -x c++-header debug.h
```
