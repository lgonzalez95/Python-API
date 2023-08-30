#!/bin/bash

WORKSPACE=$(pwd)
pytest --color=yes \
--html $WORKSPACE/reports/pytest-report.html
