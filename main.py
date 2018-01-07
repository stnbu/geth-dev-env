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

def run(path):

    args = ['--rpc', '--datadir', path, '&']
    geth(args)

def main():

    path = './xyz'
    init(path)
    run(path)
    return 0


if __name__ == '__main__':

    sys.exit(main())# 10141  geth console
# 10147  geth console
# 10149  ps axu | grep -i geth
# 10162  echo 'geth --identity "MyNodeName" --rpc --rpcport "8080" --rpccorsdomain "*" --datadir "C:\chains\TestChain1" --port "30303" --nodiscover --rpcapi "db,eth,net,web3" --networkid 1999 init /path/to/CustomGenesis.json' > geth.sh
# 10163  ec -n geth.sh 
# 10164  chmod 755 geth.sh
# 10165  ./geth.sh 
# 10166  geth --version
# 10167  ./geth.sh 
# 10189  cat ../geth.sh
# 10190  ./geth.sh console
# 10191  ./geth.sh --mine --minerthreads=4
# 10192  ./geth.sh console
# 10202  geth --version | less
# 10205  ./geth.sh --mine --minerthreads=4
# 10220  ./geth.sh console
# 15151  brew search geth
# 15152  brew show geth
# 15153  brew info geth
# 15156  brew install geth
# 15165  ls -ltr ~/Downloads/geth-alltools-darwin-amd64-1.7.3-4bb3c89d.tar.gz 
# 15168  tar -xf ~/Downloads/geth-alltools-darwin-amd64-1.7.3-4bb3c89d.tar.gz 
# 15186  geth --datadir "${ethereum_home}/testnet" init ~/ethereum/genesis.json 
# 15189  geth --datadir "${ethereum_home}/testnet" init ~/ethereum/genesis.json 
# 15190  geth --datadir "${ethereum_home}/testnet" console 2>/dev/null
# 15195  geth attach ipc:./geth.ipc 
# 15196  geth --nodiscovery attach ipc:./geth.ipc 
# 15197  geth --nodiscover attach ipc:./geth.ipc 
# 15198  geth --nodiscover --datadir "${ethereum_home}/testnet" console 2>/dev/null
# 15205  geth --datadir "${ethereum_home}/testnet2" init ./genesis.json 
# 15208  geth --nodiscover attach ipc:./geth.ipc 
# 15211  geth --datadir ./testnet2 --port 30304 --nodiscover --networkid 1234 console 2>/dev/null 
# 15213  geth --nodiscover --datadir "${ethereum_home}/testnet" --networkid 1234 console 2>/dev/null
# 15219  git clone git@github.com:stnbu/geth-dev-env.git
# 15220  cd geth-dev-env/
# 15229  geth --help
# 15230  grep geth ~/.bash_history
# 15233  ~/git/geth-dev-env/main.py 
# 15234  geth --help | less
# 15235  ~/git/geth-dev-env/main.py 
# 15238  ~/git/geth-dev-env/main.py 
# 15242  ~/git/geth-dev-env/main.py 
# 15244  ~/git/geth-dev-env/main.py 
# 15247  geth --datadir ./ init /var/folders/gc/n88bs5vn5f15w8kj2_56sdj000b5j1/T/tmpO6W96m
# 15250  ~/git/geth-dev-env/main.py 
# 15274  ps axu | grep -i geth
# 15275  ~/git/geth-dev-env/main.py 
# 15278  ~/git/geth-dev-env/main.py 
# 15279  history | grep geth
# 15280  history | grep geth | sed 's/^/# /'
# 15281  history | grep geth | sed 's/^/# /' >> ~/git/geth-dev-env/main.py 
