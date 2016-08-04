#!/bin/bash
# DO NOT USE environment = COPY_ALL
#@ wall_clock_limit = 04:30:00,04:29:30
## with softlimit
#@ job_name = syvolt
#@ job_type = parallel
#@ class = fat
#@ node = 1
#@ total_tasks = 1
#@ node_usage = not_shared
#@ initialdir = $(home)/SyVOLT
#@ output = job$(jobid).out
#@ error = job$(jobid).err
#@ notification=always
#@ notify_user=bentleyjoakes@gmail.com
#@ queue
. /etc/profile
. /etc/profile.d/modules.sh
date
python3.3 test_mbeddr.py
date
