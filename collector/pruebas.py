from pysnmp.entity.rfc3413.oneliner import cmdgen

cmdGen = cmdgen.CommandGenerator()


server_ip="10.0.3"
print ("\nFetching stats for...", server_ip)
errorIndication, errorStatus, errorIndex, varBindTable = cmdGen.bulkCmd(
    cmdgen.CommunityData('$1$5.v/c/$'),
    cmdgen.UdpTransportTarget((server_ip, 161)),
    0,25,
    '1.3.6.1.4.1.25506.2.6.1.1.1.1.5'
)

for varBindTableRow in varBindTable:
    for name, val in varBindTableRow:
            print('%s = Interface Name: %s' % (name.prettyPrint(), val.prettyPrint()))