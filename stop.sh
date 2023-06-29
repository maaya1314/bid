#!/bin/bash
BIN_PATH=`dirname $0`
cd ${BIN_PATH}
python cli_bid.py scheduler stop
echo "退出调度程序完成..."