#!/bin/bash

while true;
do
  SNAPSHOTSTATUS=$(aws elasticache describe-snapshots \
    --region ap-northeast-1 --no-cli-pager\
    | jq ".[].[] | select(.SnapshotSource | test(\"automated\") | not ) | select(.CacheClusterId | test(\"\")) | .SnapshotStatus" | tr -d '"')
  echo "Snapshot status: ${SNAPSHOTSTATUS}"

  if [ ${SNAPSHOTSTATUS} = "available" ]; then
    echo "Snapshot completed: ${NOW}"
    exit 0
  fi
  sleep 30
done

