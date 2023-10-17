#!/usr/bin/env bash

rm -r ./Downstream/build*
rm -r ./Internal/build*

conan remove -c internal/1.0.0@adnn
