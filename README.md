# cp

the most seemless, blazing-fast way to solve competitive programming problems.

tailored for `C++` devs using `helix-editor`.

## prerequisites:

- [uv](https://docs.astral.sh/uv/)
- [helix](https://helix-editor.com/)
- [rust](https://rust-lang.org/)

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
cargo install --force hx-lsp
```

## precompile debug.h:

```
g++ -std=c++20 -O2 -x c++-header debug.h
```
