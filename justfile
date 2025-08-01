_default:
    @just --list --unsorted

# build main.cpp
b:
    @echo "• compiling main.cpp..."
    @g++ main.cpp --std=c++20 -O2 -o main

# run ./main
r:
    @echo "• executing ./main"
    @./main

# build & run
br: b r

# copy main.cpp to clipboard
c:
    @xsel --clipboard < main.cpp
    @echo "• copied code to clipboard. all the best for your AC ❄"

# open main.cpp with helix
h:
    @hx main.cpp

# renew main.cpp from template
n:
    @cp template main.cpp
    @echo "• renewed main.cpp. type 'just h' to open in helix"

# add snippet
as:
    @./scripts/add_snippet.sh

# remove snippet
rs:
    @./scripts/remove_snippet.sh

# list snippet
ls:
    @./scripts/list_snippets.sh

# show snippet
ss:
    @./scripts/show_snippet.sh
