#!/bin/bash

set -ue

PROFILE=${1}
SG_ID=${2}

ips=$(curl -s http://d7uri8nf7uskq.cloudfront.net/tools/list-cloudfront-ips)
old_ips=$(aws ec2 describe-security-groups --group-ids ${SG_ID} --profile ${PROFILE} | jq '.SecurityGroups[].IpPermissions[].IpRanges[]' | jq -sSc .)
new_ips=$((echo $ips | jq '.CLOUDFRONT_REGIONAL_EDGE_IP_LIST[] | { CidrIp: . }' ) | jq -Ssc .)

old_json=$(cat <<EOC
[
  {
    "IpProtocol": "tcp", "FromPort": 443, "ToPort": 443,
    "IpRanges": ${old_ips}
  }
]
EOC
)

new_json=$(cat <<EOC
[
  {
    "IpProtocol": "tcp", "FromPort": 443, "ToPort": 443,
    "IpRanges": ${new_ips}
  }
]
EOC
)

aws ec2 revoke-security-group-ingress --group-id ${SG_ID} --profile ${PROFILE} --ip-permissions "$(echo ${old_json} | jq . -c)"
aws ec2 authorize-security-group-ingress --group-id ${SG_ID} --profile ${PROFILE} --ip-permissions "$(echo ${new_json} | jq . -c)"

