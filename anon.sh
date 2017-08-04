#!/bin/bash

for i in {1..100}
do
	anonsurf start
	sleep 10s
	anonsurf stop
done
