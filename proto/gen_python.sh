#!/bin/sh
if [ ! -d "../client/api" ]; then
  mkdir ../client/api
fi
protoc --python_out=../client/api *.proto