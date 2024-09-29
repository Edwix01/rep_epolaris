from pysnmp.entity.rfc3413.oneliner import cmdgen

cmdGen = cmdgen.CommandGenerator()

server_ip=f"10.0.1.19"
print ("\nFetching stats for...", server_ip)
errorIndication, errorStatus, errorIndex, varBindTable = cmdGen.bulkCmd(
    cmdgen.CommunityData('$1$5.v/c/$'),
    cmdgen.UdpTransportTarget((server_ip, 161)),
    0,25,
    "1.3.6.1.2.1.1.3"
)

for varBindTableRow in varBindTable:
    for name, val in varBindTableRow:
            print(int(val)/(100*60*60*24*7))

