#!/bin/bash
RUN_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )";
echo $RUN_DIR
CMD="python3 $RUN_DIR/run.py -c $RUN_DIR/config.yaml >> $RUN_DIR/run.log"
echo "0 9 * * *   root    $CMD" > /etc/cron.d/xtunnel_checkin;
/etc/init.d/cron reload;
