#!/bin/bash

#
# simple demo showing how we can deploy code to
# smart machines running viam server
#
#

SCRIPT_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )

if [[ ! -f ${SCRIPT_DIR}/venv/bin/python ]]; then
  echo "Setting up virtual environment & installing requirements"
  python3 -m venv ${SCRIPT_DIR}/venv
  exec ${SCRIPT_DIR}/venv/bin/python -m pip install -r ${SCRIPT_DIR}/requirements.txt
else
  echo "virtual environment exists, will not run setup"
fi

if [[ -f ${SCRIPT_DIR}/web-app.tar.gz ]]; then
  echo "found install, attempting install"
  source ./web_vars.sh
  tar -xf ${SCRIPT_DIR}/web-app.tar.gz -C ${WEB_APP_INSTALL_DIR}
  ${WEB_APP_INSTALL_DIR}/web-app/install.sh
  ${WEB_APP_INSTALL_DIR}/web-app/web.sh start
  rm -rf ${SCRIPT_DIR}/web-app.tar.gz
fi

exec "${SCRIPT_DIR}"/venv/bin/python3 "${SCRIPT_DIR}"/main.py "$@"