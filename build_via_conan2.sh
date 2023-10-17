#!/usr/bin/env bash

# Create the package for internal/1.0.0@adnn
conan create --user adnn Internal/conan/

# Build downstream, depending on internal
conan build Downstream/conan/
