#!/usr/bin/env bash

set -e

pushd Internal
mkdir -p build
cd build
cmake .. -DCMAKE_INSTALL_PREFIX=../../sdk/internal
cmake --build . --target install
popd

pushd Downstream
mkdir -p build
cd build
cmake .. -DCMAKE_INSTALL_PREFIX=../../sdk/downstream \
         -DCMAKE_PREFIX_PATH=$(pwd)/../../sdk/
cmake --build . --target install
popd

echo
echo "BUILD SUCCESS"
echo

./sdk/downstream/bin/myapp

