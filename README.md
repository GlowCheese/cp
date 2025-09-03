# cp

the most seemless, blazing-fast way to solve competitive programming problems.

tailored for `C++` devs using `helix-editor`.

## prerequisites:

- [uv](https://docs.astral.sh/uv/)
- [helix](https://helix-editor.com/)

## installation:

### sync project:
```
uv sync
```

### install clangd & clang-format:
**Ubuntu:**
```
sudo apt install clangd clang-format
```

**Fedora:**
```
sudo dnf install clang-tools-extra
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
