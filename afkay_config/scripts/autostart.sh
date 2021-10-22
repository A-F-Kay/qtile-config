#!/bin/bash


function run {
	if ! pgrep $1 > /dev/null ;
	then
		$@&
	fi
}

run picom --experimental-backend &
run nitrogen --restore &

