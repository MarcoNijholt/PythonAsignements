import datetime
startTime = str(datetime.datetime.now())
import configparser
import logging

config = configparser.ConfigParser()
config.read('config.ini')
snmpData = config['snmp']

try:
    if config['logging']['loglevel'] == '1':
        logging.basicConfig(filename=config['logging']['path'], level=logging.CRITICAL)
    elif config['logging']['loglevel'] == '2':
        logging.basicConfig(filename=config['logging']['path'], level=logging.ERROR)
    elif config['logging']['loglevel'] == '3':
        logging.basicConfig(filename=config['logging']['path'], level=logging.WARNING)
    elif config['logging']['loglevel'] == '4':
        logging.basicConfig(filename=config['logging']['path'], level=logging.INFO)
    elif config['logging']['loglevel'] == '5':
        logging.basicConfig(filename=config['logging']['path'], level=logging.DEBUG)
    else:
        logging.basicConfig(filename=config['logging']['path'], level=logging.CRITICAL)
except PermissionError:
    print("Kan geen logbestanden schrijven omdat python geen toegang heeft tot het logbestand")
except:
    print("Onbekende fout opgetreden, logging is niet mogelijk")

logging.info("[" + startTime + '] Started script')

if config['debug']['debuglevel'] == '1':
    for key, value in snmpData.items():
        print(key + ": " + value)


#voorbeeld voor logging binnen snmp
####    python module niet geinstalleerd  gekregen

# from pysnmp.entity.rfc3413.oneliner import cmdgen
#
# cmdGen = cmdgen.CommandGenerator()
#
# errorIndication, errorStatus, errorIndex, varBinds = cmdGen.getCmd(
#     cmdgen.CommunityData('demopublic'),
#     cmdgen.UdpTransportTarget(('test.net-snmp.org', 161)),
#     cmdgen.MibVariable('SNMPv2-MIB', 'sysName', 0)
# )
#
# # Check for errors and print out results
# if errorIndication: # error in snmp-engine
#     print("Error indicator: ", errorIndication)
#     logging.info("[" + str(datetime.datetime.now()) + '] Error indicator: ', errorIndication)
# else:
#     if errorStatus:  # error in snmp-communication
#         print('%s at %s' % (
#             errorStatus.prettyPrint(),
#             errorIndex and varBinds[int(errorIndex)-1] or '?'  # print object that caused the error
#         ))
#     else:
#         for name, val in varBinds:
#             print('%s = %s' % (name.prettyPrint(), val.prettyPrint()))



##UML IN LES


logging.info("[" + str(datetime.datetime.now()) + '] Script ended')