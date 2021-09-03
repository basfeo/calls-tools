#!/usr/bin/env python3

import shutil

total, used, free = shutil.disk_usage(__file__)
STR_SIZE='size{instance="172.24.55.155:9090", job="node-exporter"}'
STR_USED='used{instance="172.24.55.155:9090", job="node-exporter"}'
STR_AVAIL='avail{instance="172.24.55.155:9090", job="node-exporter"}'


print('{} {}\n{} {}\n{} {}\n'.format(STR_SIZE, total, STR_USED, used, STR_AVAIL, free))
path_to_file = "/root/docker-task/node-exporter/free.prom"
with open(path_to_file, "w") as f:
    f.write('{} {}\n{} {}\n{} {}\n'.format(STR_SIZE, total, STR_USED, used, STR_AVAIL, free))
    f.close