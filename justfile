default:
    @just --list --unsorted

b:
    @echo "• compiling main.cpp..."
    @g++ main.cpp --std=c++20 -O2 -o main

r:
    @echo "• executing ./main"
    @./main

br: b r

c:
    @xsel --clipboard < main.cpp
    @echo "• copied code to clipboard. all the best for your AC ❄"

h:
    @hx main.cpp

n:
    @cp template main.cpp
    @echo "• renewed main.cpp. type 'just h' to open in helix"

as:
    @./scripts/add_snippet.sh
