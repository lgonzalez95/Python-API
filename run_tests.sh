#!/bin/bash
WORKSPACE=$(pwd)
echo "WORKSPACE $WORKSPACE "
pytest --color=yes \
--html $WORKSPACE/reports/pytest-report.html
