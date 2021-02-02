# logatec-experiment

Continuous delivery template - repository for making experiments in LOG-aTEC testbed with Contiki-NG OS.

## Get repository

To get the repository:
>```$ git clone git@github.com:logatec3/logatec-experiment.git```

To also get the sub-modules files:
>```$ git submodule update --init```

Do it in one step (but you will also get all nested sub-modules, which we usually do not need)
>```$ git clone --recurse-submodules git@github.com:logatec3/logatec-experiment.git```

**NOTE** \
`git pull` will only pull the changes of the base repo.
If you want to pull the changes of the sub-module as well use: ```$ git submodule update --remote``` \
You can also add `--merge` or `--rebase` to merge/rebase your branch with remote.

If you want to make some changes to the sub-modules, first checkout to the branch you want, then commit changes and push them.

## Branches

There are few branches to work with different supported radios:

* SRDA - 868 MHz band
* SRDB - 2.4 GHz ISM band
* BLE - Bluetooth LE
* LoRa
* UWB

## Testbed info

More info about the testbed can be found [here](http://log-a-tec.eu/index.html "Official web-site")
