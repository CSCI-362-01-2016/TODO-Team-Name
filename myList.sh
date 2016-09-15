#!/usr/bin/env bash

cat << _EOF_
"<!DOCTYPE html>" > myList.html
"<HTML>" >> myList.html
"<HEAD>" >> myList.html
"<TITLE>" >> myList.html
"<$(pwd)" >> myList.html
"</TITLE>" >> myList.html
"</HEAD>" >> myList.html
"<BODY>" >> myList.html
_EOF_

for f in $( ls );
do
    echo "$f" >> myList.html
    echo "</br>" >> myList.html
done

echo "</body>" >> myList.html
echo "</html>" >> myList.html
xdg-open myList.html