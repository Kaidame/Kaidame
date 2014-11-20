import kaidame
from kaidame import *
from kaidame.Core import *


def optsargs():
    log("Checking boot time arguments", "INFO")
    from optparse import OptionParser

    p = OptionParser()
    p.add_option('-i', '--ip', default=None,
                 dest='ip', help="Specify IP required")
    p.add_option('-t', '--type', default=None,
                 dest='type', help="What site to check against:VirusTotal, AbuseIP, robtex, IPLookup or LDAP")
    p.add_option('-p', '--packet', default=None,
                 dest='intrusion', help="Intrusion Packet Decoder")
    p.add_option('-c', '--computer', default=None,
                 dest='pcname', help='Computername to lookup')

    kaidame.options, kaidame.args = p.parse_args()
