#!/bin/bash
# MIT License
# 
# Copyright (c) 2019 Stefano Prina
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

## CONFIGURATION
CC=pyinstaller
CC_OPT=-F
TARGET=app
VERSION=`grep -rn "VERSION"  app_modules/core/constants.py  | head -n 1 | cut -d "=" -f 2 | tr -d \' | tr -d " " | tr -d "\"""`

## FUNCTIONS
my_clean () {
	rm -rvf ./build
}

dist_clean ()  {
	my_clean
	rm -rvf ./dist
	rm -rvf ./env
}

my_build () {
	my_makenv
	$CC $CC_OPT $TARGET
}

my_install () {
	my_build
	install -v ./dist/app $1
	deactivate
}

print_usage () {
	echo "Usage :"
	echo "$0 clean"
	echo "$0 distclean"
	echo "$0 build"
	echo "$0 install target_path"
	echo "$0 makenv"
	echo "$0 help"
}

my_package () {
	my_build

	tar -cf ./dist/app_$VERSION.tar -C ./dist/app
	tar -f ./dist/app_$VERSION.tar -r README.md
	tar -f ./dist/app_$VERSION.tar -r LICENSE
	gzip ./dist/app_$VERSION.tar
	deactivate
}

my_makenv() {
	if [ ! -f env/bin/activate ]; then
		virtualenv -p python3 env
		source env/bin/activate
		pip install -r requirements.txt
	else
		source env/bin/activate
	fi
}

case "$1" in
	"clean" ) my_clean ;;
	"distclean" ) dist_clean ;;
	"build" ) my_build ;;
	"install" ) my_install $2 ;;
	"package" ) my_package ;;
	"makenv" ) my_makenv ;;
	* ) print_usage ;;
esac
