#!/bin/bash
echo ls
echo pwd

WORKSPACE=$(pwd)
pytest --color=yes \
--html $WORKSPACE/reports/pytest-report.html
