#!/bin/bash
WORKSPACE="$(dirname "$(readlink -f "$0")")"
echo "WORKSPACE $WORKSPACE "
pytest --color=yes \
--html $WORKSPACE/reports/pytest-report.html
