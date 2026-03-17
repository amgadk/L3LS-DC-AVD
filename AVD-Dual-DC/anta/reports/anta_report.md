# 📊 ANTA Report <a id="anta-report"></a>

**Table of Contents:**

- [ANTA Report](#anta-report)
  - [Test Results Summary](#test-results-summary)
    - [Summary Totals](#summary-totals)
    - [Summary Totals Device Under Test](#summary-totals-device-under-test)
    - [Summary Totals Per Category](#summary-totals-per-category)
  - [Test Results](#test-results)

## 📉 Test Results Summary <a id="test-results-summary"></a>

### 🔢 Summary Totals <a id="summary-totals"></a>

| Total Tests | ✅&nbsp;Success | ⏭️&nbsp;Skipped | ❌&nbsp;Failure | ❗&nbsp;Error |
| :- | :- | :- | :- | :- |
| 444 | 376 | 8 | 58 | 0 |

### 🔌 Summary Totals Device Under Test <a id="summary-totals-device-under-test"></a>

| Device | Total Tests | ✅&nbsp;Success | ⏭️&nbsp;Skipped | ❌&nbsp;Failure | ❗&nbsp;Error | Categories Skipped | Categories Failed |
| :- | :- | :- | :- | :- | :- | :- | :- |
| **dc1-borderleaf1** | 26 | 24 | 0 | 2 | 0 | - | Logging, System |
| **dc1-borderleaf2** | 26 | 24 | 0 | 2 | 0 | - | Logging, System |
| **dc1-leaf1** | 26 | 21 | 0 | 5 | 0 | - | Interfaces, Logging, MLAG, System |
| **dc1-leaf2** | 26 | 21 | 0 | 5 | 0 | - | Interfaces, Logging, MLAG, System |
| **dc1-leaf3** | 26 | 21 | 0 | 5 | 0 | - | Interfaces, Logging, MLAG, System |
| **dc1-leaf4** | 26 | 21 | 0 | 5 | 0 | - | Interfaces, Logging, MLAG, System |
| **dc1-leaf5** | 26 | 16 | 4 | 5 | 0 | MLAG, VXLAN | BGP, Connectivity, Interfaces, Logging, System |
| **dc1-leaf6** | 26 | 16 | 4 | 5 | 0 | MLAG, VXLAN | BGP, Connectivity, Interfaces, Logging, System |
| **dc1-spine1** | 20 | 16 | 0 | 4 | 0 | - | BGP, Connectivity, Logging, System |
| **dc1-spine2** | 20 | 16 | 0 | 4 | 0 | - | BGP, Connectivity, Logging, System |
| **dc2-borderleaf1** | 26 | 24 | 0 | 2 | 0 | - | Logging, System |
| **dc2-borderleaf2** | 26 | 24 | 0 | 2 | 0 | - | Logging, System |
| **dc2-leaf1** | 26 | 24 | 0 | 2 | 0 | - | Logging, System |
| **dc2-leaf2** | 26 | 24 | 0 | 2 | 0 | - | Logging, System |
| **dc2-leaf3** | 26 | 24 | 0 | 2 | 0 | - | Logging, System |
| **dc2-leaf4** | 26 | 24 | 0 | 2 | 0 | - | Logging, System |
| **dc2-spine1** | 20 | 18 | 0 | 2 | 0 | - | Logging, System |
| **dc2-spine2** | 20 | 18 | 0 | 2 | 0 | - | Logging, System |

### 🗂️ Summary Totals Per Category <a id="summary-totals-per-category"></a>

| Test Category | Total Tests | ✅&nbsp;Success | ⏭️&nbsp;Skipped | ❌&nbsp;Failure | ❗&nbsp;Error |
| :- | :- | :- | :- | :- | :- |
| **BGP** | 18 | 14 | 0 | 4 | 0 |
| **Configuration** | 36 | 36 | 0 | 0 | 0 |
| **Connectivity** | 36 | 32 | 0 | 4 | 0 |
| **Interfaces** | 118 | 106 | 0 | 10 | 0 |
| **Logging** | 18 | 0 | 0 | 18 | 0 |
| **MLAG** | 42 | 32 | 6 | 4 | 0 |
| **Routing** | 18 | 18 | 0 | 0 | 0 |
| **STP** | 18 | 18 | 0 | 0 | 0 |
| **System** | 126 | 108 | 0 | 18 | 0 |
| **VXLAN** | 14 | 12 | 2 | 0 | 0 |

## 🧪 Test Results <a id="test-results"></a>

| Device | Categories | Test | Description | Result | Messages |
| :- | :- | :- | :- | :- | :- |
| dc1-borderleaf1 | Logging | VerifyLoggingErrors | Verifies there are no syslog messages with a severity of ERRORS or higher. | ❌&nbsp;Failure | Device has reported syslog messages with a severity of ERRORS or higher:<br>Mar 17 00:27:17 localhost LoadConfig: %SYSDB-3-STARTUP_CONFIG_PARSE_ERROR: Errors encountered in parsing the startup-config<br> Mar 17 00:27:44 dc1-borderleaf1 PhyEthtool-1: %ETH-3-NETLINKFAIL: Cannot init netlink stats cache : NETLINK Error Error fetching statistics  <extra parameters: '-31' ><br> Mar 17 00:27:51 dc1-borderleaf1 ProcMgr: %PROCMGR-3-SHUTDOWNREQUESTED: ProcMgr shutdown requested via SIGQUIT or SIGTERM to worker (PID=1485) -- Master ProcMgr (PID=1485) exiting.<br> Mar 17 00:27:51 dc1-borderleaf1 Stp: %FWK-3-SOCKET_CLOSE_REMOTE: Connection to StpTxRx (pid:1883) at tbl://stpTxRxListen/+n closed by peer (EOF)<br> Mar 17 00:27:51 dc1-borderleaf1 Stp: %FWK-3-MOUNT_PEER_CLOSED: Peer closed socket connection. (tbl://stpTxRxListen/+n-in)(StpTxRx (pid:1883))<br> Mar 17 00:28:08 dc1-borderleaf1 LoadConfig: %SYSDB-3-STARTUP_CONFIG_PARSE_ERROR: Errors encountered in parsing the startup-config<br> <br> |
| dc1-borderleaf1 | System | VerifyNTP | Verifies if NTP is synchronised. | ❌&nbsp;Failure | NTP status mismatch - Expected: synchronised Actual: NTP is disabled. |
| dc1-borderleaf2 | Logging | VerifyLoggingErrors | Verifies there are no syslog messages with a severity of ERRORS or higher. | ❌&nbsp;Failure | Device has reported syslog messages with a severity of ERRORS or higher:<br>Mar 17 00:26:21 localhost LoadConfig: %SYSDB-3-STARTUP_CONFIG_PARSE_ERROR: Errors encountered in parsing the startup-config<br> Mar 17 00:27:53 dc1-borderleaf2 PhyEthtool-1: %ETH-3-NETLINKFAIL: Cannot init netlink stats cache : NETLINK Error Error fetching statistics  <extra parameters: '-31' ><br> Mar 17 00:28:01 dc1-borderleaf2 ProcMgr: %PROCMGR-3-SHUTDOWNREQUESTED: ProcMgr shutdown requested via SIGQUIT or SIGTERM to worker (PID=1485) -- Master ProcMgr (PID=1485) exiting.<br> Mar 17 00:28:01 dc1-borderleaf2 Stp: %FWK-3-SOCKET_CLOSE_REMOTE: Connection to StpTxRx (pid:1873) at tbl://stpTxRxListen/+n closed by peer (EOF)<br> Mar 17 00:28:01 dc1-borderleaf2 Stp: %FWK-3-MOUNT_PEER_CLOSED: Peer closed socket connection. (tbl://stpTxRxListen/+n-in)(StpTxRx (pid:1873))<br> Mar 17 00:28:17 dc1-borderleaf2 LoadConfig: %SYSDB-3-STARTUP_CONFIG_PARSE_ERROR: Errors encountered in parsing the startup-config<br> <br> |
| dc1-borderleaf2 | System | VerifyNTP | Verifies if NTP is synchronised. | ❌&nbsp;Failure | NTP status mismatch - Expected: synchronised Actual: NTP is disabled. |
| dc1-leaf1 | Interfaces | VerifyInterfacesStatus | Verifies the operational states of specified interfaces to ensure they match expected configurations. | ❌&nbsp;Failure | Interface: Port-Channel7 - Status mismatch - Expected: up/up, Actual: down/lowerLayerDown<br>Interface: Port-Channel9 - Status mismatch - Expected: up/up, Actual: down/lowerLayerDown |
| dc1-leaf1 | Interfaces | VerifyPortChannels | Verifies there are no inactive ports in port channels. | ❌&nbsp;Failure | Interface: Port-Channel7 - Inactive port(s) - Ethernet7, PeerEthernet7<br>Interface: Port-Channel9 - Inactive port(s) - Ethernet9, PeerEthernet9 |
| dc1-leaf1 | Logging | VerifyLoggingErrors | Verifies there are no syslog messages with a severity of ERRORS or higher. | ❌&nbsp;Failure | Device has reported syslog messages with a severity of ERRORS or higher:<br>Mar 17 00:27:52 dc1-leaf1 PhyEthtool-1: %ETH-3-NETLINKFAIL: Cannot init netlink stats cache : NETLINK Error Error fetching statistics  <extra parameters: '-31' ><br> Mar 17 00:27:59 dc1-leaf1 ProcMgr: %PROCMGR-3-SHUTDOWNREQUESTED: ProcMgr shutdown requested via SIGQUIT or SIGTERM to worker (PID=1486) -- Master ProcMgr (PID=1486) exiting.<br> Mar 17 00:27:59 dc1-leaf1 StpTxRx: %FWK-3-SOCKET_CLOSE_REMOTE: Connection to Stp (pid:1877) at tbl://stpListen/+n closed by peer (EOF)<br> Mar 17 00:27:59 dc1-leaf1 StpTxRx: %FWK-3-MOUNT_PEER_CLOSED: Peer closed socket connection. (tbl://stpListen/+n-in)(Stp (pid:1877))<br> <br> |
| dc1-leaf1 | MLAG | VerifyMlagInterfaces | Verifies there are no inactive or active-partial MLAG ports. | ❌&nbsp;Failure | MLAG status is not ok - Inactive Ports: 2 Partial Active Ports: 0 |
| dc1-leaf1 | System | VerifyNTP | Verifies if NTP is synchronised. | ❌&nbsp;Failure | NTP status mismatch - Expected: synchronised Actual: NTP is disabled. |
| dc1-leaf2 | Interfaces | VerifyInterfacesStatus | Verifies the operational states of specified interfaces to ensure they match expected configurations. | ❌&nbsp;Failure | Interface: Port-Channel7 - Status mismatch - Expected: up/up, Actual: down/lowerLayerDown<br>Interface: Port-Channel9 - Status mismatch - Expected: up/up, Actual: down/lowerLayerDown |
| dc1-leaf2 | Interfaces | VerifyPortChannels | Verifies there are no inactive ports in port channels. | ❌&nbsp;Failure | Interface: Port-Channel9 - Inactive port(s) - Ethernet9, PeerEthernet9<br>Interface: Port-Channel7 - Inactive port(s) - Ethernet7, PeerEthernet7 |
| dc1-leaf2 | Logging | VerifyLoggingErrors | Verifies there are no syslog messages with a severity of ERRORS or higher. | ❌&nbsp;Failure | Device has reported syslog messages with a severity of ERRORS or higher:<br>Mar 17 00:28:02 dc1-leaf2 PhyEthtool-1: %ETH-3-NETLINKFAIL: Cannot init netlink stats cache : NETLINK Error Error fetching statistics  <extra parameters: '-31' ><br> Mar 17 00:28:09 dc1-leaf2 ProcMgr: %PROCMGR-3-SHUTDOWNREQUESTED: ProcMgr shutdown requested via SIGQUIT or SIGTERM to worker (PID=1484) -- Master ProcMgr (PID=1484) exiting.<br> <br> |
| dc1-leaf2 | MLAG | VerifyMlagInterfaces | Verifies there are no inactive or active-partial MLAG ports. | ❌&nbsp;Failure | MLAG status is not ok - Inactive Ports: 2 Partial Active Ports: 0 |
| dc1-leaf2 | System | VerifyNTP | Verifies if NTP is synchronised. | ❌&nbsp;Failure | NTP status mismatch - Expected: synchronised Actual: NTP is disabled. |
| dc1-leaf3 | Interfaces | VerifyInterfacesStatus | Verifies the operational states of specified interfaces to ensure they match expected configurations. | ❌&nbsp;Failure | Interface: Port-Channel7 - Status mismatch - Expected: up/up, Actual: down/lowerLayerDown<br>Interface: Port-Channel9 - Status mismatch - Expected: up/up, Actual: down/lowerLayerDown |
| dc1-leaf3 | Interfaces | VerifyPortChannels | Verifies there are no inactive ports in port channels. | ❌&nbsp;Failure | Interface: Port-Channel7 - Inactive port(s) - Ethernet7, PeerEthernet7<br>Interface: Port-Channel9 - Inactive port(s) - Ethernet9, PeerEthernet9 |
| dc1-leaf3 | Logging | VerifyLoggingErrors | Verifies there are no syslog messages with a severity of ERRORS or higher. | ❌&nbsp;Failure | Device has reported syslog messages with a severity of ERRORS or higher:<br>Mar 17 00:27:43 dc1-leaf3 PhyEthtool-1: %ETH-3-NETLINKFAIL: Cannot init netlink stats cache : NETLINK Error Error fetching statistics  <extra parameters: '-31' ><br> Mar 17 00:27:50 dc1-leaf3 ProcMgr: %PROCMGR-3-SHUTDOWNREQUESTED: ProcMgr shutdown requested via SIGQUIT or SIGTERM to worker (PID=1489) -- Master ProcMgr (PID=1489) exiting.<br> Mar 17 00:27:50 dc1-leaf3 Stp: %FWK-3-SOCKET_CLOSE_REMOTE: Connection to StpTxRx (pid:1859) at tbl://stpTxRxListen/+n closed by peer (EOF)<br> Mar 17 00:27:50 dc1-leaf3 Stp: %FWK-3-MOUNT_PEER_CLOSED: Peer closed socket connection. (tbl://stpTxRxListen/+n-in)(StpTxRx (pid:1859))<br> <br> |
| dc1-leaf3 | MLAG | VerifyMlagInterfaces | Verifies there are no inactive or active-partial MLAG ports. | ❌&nbsp;Failure | MLAG status is not ok - Inactive Ports: 2 Partial Active Ports: 0 |
| dc1-leaf3 | System | VerifyNTP | Verifies if NTP is synchronised. | ❌&nbsp;Failure | NTP status mismatch - Expected: synchronised Actual: NTP is disabled. |
| dc1-leaf4 | Interfaces | VerifyInterfacesStatus | Verifies the operational states of specified interfaces to ensure they match expected configurations. | ❌&nbsp;Failure | Interface: Port-Channel7 - Status mismatch - Expected: up/up, Actual: down/lowerLayerDown<br>Interface: Port-Channel9 - Status mismatch - Expected: up/up, Actual: down/lowerLayerDown |
| dc1-leaf4 | Interfaces | VerifyPortChannels | Verifies there are no inactive ports in port channels. | ❌&nbsp;Failure | Interface: Port-Channel9 - Inactive port(s) - Ethernet9, PeerEthernet9<br>Interface: Port-Channel7 - Inactive port(s) - Ethernet7, PeerEthernet7 |
| dc1-leaf4 | Logging | VerifyLoggingErrors | Verifies there are no syslog messages with a severity of ERRORS or higher. | ❌&nbsp;Failure | Device has reported syslog messages with a severity of ERRORS or higher:<br>Mar 17 00:27:44 dc1-leaf4 PhyEthtool-1: %ETH-3-NETLINKFAIL: Cannot init netlink stats cache : NETLINK Error Error fetching statistics  <extra parameters: '-31' ><br> Mar 17 00:27:50 dc1-leaf4 ProcMgr: %PROCMGR-3-SHUTDOWNREQUESTED: ProcMgr shutdown requested via SIGQUIT or SIGTERM to worker (PID=1486) -- Master ProcMgr (PID=1486) exiting.<br> Mar 17 00:27:50 dc1-leaf4 Stp: %FWK-3-SOCKET_CLOSE_REMOTE: Connection to StpTxRx (pid:1857) at tbl://stpTxRxListen/+n closed by peer (EOF)<br> Mar 17 00:27:50 dc1-leaf4 Stp: %FWK-3-MOUNT_PEER_CLOSED: Peer closed socket connection. (tbl://stpTxRxListen/+n-in)(StpTxRx (pid:1857))<br> <br> |
| dc1-leaf4 | MLAG | VerifyMlagInterfaces | Verifies there are no inactive or active-partial MLAG ports. | ❌&nbsp;Failure | MLAG status is not ok - Inactive Ports: 2 Partial Active Ports: 0 |
| dc1-leaf4 | System | VerifyNTP | Verifies if NTP is synchronised. | ❌&nbsp;Failure | NTP status mismatch - Expected: synchronised Actual: NTP is disabled. |
| dc1-leaf5 | BGP | VerifyBGPPeerSession | Verifies the session state of BGP peers. | ❌&nbsp;Failure | 'show bgp neighbors vrf all' failed on dc1-leaf5: BGP inactive |
| dc1-leaf5 | Connectivity | VerifyReachability | Verifies point-to-point reachability between Ethernet interfaces. | ❌&nbsp;Failure | Destination 192.168.103.72 (dc1-spine1_Ethernet5) from 192.168.103.73 in VRF default - Error when executing ping: 'ping: bind: Cannot assign requested address'<br>Destination 192.168.103.74 (dc1-spine2_Ethernet5) from 192.168.103.75 in VRF default - Error when executing ping: 'ping: bind: Cannot assign requested address' |
| dc1-leaf5 | Interfaces | VerifyInterfacesStatus | Verifies the operational states of specified interfaces to ensure they match expected configurations. | ❌&nbsp;Failure | Interface: Loopback0 - Not configured<br>Interface: Loopback1 - Not configured<br>Interface: Port-Channel5 - Not configured<br>Interface: Vlan10 - Not configured<br>Interface: Vlan20 - Not configured<br>Interface: Vlan3009 - Not configured<br>Interface: Vlan3019 - Not configured<br>Interface: Vlan4093 - Not configured<br>Interface: Vlan4094 - Not configured<br>Interface: Vxlan1 - Not configured |
| dc1-leaf5 | Logging | VerifyLoggingErrors | Verifies there are no syslog messages with a severity of ERRORS or higher. | ❌&nbsp;Failure | Device has reported syslog messages with a severity of ERRORS or higher:<br>Mar 17 00:28:11 dc1-leaf5 PhyEthtool-1: %ETH-3-NETLINKFAIL: Cannot init netlink stats cache : NETLINK Error Error fetching statistics  <extra parameters: '-31' ><br> Mar 17 00:28:17 dc1-leaf5 ProcMgr: %PROCMGR-3-SHUTDOWNREQUESTED: ProcMgr shutdown requested via SIGQUIT or SIGTERM to worker (PID=1484) -- Master ProcMgr (PID=1484) exiting.<br> <br> |
| dc1-leaf5 | System | VerifyNTP | Verifies if NTP is synchronised. | ❌&nbsp;Failure | NTP status mismatch - Expected: synchronised Actual: NTP is disabled. |
| dc1-leaf6 | BGP | VerifyBGPPeerSession | Verifies the session state of BGP peers. | ❌&nbsp;Failure | 'show bgp neighbors vrf all' failed on dc1-leaf6: BGP inactive |
| dc1-leaf6 | Connectivity | VerifyReachability | Verifies point-to-point reachability between Ethernet interfaces. | ❌&nbsp;Failure | Destination 192.168.103.76 (dc1-spine1_Ethernet6) from 192.168.103.77 in VRF default - Error when executing ping: 'ping: bind: Cannot assign requested address'<br>Destination 192.168.103.78 (dc1-spine2_Ethernet6) from 192.168.103.79 in VRF default - Error when executing ping: 'ping: bind: Cannot assign requested address' |
| dc1-leaf6 | Interfaces | VerifyInterfacesStatus | Verifies the operational states of specified interfaces to ensure they match expected configurations. | ❌&nbsp;Failure | Interface: Loopback0 - Not configured<br>Interface: Loopback1 - Not configured<br>Interface: Port-Channel5 - Not configured<br>Interface: Vlan10 - Not configured<br>Interface: Vlan20 - Not configured<br>Interface: Vlan3009 - Not configured<br>Interface: Vlan3019 - Not configured<br>Interface: Vlan4093 - Not configured<br>Interface: Vlan4094 - Not configured<br>Interface: Vxlan1 - Not configured |
| dc1-leaf6 | Logging | VerifyLoggingErrors | Verifies there are no syslog messages with a severity of ERRORS or higher. | ❌&nbsp;Failure | Device has reported syslog messages with a severity of ERRORS or higher:<br>Mar 17 00:27:34 dc1-leaf6 PhyEthtool-1: %ETH-3-NETLINKFAIL: Cannot init netlink stats cache : NETLINK Error Error fetching statistics  <extra parameters: '-31' ><br> Mar 17 00:27:41 dc1-leaf6 ProcMgr: %PROCMGR-3-SHUTDOWNREQUESTED: ProcMgr shutdown requested via SIGQUIT or SIGTERM to worker (PID=1481) -- Master ProcMgr (PID=1481) exiting.<br> <br> |
| dc1-leaf6 | System | VerifyNTP | Verifies if NTP is synchronised. | ❌&nbsp;Failure | NTP status mismatch - Expected: synchronised Actual: NTP is disabled. |
| dc1-spine1 | BGP | VerifyBGPPeerSession | Verifies the session state of BGP peers. | ❌&nbsp;Failure | Peer: 192.168.101.19 VRF: default - Not found<br>Peer: 192.168.101.20 VRF: default - Not found<br>Peer: 192.168.103.73 VRF: default - Not found<br>Peer: 192.168.103.77 VRF: default - Not found |
| dc1-spine1 | Connectivity | VerifyReachability | Verifies point-to-point reachability between Ethernet interfaces. | ❌&nbsp;Failure | Destination 192.168.103.73 (dc1-leaf5_Ethernet1) from 192.168.103.72 in VRF default - Error when executing ping: 'ping: bind: Cannot assign requested address'<br>Destination 192.168.103.77 (dc1-leaf6_Ethernet1) from 192.168.103.76 in VRF default - Error when executing ping: 'ping: bind: Cannot assign requested address' |
| dc1-spine1 | Logging | VerifyLoggingErrors | Verifies there are no syslog messages with a severity of ERRORS or higher. | ❌&nbsp;Failure | Device has reported syslog messages with a severity of ERRORS or higher:<br>Mar 17 00:27:43 dc1-spine1 PhyEthtool-1: %ETH-3-NETLINKFAIL: Cannot init netlink stats cache : NETLINK Error Error fetching statistics  <extra parameters: '-31' ><br> Mar 17 00:27:50 dc1-spine1 ProcMgr: %PROCMGR-3-SHUTDOWNREQUESTED: ProcMgr shutdown requested via SIGQUIT or SIGTERM to worker (PID=1481) -- Master ProcMgr (PID=1481) exiting.<br> Mar 17 00:27:50 dc1-spine1 Stp: %FWK-3-SOCKET_CLOSE_REMOTE: Connection to StpTxRx (pid:1855) at tbl://stpTxRxListen/+n closed by peer (EOF)<br> Mar 17 00:27:50 dc1-spine1 Stp: %FWK-3-MOUNT_PEER_CLOSED: Peer closed socket connection. (tbl://stpTxRxListen/+n-in)(StpTxRx (pid:1855))<br> <br> |
| dc1-spine1 | System | VerifyNTP | Verifies if NTP is synchronised. | ❌&nbsp;Failure | NTP status mismatch - Expected: synchronised Actual: NTP is disabled. |
| dc1-spine2 | BGP | VerifyBGPPeerSession | Verifies the session state of BGP peers. | ❌&nbsp;Failure | Peer: 192.168.101.19 VRF: default - Not found<br>Peer: 192.168.101.20 VRF: default - Not found<br>Peer: 192.168.103.75 VRF: default - Not found<br>Peer: 192.168.103.79 VRF: default - Not found |
| dc1-spine2 | Connectivity | VerifyReachability | Verifies point-to-point reachability between Ethernet interfaces. | ❌&nbsp;Failure | Destination 192.168.103.75 (dc1-leaf5_Ethernet2) from 192.168.103.74 in VRF default - Error when executing ping: 'ping: bind: Cannot assign requested address'<br>Destination 192.168.103.79 (dc1-leaf6_Ethernet2) from 192.168.103.78 in VRF default - Error when executing ping: 'ping: bind: Cannot assign requested address' |
| dc1-spine2 | Logging | VerifyLoggingErrors | Verifies there are no syslog messages with a severity of ERRORS or higher. | ❌&nbsp;Failure | Device has reported syslog messages with a severity of ERRORS or higher:<br>Mar 17 00:27:34 dc1-spine2 PhyEthtool-1: %ETH-3-NETLINKFAIL: Cannot init netlink stats cache : NETLINK Error Error fetching statistics  <extra parameters: '-31' ><br> Mar 17 00:27:41 dc1-spine2 ProcMgr: %PROCMGR-3-SHUTDOWNREQUESTED: ProcMgr shutdown requested via SIGQUIT or SIGTERM to worker (PID=1488) -- Master ProcMgr (PID=1488) exiting.<br> Mar 17 00:27:41 dc1-spine2 Stp: %FWK-3-SOCKET_CLOSE_REMOTE: Connection to StpTxRx (pid:1862) at tbl://stpTxRxListen/+n closed by peer (EOF)<br> Mar 17 00:27:41 dc1-spine2 Stp: %FWK-3-MOUNT_PEER_CLOSED: Peer closed socket connection. (tbl://stpTxRxListen/+n-in)(StpTxRx (pid:1862))<br> <br> |
| dc1-spine2 | System | VerifyNTP | Verifies if NTP is synchronised. | ❌&nbsp;Failure | NTP status mismatch - Expected: synchronised Actual: NTP is disabled. |
| dc2-borderleaf1 | Logging | VerifyLoggingErrors | Verifies there are no syslog messages with a severity of ERRORS or higher. | ❌&nbsp;Failure | Device has reported syslog messages with a severity of ERRORS or higher:<br>Mar 17 00:26:23 localhost LoadConfig: %SYSDB-3-STARTUP_CONFIG_PARSE_ERROR: Errors encountered in parsing the startup-config<br> Mar 17 00:27:43 dc2-borderleaf1 PhyEthtool-1: %ETH-3-NETLINKFAIL: Cannot init netlink stats cache : NETLINK Error Error fetching statistics  <extra parameters: '-31' ><br> Mar 17 00:27:52 dc2-borderleaf1 ProcMgr: %PROCMGR-3-SHUTDOWNREQUESTED: ProcMgr shutdown requested via SIGQUIT or SIGTERM to worker (PID=1483) -- Master ProcMgr (PID=1483) exiting.<br> Mar 17 00:27:52 dc2-borderleaf1 StpTxRx: %FWK-3-SOCKET_CLOSE_REMOTE: Connection to Stp (pid:1882) at tbl://stpListen/+n closed by peer (EOF)<br> Mar 17 00:27:52 dc2-borderleaf1 StpTxRx: %FWK-3-MOUNT_PEER_CLOSED: Peer closed socket connection. (tbl://stpListen/+n-in)(Stp (pid:1882))<br> Mar 17 00:28:09 dc2-borderleaf1 LoadConfig: %SYSDB-3-STARTUP_CONFIG_PARSE_ERROR: Errors encountered in parsing the startup-config<br> <br> |
| dc2-borderleaf1 | System | VerifyNTP | Verifies if NTP is synchronised. | ❌&nbsp;Failure | NTP status mismatch - Expected: synchronised Actual: NTP is disabled. |
| dc2-borderleaf2 | Logging | VerifyLoggingErrors | Verifies there are no syslog messages with a severity of ERRORS or higher. | ❌&nbsp;Failure | Device has reported syslog messages with a severity of ERRORS or higher:<br>Mar 17 00:27:07 localhost LoadConfig: %SYSDB-3-STARTUP_CONFIG_PARSE_ERROR: Errors encountered in parsing the startup-config<br> Mar 17 00:28:10 dc2-borderleaf2 PhyEthtool-1: %ETH-3-NETLINKFAIL: Cannot init netlink stats cache : NETLINK Error Error fetching statistics  <extra parameters: '-31' ><br> Mar 17 00:28:19 dc2-borderleaf2 ProcMgr: %PROCMGR-3-SHUTDOWNREQUESTED: ProcMgr shutdown requested via SIGQUIT or SIGTERM to worker (PID=1486) -- Master ProcMgr (PID=1486) exiting.<br> Mar 17 00:28:36 dc2-borderleaf2 LoadConfig: %SYSDB-3-STARTUP_CONFIG_PARSE_ERROR: Errors encountered in parsing the startup-config<br> <br> |
| dc2-borderleaf2 | System | VerifyNTP | Verifies if NTP is synchronised. | ❌&nbsp;Failure | NTP status mismatch - Expected: synchronised Actual: NTP is disabled. |
| dc2-leaf1 | Logging | VerifyLoggingErrors | Verifies there are no syslog messages with a severity of ERRORS or higher. | ❌&nbsp;Failure | Device has reported syslog messages with a severity of ERRORS or higher:<br>Mar 17 00:28:03 dc2-leaf1 PhyEthtool-1: %ETH-3-NETLINKFAIL: Cannot init netlink stats cache : NETLINK Error Error fetching statistics  <extra parameters: '-31' ><br> Mar 17 00:28:09 dc2-leaf1 ProcMgr: %PROCMGR-3-SHUTDOWNREQUESTED: ProcMgr shutdown requested via SIGQUIT or SIGTERM to worker (PID=1484) -- Master ProcMgr (PID=1484) exiting.<br> <br> |
| dc2-leaf1 | System | VerifyNTP | Verifies if NTP is synchronised. | ❌&nbsp;Failure | NTP status mismatch - Expected: synchronised Actual: NTP is disabled. |
| dc2-leaf2 | Logging | VerifyLoggingErrors | Verifies there are no syslog messages with a severity of ERRORS or higher. | ❌&nbsp;Failure | Device has reported syslog messages with a severity of ERRORS or higher:<br>Mar 17 00:28:02 dc2-leaf2 PhyEthtool-1: %ETH-3-NETLINKFAIL: Cannot init netlink stats cache : NETLINK Error Error fetching statistics  <extra parameters: '-31' ><br> Mar 17 00:28:08 dc2-leaf2 ProcMgr: %PROCMGR-3-SHUTDOWNREQUESTED: ProcMgr shutdown requested via SIGQUIT or SIGTERM to worker (PID=1476) -- Master ProcMgr (PID=1476) exiting.<br> <br> |
| dc2-leaf2 | System | VerifyNTP | Verifies if NTP is synchronised. | ❌&nbsp;Failure | NTP status mismatch - Expected: synchronised Actual: NTP is disabled. |
| dc2-leaf3 | Logging | VerifyLoggingErrors | Verifies there are no syslog messages with a severity of ERRORS or higher. | ❌&nbsp;Failure | Device has reported syslog messages with a severity of ERRORS or higher:<br>Mar 17 00:27:34 dc2-leaf3 PhyEthtool-1: %ETH-3-NETLINKFAIL: Cannot init netlink stats cache : NETLINK Error Error fetching statistics  <extra parameters: '-31' ><br> Mar 17 00:27:41 dc2-leaf3 ProcMgr: %PROCMGR-3-SHUTDOWNREQUESTED: ProcMgr shutdown requested via SIGQUIT or SIGTERM to worker (PID=1485) -- Master ProcMgr (PID=1485) exiting.<br> Mar 17 00:27:41 dc2-leaf3 Stp: %FWK-3-SOCKET_CLOSE_REMOTE: Connection to StpTxRx (pid:1860) at tbl://stpTxRxListen/+n closed by peer (EOF)<br> Mar 17 00:27:41 dc2-leaf3 Stp: %FWK-3-MOUNT_PEER_CLOSED: Peer closed socket connection. (tbl://stpTxRxListen/+n-in)(StpTxRx (pid:1860))<br> <br> |
| dc2-leaf3 | System | VerifyNTP | Verifies if NTP is synchronised. | ❌&nbsp;Failure | NTP status mismatch - Expected: synchronised Actual: NTP is disabled. |
| dc2-leaf4 | Logging | VerifyLoggingErrors | Verifies there are no syslog messages with a severity of ERRORS or higher. | ❌&nbsp;Failure | Device has reported syslog messages with a severity of ERRORS or higher:<br>Mar 17 00:27:44 dc2-leaf4 PhyEthtool-1: %ETH-3-NETLINKFAIL: Cannot init netlink stats cache : NETLINK Error Error fetching statistics  <extra parameters: '-31' ><br> Mar 17 00:27:50 dc2-leaf4 ProcMgr: %PROCMGR-3-SHUTDOWNREQUESTED: ProcMgr shutdown requested via SIGQUIT or SIGTERM to worker (PID=1479) -- Master ProcMgr (PID=1479) exiting.<br> <br> |
| dc2-leaf4 | System | VerifyNTP | Verifies if NTP is synchronised. | ❌&nbsp;Failure | NTP status mismatch - Expected: synchronised Actual: NTP is disabled. |
| dc2-spine1 | Logging | VerifyLoggingErrors | Verifies there are no syslog messages with a severity of ERRORS or higher. | ❌&nbsp;Failure | Device has reported syslog messages with a severity of ERRORS or higher:<br>Mar 17 00:27:53 dc2-spine1 PhyEthtool-1: %ETH-3-NETLINKFAIL: Cannot init netlink stats cache : NETLINK Error Error fetching statistics  <extra parameters: '-31' ><br> Mar 17 00:27:59 dc2-spine1 ProcMgr: %PROCMGR-3-SHUTDOWNREQUESTED: ProcMgr shutdown requested via SIGQUIT or SIGTERM to worker (PID=1485) -- Master ProcMgr (PID=1485) exiting.<br> <br> |
| dc2-spine1 | System | VerifyNTP | Verifies if NTP is synchronised. | ❌&nbsp;Failure | NTP status mismatch - Expected: synchronised Actual: NTP is disabled. |
| dc2-spine2 | Logging | VerifyLoggingErrors | Verifies there are no syslog messages with a severity of ERRORS or higher. | ❌&nbsp;Failure | Device has reported syslog messages with a severity of ERRORS or higher:<br>Mar 17 00:27:44 dc2-spine2 PhyEthtool-1: %ETH-3-NETLINKFAIL: Cannot init netlink stats cache : NETLINK Error Error fetching statistics  <extra parameters: '-31' ><br> Mar 17 00:27:51 dc2-spine2 ProcMgr: %PROCMGR-3-SHUTDOWNREQUESTED: ProcMgr shutdown requested via SIGQUIT or SIGTERM to worker (PID=1482) -- Master ProcMgr (PID=1482) exiting.<br> <br> |
| dc2-spine2 | System | VerifyNTP | Verifies if NTP is synchronised. | ❌&nbsp;Failure | NTP status mismatch - Expected: synchronised Actual: NTP is disabled. |
| dc1-leaf5 | MLAG | VerifyMlagConfigSanity | Verifies there are no MLAG config-sanity inconsistencies. | ⏭️&nbsp;Skipped | MLAG is disabled |
| dc1-leaf5 | MLAG | VerifyMlagInterfaces | Verifies there are no inactive or active-partial MLAG ports. | ⏭️&nbsp;Skipped | MLAG is disabled |
| dc1-leaf5 | MLAG | VerifyMlagStatus | Verifies the health status of the MLAG configuration. | ⏭️&nbsp;Skipped | MLAG is disabled |
| dc1-leaf5 | VXLAN | VerifyVxlanConfigSanity | Verifies there are no VXLAN config-sanity inconsistencies. | ⏭️&nbsp;Skipped | VXLAN is not configured |
| dc1-leaf6 | MLAG | VerifyMlagConfigSanity | Verifies there are no MLAG config-sanity inconsistencies. | ⏭️&nbsp;Skipped | MLAG is disabled |
| dc1-leaf6 | MLAG | VerifyMlagInterfaces | Verifies there are no inactive or active-partial MLAG ports. | ⏭️&nbsp;Skipped | MLAG is disabled |
| dc1-leaf6 | MLAG | VerifyMlagStatus | Verifies the health status of the MLAG configuration. | ⏭️&nbsp;Skipped | MLAG is disabled |
| dc1-leaf6 | VXLAN | VerifyVxlanConfigSanity | Verifies there are no VXLAN config-sanity inconsistencies. | ⏭️&nbsp;Skipped | VXLAN is not configured |
| dc1-borderleaf1 | BGP | VerifyBGPPeerSession | Verifies the session state of BGP peers. | ✅&nbsp;Success | - |
| dc1-borderleaf1 | Configuration | VerifyRunningConfigDiffs | Verifies there is no difference between the running-config and the startup-config. | ✅&nbsp;Success | - |
| dc1-borderleaf1 | Configuration | VerifyZeroTouch | Verifies ZeroTouch is disabled. | ✅&nbsp;Success | - |
| dc1-borderleaf1 | Connectivity | VerifyLLDPNeighbors | Verifies the connection status of the specified LLDP (Link Layer Discovery Protocol) neighbors. | ✅&nbsp;Success | - |
| dc1-borderleaf1 | Connectivity | VerifyReachability | Verifies point-to-point reachability between Ethernet interfaces. | ✅&nbsp;Success | - |
| dc1-borderleaf1 | Interfaces | VerifyIllegalLACP | Verifies there are no illegal LACP packets in port channels. | ✅&nbsp;Success | - |
| dc1-borderleaf1 | Interfaces | VerifyInterfaceDiscards | Verifies that the interfaces packet discard counters are equal to zero. | ✅&nbsp;Success | - |
| dc1-borderleaf1 | Interfaces | VerifyInterfaceErrDisabled | Verifies there are no interfaces in the errdisabled state. | ✅&nbsp;Success | - |
| dc1-borderleaf1 | Interfaces | VerifyInterfaceErrors | Verifies that the interfaces error counters are equal to zero. | ✅&nbsp;Success | - |
| dc1-borderleaf1 | Interfaces | VerifyInterfaceUtilization | Verifies that the utilization of interfaces is below a certain threshold. | ✅&nbsp;Success | - |
| dc1-borderleaf1 | Interfaces | VerifyInterfacesStatus | Verifies the operational states of specified interfaces to ensure they match expected configurations. | ✅&nbsp;Success | - |
| dc1-borderleaf1 | Interfaces | VerifyPortChannels | Verifies there are no inactive ports in port channels. | ✅&nbsp;Success | - |
| dc1-borderleaf1 | MLAG | VerifyMlagConfigSanity | Verifies there are no MLAG config-sanity inconsistencies. | ✅&nbsp;Success | - |
| dc1-borderleaf1 | MLAG | VerifyMlagInterfaces | Verifies there are no inactive or active-partial MLAG ports. | ✅&nbsp;Success | - |
| dc1-borderleaf1 | MLAG | VerifyMlagStatus | Verifies the health status of the MLAG configuration. | ✅&nbsp;Success | - |
| dc1-borderleaf1 | Routing | VerifyRoutingProtocolModel | Verifies the configured routing protocol model. | ✅&nbsp;Success | - |
| dc1-borderleaf1 | STP | VerifySTPCounters | Verifies there is no errors in STP BPDU packets. | ✅&nbsp;Success | - |
| dc1-borderleaf1 | System | VerifyAgentLogs | Verifies there are no agent crash reports. | ✅&nbsp;Success | - |
| dc1-borderleaf1 | System | VerifyCoredump | Verifies there are no core dump files. | ✅&nbsp;Success | - |
| dc1-borderleaf1 | System | VerifyFileSystemUtilization | Verifies that no partition is utilizing more than 75% of its disk space. | ✅&nbsp;Success | - |
| dc1-borderleaf1 | System | VerifyMaintenance | Verifies that the device is not currently under or entering maintenance. | ✅&nbsp;Success | - |
| dc1-borderleaf1 | System | VerifyMemoryUtilization | Verifies whether the memory utilization is below 75%. | ✅&nbsp;Success | - |
| dc1-borderleaf1 | System | VerifyReloadCause | Verifies the last reload cause of the device. | ✅&nbsp;Success | - |
| dc1-borderleaf1 | VXLAN | VerifyVxlanConfigSanity | Verifies there are no VXLAN config-sanity inconsistencies. | ✅&nbsp;Success | - |
| dc1-borderleaf2 | BGP | VerifyBGPPeerSession | Verifies the session state of BGP peers. | ✅&nbsp;Success | - |
| dc1-borderleaf2 | Configuration | VerifyRunningConfigDiffs | Verifies there is no difference between the running-config and the startup-config. | ✅&nbsp;Success | - |
| dc1-borderleaf2 | Configuration | VerifyZeroTouch | Verifies ZeroTouch is disabled. | ✅&nbsp;Success | - |
| dc1-borderleaf2 | Connectivity | VerifyLLDPNeighbors | Verifies the connection status of the specified LLDP (Link Layer Discovery Protocol) neighbors. | ✅&nbsp;Success | - |
| dc1-borderleaf2 | Connectivity | VerifyReachability | Verifies point-to-point reachability between Ethernet interfaces. | ✅&nbsp;Success | - |
| dc1-borderleaf2 | Interfaces | VerifyIllegalLACP | Verifies there are no illegal LACP packets in port channels. | ✅&nbsp;Success | - |
| dc1-borderleaf2 | Interfaces | VerifyInterfaceDiscards | Verifies that the interfaces packet discard counters are equal to zero. | ✅&nbsp;Success | - |
| dc1-borderleaf2 | Interfaces | VerifyInterfaceErrDisabled | Verifies there are no interfaces in the errdisabled state. | ✅&nbsp;Success | - |
| dc1-borderleaf2 | Interfaces | VerifyInterfaceErrors | Verifies that the interfaces error counters are equal to zero. | ✅&nbsp;Success | - |
| dc1-borderleaf2 | Interfaces | VerifyInterfaceUtilization | Verifies that the utilization of interfaces is below a certain threshold. | ✅&nbsp;Success | - |
| dc1-borderleaf2 | Interfaces | VerifyInterfacesStatus | Verifies the operational states of specified interfaces to ensure they match expected configurations. | ✅&nbsp;Success | - |
| dc1-borderleaf2 | Interfaces | VerifyPortChannels | Verifies there are no inactive ports in port channels. | ✅&nbsp;Success | - |
| dc1-borderleaf2 | MLAG | VerifyMlagConfigSanity | Verifies there are no MLAG config-sanity inconsistencies. | ✅&nbsp;Success | - |
| dc1-borderleaf2 | MLAG | VerifyMlagInterfaces | Verifies there are no inactive or active-partial MLAG ports. | ✅&nbsp;Success | - |
| dc1-borderleaf2 | MLAG | VerifyMlagStatus | Verifies the health status of the MLAG configuration. | ✅&nbsp;Success | - |
| dc1-borderleaf2 | Routing | VerifyRoutingProtocolModel | Verifies the configured routing protocol model. | ✅&nbsp;Success | - |
| dc1-borderleaf2 | STP | VerifySTPCounters | Verifies there is no errors in STP BPDU packets. | ✅&nbsp;Success | - |
| dc1-borderleaf2 | System | VerifyAgentLogs | Verifies there are no agent crash reports. | ✅&nbsp;Success | - |
| dc1-borderleaf2 | System | VerifyCoredump | Verifies there are no core dump files. | ✅&nbsp;Success | - |
| dc1-borderleaf2 | System | VerifyFileSystemUtilization | Verifies that no partition is utilizing more than 75% of its disk space. | ✅&nbsp;Success | - |
| dc1-borderleaf2 | System | VerifyMaintenance | Verifies that the device is not currently under or entering maintenance. | ✅&nbsp;Success | - |
| dc1-borderleaf2 | System | VerifyMemoryUtilization | Verifies whether the memory utilization is below 75%. | ✅&nbsp;Success | - |
| dc1-borderleaf2 | System | VerifyReloadCause | Verifies the last reload cause of the device. | ✅&nbsp;Success | - |
| dc1-borderleaf2 | VXLAN | VerifyVxlanConfigSanity | Verifies there are no VXLAN config-sanity inconsistencies. | ✅&nbsp;Success | - |
| dc1-leaf1 | BGP | VerifyBGPPeerSession | Verifies the session state of BGP peers. | ✅&nbsp;Success | - |
| dc1-leaf1 | Configuration | VerifyRunningConfigDiffs | Verifies there is no difference between the running-config and the startup-config. | ✅&nbsp;Success | - |
| dc1-leaf1 | Configuration | VerifyZeroTouch | Verifies ZeroTouch is disabled. | ✅&nbsp;Success | - |
| dc1-leaf1 | Connectivity | VerifyLLDPNeighbors | Verifies the connection status of the specified LLDP (Link Layer Discovery Protocol) neighbors. | ✅&nbsp;Success | - |
| dc1-leaf1 | Connectivity | VerifyReachability | Verifies point-to-point reachability between Ethernet interfaces. | ✅&nbsp;Success | - |
| dc1-leaf1 | Interfaces | VerifyIllegalLACP | Verifies there are no illegal LACP packets in port channels. | ✅&nbsp;Success | - |
| dc1-leaf1 | Interfaces | VerifyInterfaceDiscards | Verifies that the interfaces packet discard counters are equal to zero. | ✅&nbsp;Success | - |
| dc1-leaf1 | Interfaces | VerifyInterfaceErrDisabled | Verifies there are no interfaces in the errdisabled state. | ✅&nbsp;Success | - |
| dc1-leaf1 | Interfaces | VerifyInterfaceErrors | Verifies that the interfaces error counters are equal to zero. | ✅&nbsp;Success | - |
| dc1-leaf1 | Interfaces | VerifyInterfaceUtilization | Verifies that the utilization of interfaces is below a certain threshold. | ✅&nbsp;Success | - |
| dc1-leaf1 | MLAG | VerifyMlagConfigSanity | Verifies there are no MLAG config-sanity inconsistencies. | ✅&nbsp;Success | - |
| dc1-leaf1 | MLAG | VerifyMlagStatus | Verifies the health status of the MLAG configuration. | ✅&nbsp;Success | - |
| dc1-leaf1 | Routing | VerifyRoutingProtocolModel | Verifies the configured routing protocol model. | ✅&nbsp;Success | - |
| dc1-leaf1 | STP | VerifySTPCounters | Verifies there is no errors in STP BPDU packets. | ✅&nbsp;Success | - |
| dc1-leaf1 | System | VerifyAgentLogs | Verifies there are no agent crash reports. | ✅&nbsp;Success | - |
| dc1-leaf1 | System | VerifyCoredump | Verifies there are no core dump files. | ✅&nbsp;Success | - |
| dc1-leaf1 | System | VerifyFileSystemUtilization | Verifies that no partition is utilizing more than 75% of its disk space. | ✅&nbsp;Success | - |
| dc1-leaf1 | System | VerifyMaintenance | Verifies that the device is not currently under or entering maintenance. | ✅&nbsp;Success | - |
| dc1-leaf1 | System | VerifyMemoryUtilization | Verifies whether the memory utilization is below 75%. | ✅&nbsp;Success | - |
| dc1-leaf1 | System | VerifyReloadCause | Verifies the last reload cause of the device. | ✅&nbsp;Success | - |
| dc1-leaf1 | VXLAN | VerifyVxlanConfigSanity | Verifies there are no VXLAN config-sanity inconsistencies. | ✅&nbsp;Success | - |
| dc1-leaf2 | BGP | VerifyBGPPeerSession | Verifies the session state of BGP peers. | ✅&nbsp;Success | - |
| dc1-leaf2 | Configuration | VerifyRunningConfigDiffs | Verifies there is no difference between the running-config and the startup-config. | ✅&nbsp;Success | - |
| dc1-leaf2 | Configuration | VerifyZeroTouch | Verifies ZeroTouch is disabled. | ✅&nbsp;Success | - |
| dc1-leaf2 | Connectivity | VerifyLLDPNeighbors | Verifies the connection status of the specified LLDP (Link Layer Discovery Protocol) neighbors. | ✅&nbsp;Success | - |
| dc1-leaf2 | Connectivity | VerifyReachability | Verifies point-to-point reachability between Ethernet interfaces. | ✅&nbsp;Success | - |
| dc1-leaf2 | Interfaces | VerifyIllegalLACP | Verifies there are no illegal LACP packets in port channels. | ✅&nbsp;Success | - |
| dc1-leaf2 | Interfaces | VerifyInterfaceDiscards | Verifies that the interfaces packet discard counters are equal to zero. | ✅&nbsp;Success | - |
| dc1-leaf2 | Interfaces | VerifyInterfaceErrDisabled | Verifies there are no interfaces in the errdisabled state. | ✅&nbsp;Success | - |
| dc1-leaf2 | Interfaces | VerifyInterfaceErrors | Verifies that the interfaces error counters are equal to zero. | ✅&nbsp;Success | - |
| dc1-leaf2 | Interfaces | VerifyInterfaceUtilization | Verifies that the utilization of interfaces is below a certain threshold. | ✅&nbsp;Success | - |
| dc1-leaf2 | MLAG | VerifyMlagConfigSanity | Verifies there are no MLAG config-sanity inconsistencies. | ✅&nbsp;Success | - |
| dc1-leaf2 | MLAG | VerifyMlagStatus | Verifies the health status of the MLAG configuration. | ✅&nbsp;Success | - |
| dc1-leaf2 | Routing | VerifyRoutingProtocolModel | Verifies the configured routing protocol model. | ✅&nbsp;Success | - |
| dc1-leaf2 | STP | VerifySTPCounters | Verifies there is no errors in STP BPDU packets. | ✅&nbsp;Success | - |
| dc1-leaf2 | System | VerifyAgentLogs | Verifies there are no agent crash reports. | ✅&nbsp;Success | - |
| dc1-leaf2 | System | VerifyCoredump | Verifies there are no core dump files. | ✅&nbsp;Success | - |
| dc1-leaf2 | System | VerifyFileSystemUtilization | Verifies that no partition is utilizing more than 75% of its disk space. | ✅&nbsp;Success | - |
| dc1-leaf2 | System | VerifyMaintenance | Verifies that the device is not currently under or entering maintenance. | ✅&nbsp;Success | - |
| dc1-leaf2 | System | VerifyMemoryUtilization | Verifies whether the memory utilization is below 75%. | ✅&nbsp;Success | - |
| dc1-leaf2 | System | VerifyReloadCause | Verifies the last reload cause of the device. | ✅&nbsp;Success | - |
| dc1-leaf2 | VXLAN | VerifyVxlanConfigSanity | Verifies there are no VXLAN config-sanity inconsistencies. | ✅&nbsp;Success | - |
| dc1-leaf3 | BGP | VerifyBGPPeerSession | Verifies the session state of BGP peers. | ✅&nbsp;Success | - |
| dc1-leaf3 | Configuration | VerifyRunningConfigDiffs | Verifies there is no difference between the running-config and the startup-config. | ✅&nbsp;Success | - |
| dc1-leaf3 | Configuration | VerifyZeroTouch | Verifies ZeroTouch is disabled. | ✅&nbsp;Success | - |
| dc1-leaf3 | Connectivity | VerifyLLDPNeighbors | Verifies the connection status of the specified LLDP (Link Layer Discovery Protocol) neighbors. | ✅&nbsp;Success | - |
| dc1-leaf3 | Connectivity | VerifyReachability | Verifies point-to-point reachability between Ethernet interfaces. | ✅&nbsp;Success | - |
| dc1-leaf3 | Interfaces | VerifyIllegalLACP | Verifies there are no illegal LACP packets in port channels. | ✅&nbsp;Success | - |
| dc1-leaf3 | Interfaces | VerifyInterfaceDiscards | Verifies that the interfaces packet discard counters are equal to zero. | ✅&nbsp;Success | - |
| dc1-leaf3 | Interfaces | VerifyInterfaceErrDisabled | Verifies there are no interfaces in the errdisabled state. | ✅&nbsp;Success | - |
| dc1-leaf3 | Interfaces | VerifyInterfaceErrors | Verifies that the interfaces error counters are equal to zero. | ✅&nbsp;Success | - |
| dc1-leaf3 | Interfaces | VerifyInterfaceUtilization | Verifies that the utilization of interfaces is below a certain threshold. | ✅&nbsp;Success | - |
| dc1-leaf3 | MLAG | VerifyMlagConfigSanity | Verifies there are no MLAG config-sanity inconsistencies. | ✅&nbsp;Success | - |
| dc1-leaf3 | MLAG | VerifyMlagStatus | Verifies the health status of the MLAG configuration. | ✅&nbsp;Success | - |
| dc1-leaf3 | Routing | VerifyRoutingProtocolModel | Verifies the configured routing protocol model. | ✅&nbsp;Success | - |
| dc1-leaf3 | STP | VerifySTPCounters | Verifies there is no errors in STP BPDU packets. | ✅&nbsp;Success | - |
| dc1-leaf3 | System | VerifyAgentLogs | Verifies there are no agent crash reports. | ✅&nbsp;Success | - |
| dc1-leaf3 | System | VerifyCoredump | Verifies there are no core dump files. | ✅&nbsp;Success | - |
| dc1-leaf3 | System | VerifyFileSystemUtilization | Verifies that no partition is utilizing more than 75% of its disk space. | ✅&nbsp;Success | - |
| dc1-leaf3 | System | VerifyMaintenance | Verifies that the device is not currently under or entering maintenance. | ✅&nbsp;Success | - |
| dc1-leaf3 | System | VerifyMemoryUtilization | Verifies whether the memory utilization is below 75%. | ✅&nbsp;Success | - |
| dc1-leaf3 | System | VerifyReloadCause | Verifies the last reload cause of the device. | ✅&nbsp;Success | - |
| dc1-leaf3 | VXLAN | VerifyVxlanConfigSanity | Verifies there are no VXLAN config-sanity inconsistencies. | ✅&nbsp;Success | - |
| dc1-leaf4 | BGP | VerifyBGPPeerSession | Verifies the session state of BGP peers. | ✅&nbsp;Success | - |
| dc1-leaf4 | Configuration | VerifyRunningConfigDiffs | Verifies there is no difference between the running-config and the startup-config. | ✅&nbsp;Success | - |
| dc1-leaf4 | Configuration | VerifyZeroTouch | Verifies ZeroTouch is disabled. | ✅&nbsp;Success | - |
| dc1-leaf4 | Connectivity | VerifyLLDPNeighbors | Verifies the connection status of the specified LLDP (Link Layer Discovery Protocol) neighbors. | ✅&nbsp;Success | - |
| dc1-leaf4 | Connectivity | VerifyReachability | Verifies point-to-point reachability between Ethernet interfaces. | ✅&nbsp;Success | - |
| dc1-leaf4 | Interfaces | VerifyIllegalLACP | Verifies there are no illegal LACP packets in port channels. | ✅&nbsp;Success | - |
| dc1-leaf4 | Interfaces | VerifyInterfaceDiscards | Verifies that the interfaces packet discard counters are equal to zero. | ✅&nbsp;Success | - |
| dc1-leaf4 | Interfaces | VerifyInterfaceErrDisabled | Verifies there are no interfaces in the errdisabled state. | ✅&nbsp;Success | - |
| dc1-leaf4 | Interfaces | VerifyInterfaceErrors | Verifies that the interfaces error counters are equal to zero. | ✅&nbsp;Success | - |
| dc1-leaf4 | Interfaces | VerifyInterfaceUtilization | Verifies that the utilization of interfaces is below a certain threshold. | ✅&nbsp;Success | - |
| dc1-leaf4 | MLAG | VerifyMlagConfigSanity | Verifies there are no MLAG config-sanity inconsistencies. | ✅&nbsp;Success | - |
| dc1-leaf4 | MLAG | VerifyMlagStatus | Verifies the health status of the MLAG configuration. | ✅&nbsp;Success | - |
| dc1-leaf4 | Routing | VerifyRoutingProtocolModel | Verifies the configured routing protocol model. | ✅&nbsp;Success | - |
| dc1-leaf4 | STP | VerifySTPCounters | Verifies there is no errors in STP BPDU packets. | ✅&nbsp;Success | - |
| dc1-leaf4 | System | VerifyAgentLogs | Verifies there are no agent crash reports. | ✅&nbsp;Success | - |
| dc1-leaf4 | System | VerifyCoredump | Verifies there are no core dump files. | ✅&nbsp;Success | - |
| dc1-leaf4 | System | VerifyFileSystemUtilization | Verifies that no partition is utilizing more than 75% of its disk space. | ✅&nbsp;Success | - |
| dc1-leaf4 | System | VerifyMaintenance | Verifies that the device is not currently under or entering maintenance. | ✅&nbsp;Success | - |
| dc1-leaf4 | System | VerifyMemoryUtilization | Verifies whether the memory utilization is below 75%. | ✅&nbsp;Success | - |
| dc1-leaf4 | System | VerifyReloadCause | Verifies the last reload cause of the device. | ✅&nbsp;Success | - |
| dc1-leaf4 | VXLAN | VerifyVxlanConfigSanity | Verifies there are no VXLAN config-sanity inconsistencies. | ✅&nbsp;Success | - |
| dc1-leaf5 | Configuration | VerifyRunningConfigDiffs | Verifies there is no difference between the running-config and the startup-config. | ✅&nbsp;Success | - |
| dc1-leaf5 | Configuration | VerifyZeroTouch | Verifies ZeroTouch is disabled. | ✅&nbsp;Success | - |
| dc1-leaf5 | Connectivity | VerifyLLDPNeighbors | Verifies the connection status of the specified LLDP (Link Layer Discovery Protocol) neighbors. | ✅&nbsp;Success | - |
| dc1-leaf5 | Interfaces | VerifyIllegalLACP | Verifies there are no illegal LACP packets in port channels. | ✅&nbsp;Success | - |
| dc1-leaf5 | Interfaces | VerifyInterfaceDiscards | Verifies that the interfaces packet discard counters are equal to zero. | ✅&nbsp;Success | - |
| dc1-leaf5 | Interfaces | VerifyInterfaceErrDisabled | Verifies there are no interfaces in the errdisabled state. | ✅&nbsp;Success | - |
| dc1-leaf5 | Interfaces | VerifyInterfaceErrors | Verifies that the interfaces error counters are equal to zero. | ✅&nbsp;Success | - |
| dc1-leaf5 | Interfaces | VerifyInterfaceUtilization | Verifies that the utilization of interfaces is below a certain threshold. | ✅&nbsp;Success | - |
| dc1-leaf5 | Routing | VerifyRoutingProtocolModel | Verifies the configured routing protocol model. | ✅&nbsp;Success | - |
| dc1-leaf5 | STP | VerifySTPCounters | Verifies there is no errors in STP BPDU packets. | ✅&nbsp;Success | - |
| dc1-leaf5 | System | VerifyAgentLogs | Verifies there are no agent crash reports. | ✅&nbsp;Success | - |
| dc1-leaf5 | System | VerifyCoredump | Verifies there are no core dump files. | ✅&nbsp;Success | - |
| dc1-leaf5 | System | VerifyFileSystemUtilization | Verifies that no partition is utilizing more than 75% of its disk space. | ✅&nbsp;Success | - |
| dc1-leaf5 | System | VerifyMaintenance | Verifies that the device is not currently under or entering maintenance. | ✅&nbsp;Success | - |
| dc1-leaf5 | System | VerifyMemoryUtilization | Verifies whether the memory utilization is below 75%. | ✅&nbsp;Success | - |
| dc1-leaf5 | System | VerifyReloadCause | Verifies the last reload cause of the device. | ✅&nbsp;Success | - |
| dc1-leaf6 | Configuration | VerifyRunningConfigDiffs | Verifies there is no difference between the running-config and the startup-config. | ✅&nbsp;Success | - |
| dc1-leaf6 | Configuration | VerifyZeroTouch | Verifies ZeroTouch is disabled. | ✅&nbsp;Success | - |
| dc1-leaf6 | Connectivity | VerifyLLDPNeighbors | Verifies the connection status of the specified LLDP (Link Layer Discovery Protocol) neighbors. | ✅&nbsp;Success | - |
| dc1-leaf6 | Interfaces | VerifyIllegalLACP | Verifies there are no illegal LACP packets in port channels. | ✅&nbsp;Success | - |
| dc1-leaf6 | Interfaces | VerifyInterfaceDiscards | Verifies that the interfaces packet discard counters are equal to zero. | ✅&nbsp;Success | - |
| dc1-leaf6 | Interfaces | VerifyInterfaceErrDisabled | Verifies there are no interfaces in the errdisabled state. | ✅&nbsp;Success | - |
| dc1-leaf6 | Interfaces | VerifyInterfaceErrors | Verifies that the interfaces error counters are equal to zero. | ✅&nbsp;Success | - |
| dc1-leaf6 | Interfaces | VerifyInterfaceUtilization | Verifies that the utilization of interfaces is below a certain threshold. | ✅&nbsp;Success | - |
| dc1-leaf6 | Routing | VerifyRoutingProtocolModel | Verifies the configured routing protocol model. | ✅&nbsp;Success | - |
| dc1-leaf6 | STP | VerifySTPCounters | Verifies there is no errors in STP BPDU packets. | ✅&nbsp;Success | - |
| dc1-leaf6 | System | VerifyAgentLogs | Verifies there are no agent crash reports. | ✅&nbsp;Success | - |
| dc1-leaf6 | System | VerifyCoredump | Verifies there are no core dump files. | ✅&nbsp;Success | - |
| dc1-leaf6 | System | VerifyFileSystemUtilization | Verifies that no partition is utilizing more than 75% of its disk space. | ✅&nbsp;Success | - |
| dc1-leaf6 | System | VerifyMaintenance | Verifies that the device is not currently under or entering maintenance. | ✅&nbsp;Success | - |
| dc1-leaf6 | System | VerifyMemoryUtilization | Verifies whether the memory utilization is below 75%. | ✅&nbsp;Success | - |
| dc1-leaf6 | System | VerifyReloadCause | Verifies the last reload cause of the device. | ✅&nbsp;Success | - |
| dc1-spine1 | Configuration | VerifyRunningConfigDiffs | Verifies there is no difference between the running-config and the startup-config. | ✅&nbsp;Success | - |
| dc1-spine1 | Configuration | VerifyZeroTouch | Verifies ZeroTouch is disabled. | ✅&nbsp;Success | - |
| dc1-spine1 | Connectivity | VerifyLLDPNeighbors | Verifies the connection status of the specified LLDP (Link Layer Discovery Protocol) neighbors. | ✅&nbsp;Success | - |
| dc1-spine1 | Interfaces | VerifyInterfaceDiscards | Verifies that the interfaces packet discard counters are equal to zero. | ✅&nbsp;Success | - |
| dc1-spine1 | Interfaces | VerifyInterfaceErrDisabled | Verifies there are no interfaces in the errdisabled state. | ✅&nbsp;Success | - |
| dc1-spine1 | Interfaces | VerifyInterfaceErrors | Verifies that the interfaces error counters are equal to zero. | ✅&nbsp;Success | - |
| dc1-spine1 | Interfaces | VerifyInterfaceUtilization | Verifies that the utilization of interfaces is below a certain threshold. | ✅&nbsp;Success | - |
| dc1-spine1 | Interfaces | VerifyInterfacesStatus | Verifies the operational states of specified interfaces to ensure they match expected configurations. | ✅&nbsp;Success | - |
| dc1-spine1 | Routing | VerifyRoutingProtocolModel | Verifies the configured routing protocol model. | ✅&nbsp;Success | - |
| dc1-spine1 | STP | VerifySTPCounters | Verifies there is no errors in STP BPDU packets. | ✅&nbsp;Success | - |
| dc1-spine1 | System | VerifyAgentLogs | Verifies there are no agent crash reports. | ✅&nbsp;Success | - |
| dc1-spine1 | System | VerifyCoredump | Verifies there are no core dump files. | ✅&nbsp;Success | - |
| dc1-spine1 | System | VerifyFileSystemUtilization | Verifies that no partition is utilizing more than 75% of its disk space. | ✅&nbsp;Success | - |
| dc1-spine1 | System | VerifyMaintenance | Verifies that the device is not currently under or entering maintenance. | ✅&nbsp;Success | - |
| dc1-spine1 | System | VerifyMemoryUtilization | Verifies whether the memory utilization is below 75%. | ✅&nbsp;Success | - |
| dc1-spine1 | System | VerifyReloadCause | Verifies the last reload cause of the device. | ✅&nbsp;Success | - |
| dc1-spine2 | Configuration | VerifyRunningConfigDiffs | Verifies there is no difference between the running-config and the startup-config. | ✅&nbsp;Success | - |
| dc1-spine2 | Configuration | VerifyZeroTouch | Verifies ZeroTouch is disabled. | ✅&nbsp;Success | - |
| dc1-spine2 | Connectivity | VerifyLLDPNeighbors | Verifies the connection status of the specified LLDP (Link Layer Discovery Protocol) neighbors. | ✅&nbsp;Success | - |
| dc1-spine2 | Interfaces | VerifyInterfaceDiscards | Verifies that the interfaces packet discard counters are equal to zero. | ✅&nbsp;Success | - |
| dc1-spine2 | Interfaces | VerifyInterfaceErrDisabled | Verifies there are no interfaces in the errdisabled state. | ✅&nbsp;Success | - |
| dc1-spine2 | Interfaces | VerifyInterfaceErrors | Verifies that the interfaces error counters are equal to zero. | ✅&nbsp;Success | - |
| dc1-spine2 | Interfaces | VerifyInterfaceUtilization | Verifies that the utilization of interfaces is below a certain threshold. | ✅&nbsp;Success | - |
| dc1-spine2 | Interfaces | VerifyInterfacesStatus | Verifies the operational states of specified interfaces to ensure they match expected configurations. | ✅&nbsp;Success | - |
| dc1-spine2 | Routing | VerifyRoutingProtocolModel | Verifies the configured routing protocol model. | ✅&nbsp;Success | - |
| dc1-spine2 | STP | VerifySTPCounters | Verifies there is no errors in STP BPDU packets. | ✅&nbsp;Success | - |
| dc1-spine2 | System | VerifyAgentLogs | Verifies there are no agent crash reports. | ✅&nbsp;Success | - |
| dc1-spine2 | System | VerifyCoredump | Verifies there are no core dump files. | ✅&nbsp;Success | - |
| dc1-spine2 | System | VerifyFileSystemUtilization | Verifies that no partition is utilizing more than 75% of its disk space. | ✅&nbsp;Success | - |
| dc1-spine2 | System | VerifyMaintenance | Verifies that the device is not currently under or entering maintenance. | ✅&nbsp;Success | - |
| dc1-spine2 | System | VerifyMemoryUtilization | Verifies whether the memory utilization is below 75%. | ✅&nbsp;Success | - |
| dc1-spine2 | System | VerifyReloadCause | Verifies the last reload cause of the device. | ✅&nbsp;Success | - |
| dc2-borderleaf1 | BGP | VerifyBGPPeerSession | Verifies the session state of BGP peers. | ✅&nbsp;Success | - |
| dc2-borderleaf1 | Configuration | VerifyRunningConfigDiffs | Verifies there is no difference between the running-config and the startup-config. | ✅&nbsp;Success | - |
| dc2-borderleaf1 | Configuration | VerifyZeroTouch | Verifies ZeroTouch is disabled. | ✅&nbsp;Success | - |
| dc2-borderleaf1 | Connectivity | VerifyLLDPNeighbors | Verifies the connection status of the specified LLDP (Link Layer Discovery Protocol) neighbors. | ✅&nbsp;Success | - |
| dc2-borderleaf1 | Connectivity | VerifyReachability | Verifies point-to-point reachability between Ethernet interfaces. | ✅&nbsp;Success | - |
| dc2-borderleaf1 | Interfaces | VerifyIllegalLACP | Verifies there are no illegal LACP packets in port channels. | ✅&nbsp;Success | - |
| dc2-borderleaf1 | Interfaces | VerifyInterfaceDiscards | Verifies that the interfaces packet discard counters are equal to zero. | ✅&nbsp;Success | - |
| dc2-borderleaf1 | Interfaces | VerifyInterfaceErrDisabled | Verifies there are no interfaces in the errdisabled state. | ✅&nbsp;Success | - |
| dc2-borderleaf1 | Interfaces | VerifyInterfaceErrors | Verifies that the interfaces error counters are equal to zero. | ✅&nbsp;Success | - |
| dc2-borderleaf1 | Interfaces | VerifyInterfaceUtilization | Verifies that the utilization of interfaces is below a certain threshold. | ✅&nbsp;Success | - |
| dc2-borderleaf1 | Interfaces | VerifyInterfacesStatus | Verifies the operational states of specified interfaces to ensure they match expected configurations. | ✅&nbsp;Success | - |
| dc2-borderleaf1 | Interfaces | VerifyPortChannels | Verifies there are no inactive ports in port channels. | ✅&nbsp;Success | - |
| dc2-borderleaf1 | MLAG | VerifyMlagConfigSanity | Verifies there are no MLAG config-sanity inconsistencies. | ✅&nbsp;Success | - |
| dc2-borderleaf1 | MLAG | VerifyMlagInterfaces | Verifies there are no inactive or active-partial MLAG ports. | ✅&nbsp;Success | - |
| dc2-borderleaf1 | MLAG | VerifyMlagStatus | Verifies the health status of the MLAG configuration. | ✅&nbsp;Success | - |
| dc2-borderleaf1 | Routing | VerifyRoutingProtocolModel | Verifies the configured routing protocol model. | ✅&nbsp;Success | - |
| dc2-borderleaf1 | STP | VerifySTPCounters | Verifies there is no errors in STP BPDU packets. | ✅&nbsp;Success | - |
| dc2-borderleaf1 | System | VerifyAgentLogs | Verifies there are no agent crash reports. | ✅&nbsp;Success | - |
| dc2-borderleaf1 | System | VerifyCoredump | Verifies there are no core dump files. | ✅&nbsp;Success | - |
| dc2-borderleaf1 | System | VerifyFileSystemUtilization | Verifies that no partition is utilizing more than 75% of its disk space. | ✅&nbsp;Success | - |
| dc2-borderleaf1 | System | VerifyMaintenance | Verifies that the device is not currently under or entering maintenance. | ✅&nbsp;Success | - |
| dc2-borderleaf1 | System | VerifyMemoryUtilization | Verifies whether the memory utilization is below 75%. | ✅&nbsp;Success | - |
| dc2-borderleaf1 | System | VerifyReloadCause | Verifies the last reload cause of the device. | ✅&nbsp;Success | - |
| dc2-borderleaf1 | VXLAN | VerifyVxlanConfigSanity | Verifies there are no VXLAN config-sanity inconsistencies. | ✅&nbsp;Success | - |
| dc2-borderleaf2 | BGP | VerifyBGPPeerSession | Verifies the session state of BGP peers. | ✅&nbsp;Success | - |
| dc2-borderleaf2 | Configuration | VerifyRunningConfigDiffs | Verifies there is no difference between the running-config and the startup-config. | ✅&nbsp;Success | - |
| dc2-borderleaf2 | Configuration | VerifyZeroTouch | Verifies ZeroTouch is disabled. | ✅&nbsp;Success | - |
| dc2-borderleaf2 | Connectivity | VerifyLLDPNeighbors | Verifies the connection status of the specified LLDP (Link Layer Discovery Protocol) neighbors. | ✅&nbsp;Success | - |
| dc2-borderleaf2 | Connectivity | VerifyReachability | Verifies point-to-point reachability between Ethernet interfaces. | ✅&nbsp;Success | - |
| dc2-borderleaf2 | Interfaces | VerifyIllegalLACP | Verifies there are no illegal LACP packets in port channels. | ✅&nbsp;Success | - |
| dc2-borderleaf2 | Interfaces | VerifyInterfaceDiscards | Verifies that the interfaces packet discard counters are equal to zero. | ✅&nbsp;Success | - |
| dc2-borderleaf2 | Interfaces | VerifyInterfaceErrDisabled | Verifies there are no interfaces in the errdisabled state. | ✅&nbsp;Success | - |
| dc2-borderleaf2 | Interfaces | VerifyInterfaceErrors | Verifies that the interfaces error counters are equal to zero. | ✅&nbsp;Success | - |
| dc2-borderleaf2 | Interfaces | VerifyInterfaceUtilization | Verifies that the utilization of interfaces is below a certain threshold. | ✅&nbsp;Success | - |
| dc2-borderleaf2 | Interfaces | VerifyInterfacesStatus | Verifies the operational states of specified interfaces to ensure they match expected configurations. | ✅&nbsp;Success | - |
| dc2-borderleaf2 | Interfaces | VerifyPortChannels | Verifies there are no inactive ports in port channels. | ✅&nbsp;Success | - |
| dc2-borderleaf2 | MLAG | VerifyMlagConfigSanity | Verifies there are no MLAG config-sanity inconsistencies. | ✅&nbsp;Success | - |
| dc2-borderleaf2 | MLAG | VerifyMlagInterfaces | Verifies there are no inactive or active-partial MLAG ports. | ✅&nbsp;Success | - |
| dc2-borderleaf2 | MLAG | VerifyMlagStatus | Verifies the health status of the MLAG configuration. | ✅&nbsp;Success | - |
| dc2-borderleaf2 | Routing | VerifyRoutingProtocolModel | Verifies the configured routing protocol model. | ✅&nbsp;Success | - |
| dc2-borderleaf2 | STP | VerifySTPCounters | Verifies there is no errors in STP BPDU packets. | ✅&nbsp;Success | - |
| dc2-borderleaf2 | System | VerifyAgentLogs | Verifies there are no agent crash reports. | ✅&nbsp;Success | - |
| dc2-borderleaf2 | System | VerifyCoredump | Verifies there are no core dump files. | ✅&nbsp;Success | - |
| dc2-borderleaf2 | System | VerifyFileSystemUtilization | Verifies that no partition is utilizing more than 75% of its disk space. | ✅&nbsp;Success | - |
| dc2-borderleaf2 | System | VerifyMaintenance | Verifies that the device is not currently under or entering maintenance. | ✅&nbsp;Success | - |
| dc2-borderleaf2 | System | VerifyMemoryUtilization | Verifies whether the memory utilization is below 75%. | ✅&nbsp;Success | - |
| dc2-borderleaf2 | System | VerifyReloadCause | Verifies the last reload cause of the device. | ✅&nbsp;Success | - |
| dc2-borderleaf2 | VXLAN | VerifyVxlanConfigSanity | Verifies there are no VXLAN config-sanity inconsistencies. | ✅&nbsp;Success | - |
| dc2-leaf1 | BGP | VerifyBGPPeerSession | Verifies the session state of BGP peers. | ✅&nbsp;Success | - |
| dc2-leaf1 | Configuration | VerifyRunningConfigDiffs | Verifies there is no difference between the running-config and the startup-config. | ✅&nbsp;Success | - |
| dc2-leaf1 | Configuration | VerifyZeroTouch | Verifies ZeroTouch is disabled. | ✅&nbsp;Success | - |
| dc2-leaf1 | Connectivity | VerifyLLDPNeighbors | Verifies the connection status of the specified LLDP (Link Layer Discovery Protocol) neighbors. | ✅&nbsp;Success | - |
| dc2-leaf1 | Connectivity | VerifyReachability | Verifies point-to-point reachability between Ethernet interfaces. | ✅&nbsp;Success | - |
| dc2-leaf1 | Interfaces | VerifyIllegalLACP | Verifies there are no illegal LACP packets in port channels. | ✅&nbsp;Success | - |
| dc2-leaf1 | Interfaces | VerifyInterfaceDiscards | Verifies that the interfaces packet discard counters are equal to zero. | ✅&nbsp;Success | - |
| dc2-leaf1 | Interfaces | VerifyInterfaceErrDisabled | Verifies there are no interfaces in the errdisabled state. | ✅&nbsp;Success | - |
| dc2-leaf1 | Interfaces | VerifyInterfaceErrors | Verifies that the interfaces error counters are equal to zero. | ✅&nbsp;Success | - |
| dc2-leaf1 | Interfaces | VerifyInterfaceUtilization | Verifies that the utilization of interfaces is below a certain threshold. | ✅&nbsp;Success | - |
| dc2-leaf1 | Interfaces | VerifyInterfacesStatus | Verifies the operational states of specified interfaces to ensure they match expected configurations. | ✅&nbsp;Success | - |
| dc2-leaf1 | Interfaces | VerifyPortChannels | Verifies there are no inactive ports in port channels. | ✅&nbsp;Success | - |
| dc2-leaf1 | MLAG | VerifyMlagConfigSanity | Verifies there are no MLAG config-sanity inconsistencies. | ✅&nbsp;Success | - |
| dc2-leaf1 | MLAG | VerifyMlagInterfaces | Verifies there are no inactive or active-partial MLAG ports. | ✅&nbsp;Success | - |
| dc2-leaf1 | MLAG | VerifyMlagStatus | Verifies the health status of the MLAG configuration. | ✅&nbsp;Success | - |
| dc2-leaf1 | Routing | VerifyRoutingProtocolModel | Verifies the configured routing protocol model. | ✅&nbsp;Success | - |
| dc2-leaf1 | STP | VerifySTPCounters | Verifies there is no errors in STP BPDU packets. | ✅&nbsp;Success | - |
| dc2-leaf1 | System | VerifyAgentLogs | Verifies there are no agent crash reports. | ✅&nbsp;Success | - |
| dc2-leaf1 | System | VerifyCoredump | Verifies there are no core dump files. | ✅&nbsp;Success | - |
| dc2-leaf1 | System | VerifyFileSystemUtilization | Verifies that no partition is utilizing more than 75% of its disk space. | ✅&nbsp;Success | - |
| dc2-leaf1 | System | VerifyMaintenance | Verifies that the device is not currently under or entering maintenance. | ✅&nbsp;Success | - |
| dc2-leaf1 | System | VerifyMemoryUtilization | Verifies whether the memory utilization is below 75%. | ✅&nbsp;Success | - |
| dc2-leaf1 | System | VerifyReloadCause | Verifies the last reload cause of the device. | ✅&nbsp;Success | - |
| dc2-leaf1 | VXLAN | VerifyVxlanConfigSanity | Verifies there are no VXLAN config-sanity inconsistencies. | ✅&nbsp;Success | - |
| dc2-leaf2 | BGP | VerifyBGPPeerSession | Verifies the session state of BGP peers. | ✅&nbsp;Success | - |
| dc2-leaf2 | Configuration | VerifyRunningConfigDiffs | Verifies there is no difference between the running-config and the startup-config. | ✅&nbsp;Success | - |
| dc2-leaf2 | Configuration | VerifyZeroTouch | Verifies ZeroTouch is disabled. | ✅&nbsp;Success | - |
| dc2-leaf2 | Connectivity | VerifyLLDPNeighbors | Verifies the connection status of the specified LLDP (Link Layer Discovery Protocol) neighbors. | ✅&nbsp;Success | - |
| dc2-leaf2 | Connectivity | VerifyReachability | Verifies point-to-point reachability between Ethernet interfaces. | ✅&nbsp;Success | - |
| dc2-leaf2 | Interfaces | VerifyIllegalLACP | Verifies there are no illegal LACP packets in port channels. | ✅&nbsp;Success | - |
| dc2-leaf2 | Interfaces | VerifyInterfaceDiscards | Verifies that the interfaces packet discard counters are equal to zero. | ✅&nbsp;Success | - |
| dc2-leaf2 | Interfaces | VerifyInterfaceErrDisabled | Verifies there are no interfaces in the errdisabled state. | ✅&nbsp;Success | - |
| dc2-leaf2 | Interfaces | VerifyInterfaceErrors | Verifies that the interfaces error counters are equal to zero. | ✅&nbsp;Success | - |
| dc2-leaf2 | Interfaces | VerifyInterfaceUtilization | Verifies that the utilization of interfaces is below a certain threshold. | ✅&nbsp;Success | - |
| dc2-leaf2 | Interfaces | VerifyInterfacesStatus | Verifies the operational states of specified interfaces to ensure they match expected configurations. | ✅&nbsp;Success | - |
| dc2-leaf2 | Interfaces | VerifyPortChannels | Verifies there are no inactive ports in port channels. | ✅&nbsp;Success | - |
| dc2-leaf2 | MLAG | VerifyMlagConfigSanity | Verifies there are no MLAG config-sanity inconsistencies. | ✅&nbsp;Success | - |
| dc2-leaf2 | MLAG | VerifyMlagInterfaces | Verifies there are no inactive or active-partial MLAG ports. | ✅&nbsp;Success | - |
| dc2-leaf2 | MLAG | VerifyMlagStatus | Verifies the health status of the MLAG configuration. | ✅&nbsp;Success | - |
| dc2-leaf2 | Routing | VerifyRoutingProtocolModel | Verifies the configured routing protocol model. | ✅&nbsp;Success | - |
| dc2-leaf2 | STP | VerifySTPCounters | Verifies there is no errors in STP BPDU packets. | ✅&nbsp;Success | - |
| dc2-leaf2 | System | VerifyAgentLogs | Verifies there are no agent crash reports. | ✅&nbsp;Success | - |
| dc2-leaf2 | System | VerifyCoredump | Verifies there are no core dump files. | ✅&nbsp;Success | - |
| dc2-leaf2 | System | VerifyFileSystemUtilization | Verifies that no partition is utilizing more than 75% of its disk space. | ✅&nbsp;Success | - |
| dc2-leaf2 | System | VerifyMaintenance | Verifies that the device is not currently under or entering maintenance. | ✅&nbsp;Success | - |
| dc2-leaf2 | System | VerifyMemoryUtilization | Verifies whether the memory utilization is below 75%. | ✅&nbsp;Success | - |
| dc2-leaf2 | System | VerifyReloadCause | Verifies the last reload cause of the device. | ✅&nbsp;Success | - |
| dc2-leaf2 | VXLAN | VerifyVxlanConfigSanity | Verifies there are no VXLAN config-sanity inconsistencies. | ✅&nbsp;Success | - |
| dc2-leaf3 | BGP | VerifyBGPPeerSession | Verifies the session state of BGP peers. | ✅&nbsp;Success | - |
| dc2-leaf3 | Configuration | VerifyRunningConfigDiffs | Verifies there is no difference between the running-config and the startup-config. | ✅&nbsp;Success | - |
| dc2-leaf3 | Configuration | VerifyZeroTouch | Verifies ZeroTouch is disabled. | ✅&nbsp;Success | - |
| dc2-leaf3 | Connectivity | VerifyLLDPNeighbors | Verifies the connection status of the specified LLDP (Link Layer Discovery Protocol) neighbors. | ✅&nbsp;Success | - |
| dc2-leaf3 | Connectivity | VerifyReachability | Verifies point-to-point reachability between Ethernet interfaces. | ✅&nbsp;Success | - |
| dc2-leaf3 | Interfaces | VerifyIllegalLACP | Verifies there are no illegal LACP packets in port channels. | ✅&nbsp;Success | - |
| dc2-leaf3 | Interfaces | VerifyInterfaceDiscards | Verifies that the interfaces packet discard counters are equal to zero. | ✅&nbsp;Success | - |
| dc2-leaf3 | Interfaces | VerifyInterfaceErrDisabled | Verifies there are no interfaces in the errdisabled state. | ✅&nbsp;Success | - |
| dc2-leaf3 | Interfaces | VerifyInterfaceErrors | Verifies that the interfaces error counters are equal to zero. | ✅&nbsp;Success | - |
| dc2-leaf3 | Interfaces | VerifyInterfaceUtilization | Verifies that the utilization of interfaces is below a certain threshold. | ✅&nbsp;Success | - |
| dc2-leaf3 | Interfaces | VerifyInterfacesStatus | Verifies the operational states of specified interfaces to ensure they match expected configurations. | ✅&nbsp;Success | - |
| dc2-leaf3 | Interfaces | VerifyPortChannels | Verifies there are no inactive ports in port channels. | ✅&nbsp;Success | - |
| dc2-leaf3 | MLAG | VerifyMlagConfigSanity | Verifies there are no MLAG config-sanity inconsistencies. | ✅&nbsp;Success | - |
| dc2-leaf3 | MLAG | VerifyMlagInterfaces | Verifies there are no inactive or active-partial MLAG ports. | ✅&nbsp;Success | - |
| dc2-leaf3 | MLAG | VerifyMlagStatus | Verifies the health status of the MLAG configuration. | ✅&nbsp;Success | - |
| dc2-leaf3 | Routing | VerifyRoutingProtocolModel | Verifies the configured routing protocol model. | ✅&nbsp;Success | - |
| dc2-leaf3 | STP | VerifySTPCounters | Verifies there is no errors in STP BPDU packets. | ✅&nbsp;Success | - |
| dc2-leaf3 | System | VerifyAgentLogs | Verifies there are no agent crash reports. | ✅&nbsp;Success | - |
| dc2-leaf3 | System | VerifyCoredump | Verifies there are no core dump files. | ✅&nbsp;Success | - |
| dc2-leaf3 | System | VerifyFileSystemUtilization | Verifies that no partition is utilizing more than 75% of its disk space. | ✅&nbsp;Success | - |
| dc2-leaf3 | System | VerifyMaintenance | Verifies that the device is not currently under or entering maintenance. | ✅&nbsp;Success | - |
| dc2-leaf3 | System | VerifyMemoryUtilization | Verifies whether the memory utilization is below 75%. | ✅&nbsp;Success | - |
| dc2-leaf3 | System | VerifyReloadCause | Verifies the last reload cause of the device. | ✅&nbsp;Success | - |
| dc2-leaf3 | VXLAN | VerifyVxlanConfigSanity | Verifies there are no VXLAN config-sanity inconsistencies. | ✅&nbsp;Success | - |
| dc2-leaf4 | BGP | VerifyBGPPeerSession | Verifies the session state of BGP peers. | ✅&nbsp;Success | - |
| dc2-leaf4 | Configuration | VerifyRunningConfigDiffs | Verifies there is no difference between the running-config and the startup-config. | ✅&nbsp;Success | - |
| dc2-leaf4 | Configuration | VerifyZeroTouch | Verifies ZeroTouch is disabled. | ✅&nbsp;Success | - |
| dc2-leaf4 | Connectivity | VerifyLLDPNeighbors | Verifies the connection status of the specified LLDP (Link Layer Discovery Protocol) neighbors. | ✅&nbsp;Success | - |
| dc2-leaf4 | Connectivity | VerifyReachability | Verifies point-to-point reachability between Ethernet interfaces. | ✅&nbsp;Success | - |
| dc2-leaf4 | Interfaces | VerifyIllegalLACP | Verifies there are no illegal LACP packets in port channels. | ✅&nbsp;Success | - |
| dc2-leaf4 | Interfaces | VerifyInterfaceDiscards | Verifies that the interfaces packet discard counters are equal to zero. | ✅&nbsp;Success | - |
| dc2-leaf4 | Interfaces | VerifyInterfaceErrDisabled | Verifies there are no interfaces in the errdisabled state. | ✅&nbsp;Success | - |
| dc2-leaf4 | Interfaces | VerifyInterfaceErrors | Verifies that the interfaces error counters are equal to zero. | ✅&nbsp;Success | - |
| dc2-leaf4 | Interfaces | VerifyInterfaceUtilization | Verifies that the utilization of interfaces is below a certain threshold. | ✅&nbsp;Success | - |
| dc2-leaf4 | Interfaces | VerifyInterfacesStatus | Verifies the operational states of specified interfaces to ensure they match expected configurations. | ✅&nbsp;Success | - |
| dc2-leaf4 | Interfaces | VerifyPortChannels | Verifies there are no inactive ports in port channels. | ✅&nbsp;Success | - |
| dc2-leaf4 | MLAG | VerifyMlagConfigSanity | Verifies there are no MLAG config-sanity inconsistencies. | ✅&nbsp;Success | - |
| dc2-leaf4 | MLAG | VerifyMlagInterfaces | Verifies there are no inactive or active-partial MLAG ports. | ✅&nbsp;Success | - |
| dc2-leaf4 | MLAG | VerifyMlagStatus | Verifies the health status of the MLAG configuration. | ✅&nbsp;Success | - |
| dc2-leaf4 | Routing | VerifyRoutingProtocolModel | Verifies the configured routing protocol model. | ✅&nbsp;Success | - |
| dc2-leaf4 | STP | VerifySTPCounters | Verifies there is no errors in STP BPDU packets. | ✅&nbsp;Success | - |
| dc2-leaf4 | System | VerifyAgentLogs | Verifies there are no agent crash reports. | ✅&nbsp;Success | - |
| dc2-leaf4 | System | VerifyCoredump | Verifies there are no core dump files. | ✅&nbsp;Success | - |
| dc2-leaf4 | System | VerifyFileSystemUtilization | Verifies that no partition is utilizing more than 75% of its disk space. | ✅&nbsp;Success | - |
| dc2-leaf4 | System | VerifyMaintenance | Verifies that the device is not currently under or entering maintenance. | ✅&nbsp;Success | - |
| dc2-leaf4 | System | VerifyMemoryUtilization | Verifies whether the memory utilization is below 75%. | ✅&nbsp;Success | - |
| dc2-leaf4 | System | VerifyReloadCause | Verifies the last reload cause of the device. | ✅&nbsp;Success | - |
| dc2-leaf4 | VXLAN | VerifyVxlanConfigSanity | Verifies there are no VXLAN config-sanity inconsistencies. | ✅&nbsp;Success | - |
| dc2-spine1 | BGP | VerifyBGPPeerSession | Verifies the session state of BGP peers. | ✅&nbsp;Success | - |
| dc2-spine1 | Configuration | VerifyRunningConfigDiffs | Verifies there is no difference between the running-config and the startup-config. | ✅&nbsp;Success | - |
| dc2-spine1 | Configuration | VerifyZeroTouch | Verifies ZeroTouch is disabled. | ✅&nbsp;Success | - |
| dc2-spine1 | Connectivity | VerifyLLDPNeighbors | Verifies the connection status of the specified LLDP (Link Layer Discovery Protocol) neighbors. | ✅&nbsp;Success | - |
| dc2-spine1 | Connectivity | VerifyReachability | Verifies point-to-point reachability between Ethernet interfaces. | ✅&nbsp;Success | - |
| dc2-spine1 | Interfaces | VerifyInterfaceDiscards | Verifies that the interfaces packet discard counters are equal to zero. | ✅&nbsp;Success | - |
| dc2-spine1 | Interfaces | VerifyInterfaceErrDisabled | Verifies there are no interfaces in the errdisabled state. | ✅&nbsp;Success | - |
| dc2-spine1 | Interfaces | VerifyInterfaceErrors | Verifies that the interfaces error counters are equal to zero. | ✅&nbsp;Success | - |
| dc2-spine1 | Interfaces | VerifyInterfaceUtilization | Verifies that the utilization of interfaces is below a certain threshold. | ✅&nbsp;Success | - |
| dc2-spine1 | Interfaces | VerifyInterfacesStatus | Verifies the operational states of specified interfaces to ensure they match expected configurations. | ✅&nbsp;Success | - |
| dc2-spine1 | Routing | VerifyRoutingProtocolModel | Verifies the configured routing protocol model. | ✅&nbsp;Success | - |
| dc2-spine1 | STP | VerifySTPCounters | Verifies there is no errors in STP BPDU packets. | ✅&nbsp;Success | - |
| dc2-spine1 | System | VerifyAgentLogs | Verifies there are no agent crash reports. | ✅&nbsp;Success | - |
| dc2-spine1 | System | VerifyCoredump | Verifies there are no core dump files. | ✅&nbsp;Success | - |
| dc2-spine1 | System | VerifyFileSystemUtilization | Verifies that no partition is utilizing more than 75% of its disk space. | ✅&nbsp;Success | - |
| dc2-spine1 | System | VerifyMaintenance | Verifies that the device is not currently under or entering maintenance. | ✅&nbsp;Success | - |
| dc2-spine1 | System | VerifyMemoryUtilization | Verifies whether the memory utilization is below 75%. | ✅&nbsp;Success | - |
| dc2-spine1 | System | VerifyReloadCause | Verifies the last reload cause of the device. | ✅&nbsp;Success | - |
| dc2-spine2 | BGP | VerifyBGPPeerSession | Verifies the session state of BGP peers. | ✅&nbsp;Success | - |
| dc2-spine2 | Configuration | VerifyRunningConfigDiffs | Verifies there is no difference between the running-config and the startup-config. | ✅&nbsp;Success | - |
| dc2-spine2 | Configuration | VerifyZeroTouch | Verifies ZeroTouch is disabled. | ✅&nbsp;Success | - |
| dc2-spine2 | Connectivity | VerifyLLDPNeighbors | Verifies the connection status of the specified LLDP (Link Layer Discovery Protocol) neighbors. | ✅&nbsp;Success | - |
| dc2-spine2 | Connectivity | VerifyReachability | Verifies point-to-point reachability between Ethernet interfaces. | ✅&nbsp;Success | - |
| dc2-spine2 | Interfaces | VerifyInterfaceDiscards | Verifies that the interfaces packet discard counters are equal to zero. | ✅&nbsp;Success | - |
| dc2-spine2 | Interfaces | VerifyInterfaceErrDisabled | Verifies there are no interfaces in the errdisabled state. | ✅&nbsp;Success | - |
| dc2-spine2 | Interfaces | VerifyInterfaceErrors | Verifies that the interfaces error counters are equal to zero. | ✅&nbsp;Success | - |
| dc2-spine2 | Interfaces | VerifyInterfaceUtilization | Verifies that the utilization of interfaces is below a certain threshold. | ✅&nbsp;Success | - |
| dc2-spine2 | Interfaces | VerifyInterfacesStatus | Verifies the operational states of specified interfaces to ensure they match expected configurations. | ✅&nbsp;Success | - |
| dc2-spine2 | Routing | VerifyRoutingProtocolModel | Verifies the configured routing protocol model. | ✅&nbsp;Success | - |
| dc2-spine2 | STP | VerifySTPCounters | Verifies there is no errors in STP BPDU packets. | ✅&nbsp;Success | - |
| dc2-spine2 | System | VerifyAgentLogs | Verifies there are no agent crash reports. | ✅&nbsp;Success | - |
| dc2-spine2 | System | VerifyCoredump | Verifies there are no core dump files. | ✅&nbsp;Success | - |
| dc2-spine2 | System | VerifyFileSystemUtilization | Verifies that no partition is utilizing more than 75% of its disk space. | ✅&nbsp;Success | - |
| dc2-spine2 | System | VerifyMaintenance | Verifies that the device is not currently under or entering maintenance. | ✅&nbsp;Success | - |
| dc2-spine2 | System | VerifyMemoryUtilization | Verifies whether the memory utilization is below 75%. | ✅&nbsp;Success | - |
| dc2-spine2 | System | VerifyReloadCause | Verifies the last reload cause of the device. | ✅&nbsp;Success | - |
| dc1-leaf5 | Interfaces | VerifyPortChannels | Verifies there are no inactive ports in port channels. | Unset | - |
| dc1-leaf6 | Interfaces | VerifyPortChannels | Verifies there are no inactive ports in port channels. | Unset | - |
