#!/usr/bin/env python

import peeringdb

from pprint import pprint

pdb = peeringdb.PeeringDB()

# search by ix and name
ix = pdb.all('ix', name='chix', country='us')[0]
pprint(ix)

# get lan on ix
ixlan = pdb.all('ixlan', ix_id=ix['id'])[0]
pprint(ixlan)

# lookup network by ASN
net = pdb.all('net', asn=63311)[0]
pprint(net)

# lookup peer info by network and ixlan
peerings = pdb.all('netixlan', ixlan_id=ixlan['id'], asn=63311)
pprint(peerings)

print("adding peer %s (AS%d)..." % (net['name'], net['asn']))
print("  import %s" % (net['irr_as_set']))
for peer in peerings:
    print("  ipv4: %s (max prefix %d)" % (peer['ipaddr4'], net['info_prefixes4']))
    print("  ipv4: %s (max prefis %d)" % (peer['ipaddr6'], net['info_prefixes6']))


