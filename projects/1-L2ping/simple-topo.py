from mininet.net import Mininet
from mininet.topo import Topo
from mininet.nodelib import LinuxBridge
from mininet.cli import CLI

NUM_HOSTS = 4

class SingleSwitchTopo( Topo ):
    "Single switch connected to k hosts."

    def build( self, k=2, **_opts ):
        "k: number of hosts"
        self.k = k
        switch = self.addSwitch( 's1', cls=LinuxBridge)
        for h in range( 1, k+1 ):
            host = self.addHost( 'h%s' % h, ip=None )
            self.addLink( host, switch )

topo = SingleSwitchTopo(NUM_HOSTS)
net = Mininet(topo=topo, controller=None)
net.start()

try:
    sw = net.get('s1')
    sw.dpctl('setageing', 's1', '0')

    CLI(net)
finally:
    net.stop()
