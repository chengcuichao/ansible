#!/bin/bash
rabbitmqctl set_policy ha-all "." '{"ha-mode":"exactly","ha-params":3,"ha-sync-mode":"automatic"}'