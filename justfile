default:
    @just --list --unsorted

b:
    @g++ main.cpp --std=c++17 -O2 -o main

r:
    @echo "---- executing ./main ----\n"
    @./main
    @echo "\n----- execution done -----"

bnr: b r
