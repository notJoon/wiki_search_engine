#!/bin/bash

function pip3_install {
    for p $@; do
        sudo pip3 install $p 
        if [ $? -ne 0 ]; then 
            echo "could not install $p - abort"
            exit 1
        fi
    done
}

pip3_install lxml
pip3_install nltk
pip3_install requests