# Rust cookbook

## Install

```shell
# Rust programming language
# https://www.rust-lang.org/tools/install
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
# Install formatting tool
rustup component add rustfmt
```


## Format + linting

```bash
cargo clippy -- -W clippy::all -W clippy::pedantic -W clippy::nursery -W clippy::restriction -A clippy::mod_module_files -A clippy::implicit-return -A clippy::missing-inline-in-public-items -A clippy::std-instead-of-core -A clippy::indexing-slicing -A clippy::integer-arithmetic -A clippy::arithmetic-side-effects

cargo fmt
```