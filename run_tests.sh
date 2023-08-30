#!/bin/bash
echo "priting"
echo $(ls -ld $PWD/*)
echo $(pwd)

WORKSPACE=$(pwd)
pytest --color=yes \
--html $WORKSPACE/reports/pytest-report.html
