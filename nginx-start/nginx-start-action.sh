#!/bin/bash

SRC_DIR=$(dirname $0)
echo $SRC_DIR

nohup $SRC_DIR/../bin/nginx-action.sh > /tmp/actions.out &
