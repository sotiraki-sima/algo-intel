#!/bin/sh

list_of_regex=(
                "(eyJ)[A-Za-z0-9_=\-]{30,}\.(eyJ)[A-Za-z0-9_=\-]{20,}\.[A-Za-z0-9_=\-]{20,}"  # JWT
                "(([Ss][Ee][Cc][Rr][Ee][Tt])|([Pp][Aa][Ss][Ss][Ww][Oo][Rr][Dd]))(\s){0,1}[=:]{1}(\s){0,1}[A-Za-z0-9_=\-]{5,}" # PASSWORD
                "(aws_access_key_id)(\s){0,1}[=:]{0,1}(\s){0,1}[A-Za-z0-9_=\-]{20}" # aws_access_key_id = (20)
                )

for t in ${list_of_regex[@]}; do
    grep --color=always -nrI -E --exclude-dir=.git --exclude-dir=doc --exclude-dir=./ --exclude-dir=.svn --exclude-dir=node_modules $t .
done
