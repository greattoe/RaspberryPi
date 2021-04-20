#!/bin/sh

FILENAME=${1}

sed -i "s/\r//" ./${FILENAME}
