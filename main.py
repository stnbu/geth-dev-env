#!/usr/bin/env python

import sys
import subprocess
import json
import tempfile

genesis_block = {
    u'alloc': {},
    u'config': {
        u'chainId': 15,
        u'eip155Block': 0,
        u'eip158Block': 0,
        u'homesteadBlock': 0
    },
    u'difficulty': u'400',
    u'gasLimit': u'2100000'
}

def geth(args=[], stdin=None):

    cmd = ['geth'] + args
    p = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, err = p.communicate(stdin)
    if p.returncode:
        raise Exception(err)

def init(path):

    with tempfile.NamedTemporaryFile(delete=False) as f:
        json.dump(genesis_block, f, indent=4)
        f.flush()
        args = ['--datadir', path, 'init', f.name]
        geth(args)


def main():

    init('./fdsfdas')
    return 0


if __name__ == '__main__':

    sys.exit(main())