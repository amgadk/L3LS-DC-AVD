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
| 392 | 348 | 0 | 44 | 0 |

### 🔌 Summary Totals Device Under Test <a id="summary-totals-device-under-test"></a>

| Device | Total Tests | ✅&nbsp;Success | ⏭️&nbsp;Skipped | ❌&nbsp;Failure | ❗&nbsp;Error | Categories Skipped | Categories Failed |
| :- | :- | :- | :- | :- | :- | :- | :- |
| **dc1-borderleaf1** | 26 | 24 | 0 | 2 | 0 | - | Logging, System |
| **dc1-borderleaf2** | 26 | 24 | 0 | 2 | 0 | - | Logging, System |
| **dc1-leaf1** | 26 | 21 | 0 | 5 | 0 | - | Interfaces, Logging, MLAG, System |
| **dc1-leaf2** | 26 | 21 | 0 | 5 | 0 | - | Interfaces, Logging, MLAG, System |
| **dc1-leaf3** | 26 | 21 | 0 | 5 | 0 | - | Interfaces, Logging, MLAG, System |
| **dc1-leaf4** | 26 | 21 | 0 | 5 | 0 | - | Interfaces, Logging, MLAG, System |
| **dc1-spine1** | 20 | 18 | 0 | 2 | 0 | - | Logging, System |
| **dc1-spine2** | 20 | 18 | 0 | 2 | 0 | - | Logging, System |
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
| **BGP** | 16 | 16 | 0 | 0 | 0 |
| **Configuration** | 32 | 32 | 0 | 0 | 0 |
| **Connectivity** | 32 | 32 | 0 | 0 | 0 |
| **Interfaces** | 104 | 96 | 0 | 8 | 0 |
| **Logging** | 16 | 0 | 0 | 16 | 0 |
| **MLAG** | 36 | 32 | 0 | 4 | 0 |
| **Routing** | 16 | 16 | 0 | 0 | 0 |
| **STP** | 16 | 16 | 0 | 0 | 0 |
| **System** | 112 | 96 | 0 | 16 | 0 |
| **VXLAN** | 12 | 12 | 0 | 0 | 0 |

## 🧪 Test Results <a id="test-results"></a>

| Device | Categories | Test | Description | Result | Messages |
| :- | :- | :- | :- | :- | :- |
| dc1-borderleaf1 | Logging | VerifyLoggingErrors | Verifies there are no syslog messages with a severity of ERRORS or higher. | ❌&nbsp;Failure | Device has reported syslog messages with a severity of ERRORS or higher:<br>Mar 17 03:45:17 localhost LoadConfig: %SYSDB-3-STARTUP_CONFIG_PARSE_ERROR: Errors encountered in parsing the startup-config<br> Mar 17 03:45:39 dc1-borderleaf1 PhyEthtool-1: %ETH-3-NETLINKFAIL: Cannot init netlink stats cache : NETLINK Error Error fetching statistics  <extra parameters: '-31' ><br> Mar 17 03:45:47 dc1-borderleaf1 ProcMgr: %PROCMGR-3-SHUTDOWNREQUESTED: ProcMgr shutdown requested via SIGQUIT or SIGTERM to worker (PID=1485) -- Master ProcMgr (PID=1485) exiting.<br> Mar 17 03:46:03 dc1-borderleaf1 LoadConfig: %SYSDB-3-STARTUP_CONFIG_PARSE_ERROR: Errors encountered in parsing the startup-config<br> <br> |
| dc1-borderleaf1 | System | VerifyNTP | Verifies if NTP is synchronised. | ❌&nbsp;Failure | NTP status mismatch - Expected: synchronised Actual: NTP is disabled. |
| dc1-borderleaf2 | Logging | VerifyLoggingErrors | Verifies there are no syslog messages with a severity of ERRORS or higher. | ❌&nbsp;Failure | Device has reported syslog messages with a severity of ERRORS or higher:<br>Mar 17 03:45:01 localhost LoadConfig: %SYSDB-3-STARTUP_CONFIG_PARSE_ERROR: Errors encountered in parsing the startup-config<br> Mar 17 03:45:38 dc1-borderleaf2 PhyEthtool-1: %ETH-3-NETLINKFAIL: Cannot init netlink stats cache : NETLINK Error Error fetching statistics  <extra parameters: '-31' ><br> Mar 17 03:45:45 dc1-borderleaf2 ProcMgr: %PROCMGR-3-SHUTDOWNREQUESTED: ProcMgr shutdown requested via SIGQUIT or SIGTERM to worker (PID=1484) -- Master ProcMgr (PID=1484) exiting.<br> Mar 17 03:45:45 dc1-borderleaf2 Stp: %FWK-3-SOCKET_CLOSE_REMOTE: Connection to StpTxRx (pid:1876) at tbl://stpTxRxListen/+n closed by peer (EOF)<br> Mar 17 03:45:45 dc1-borderleaf2 Stp: %FWK-3-MOUNT_PEER_CLOSED: Peer closed socket connection. (tbl://stpTxRxListen/+n-in)(StpTxRx (pid:1876))<br> Mar 17 03:46:01 dc1-borderleaf2 LoadConfig: %SYSDB-3-STARTUP_CONFIG_PARSE_ERROR: Errors encountered in parsing the startup-config<br> <br> |
| dc1-borderleaf2 | System | VerifyNTP | Verifies if NTP is synchronised. | ❌&nbsp;Failure | NTP status mismatch - Expected: synchronised Actual: NTP is disabled. |
| dc1-leaf1 | Interfaces | VerifyInterfacesStatus | Verifies the operational states of specified interfaces to ensure they match expected configurations. | ❌&nbsp;Failure | Interface: Port-Channel7 - Status mismatch - Expected: up/up, Actual: down/lowerLayerDown<br>Interface: Port-Channel9 - Status mismatch - Expected: up/up, Actual: down/lowerLayerDown |
| dc1-leaf1 | Interfaces | VerifyPortChannels | Verifies there are no inactive ports in port channels. | ❌&nbsp;Failure | Interface: Port-Channel9 - Inactive port(s) - Ethernet9, PeerEthernet9<br>Interface: Port-Channel7 - Inactive port(s) - Ethernet7, PeerEthernet7 |
| dc1-leaf1 | Logging | VerifyLoggingErrors | Verifies there are no syslog messages with a severity of ERRORS or higher. | ❌&nbsp;Failure | Device has reported syslog messages with a severity of ERRORS or higher:<br>Mar 17 03:45:31 dc1-leaf1 PhyEthtool-1: %ETH-3-NETLINKFAIL: Cannot init netlink stats cache : NETLINK Error Error fetching statistics  <extra parameters: '-31' ><br> Mar 17 03:45:37 dc1-leaf1 ProcMgr: %PROCMGR-3-SHUTDOWNREQUESTED: ProcMgr shutdown requested via SIGQUIT or SIGTERM to worker (PID=1482) -- Master ProcMgr (PID=1482) exiting.<br> Mar 17 03:45:37 dc1-leaf1 Stp: %FWK-3-SOCKET_CLOSE_REMOTE: Connection to StpTxRx (pid:1853) at tbl://stpTxRxListen/+n closed by peer (EOF)<br> Mar 17 03:45:37 dc1-leaf1 Stp: %FWK-3-MOUNT_PEER_CLOSED: Peer closed socket connection. (tbl://stpTxRxListen/+n-in)(StpTxRx (pid:1853))<br> <br> |
| dc1-leaf1 | MLAG | VerifyMlagInterfaces | Verifies there are no inactive or active-partial MLAG ports. | ❌&nbsp;Failure | MLAG status is not ok - Inactive Ports: 2 Partial Active Ports: 0 |
| dc1-leaf1 | System | VerifyNTP | Verifies if NTP is synchronised. | ❌&nbsp;Failure | NTP status mismatch - Expected: synchronised Actual: NTP is disabled. |
| dc1-leaf2 | Interfaces | VerifyInterfacesStatus | Verifies the operational states of specified interfaces to ensure they match expected configurations. | ❌&nbsp;Failure | Interface: Port-Channel7 - Status mismatch - Expected: up/up, Actual: down/lowerLayerDown<br>Interface: Port-Channel9 - Status mismatch - Expected: up/up, Actual: down/lowerLayerDown |
| dc1-leaf2 | Interfaces | VerifyPortChannels | Verifies there are no inactive ports in port channels. | ❌&nbsp;Failure | Interface: Port-Channel7 - Inactive port(s) - Ethernet7, PeerEthernet7<br>Interface: Port-Channel9 - Inactive port(s) - Ethernet9, PeerEthernet9 |
| dc1-leaf2 | Logging | VerifyLoggingErrors | Verifies there are no syslog messages with a severity of ERRORS or higher. | ❌&nbsp;Failure | Device has reported syslog messages with a severity of ERRORS or higher:<br>Mar 17 03:45:20 dc1-leaf2 PhyEthtool-1: %ETH-3-NETLINKFAIL: Cannot init netlink stats cache : NETLINK Error Error fetching statistics  <extra parameters: '-31' ><br> Mar 17 03:45:27 dc1-leaf2 ProcMgr: %PROCMGR-3-SHUTDOWNREQUESTED: ProcMgr shutdown requested via SIGQUIT or SIGTERM to worker (PID=1479) -- Master ProcMgr (PID=1479) exiting.<br> <br> |
| dc1-leaf2 | MLAG | VerifyMlagInterfaces | Verifies there are no inactive or active-partial MLAG ports. | ❌&nbsp;Failure | MLAG status is not ok - Inactive Ports: 2 Partial Active Ports: 0 |
| dc1-leaf2 | System | VerifyNTP | Verifies if NTP is synchronised. | ❌&nbsp;Failure | NTP status mismatch - Expected: synchronised Actual: NTP is disabled. |
| dc1-leaf3 | Interfaces | VerifyInterfacesStatus | Verifies the operational states of specified interfaces to ensure they match expected configurations. | ❌&nbsp;Failure | Interface: Port-Channel7 - Status mismatch - Expected: up/up, Actual: down/lowerLayerDown<br>Interface: Port-Channel9 - Status mismatch - Expected: up/up, Actual: down/lowerLayerDown |
| dc1-leaf3 | Interfaces | VerifyPortChannels | Verifies there are no inactive ports in port channels. | ❌&nbsp;Failure | Interface: Port-Channel9 - Inactive port(s) - Ethernet9, PeerEthernet9<br>Interface: Port-Channel7 - Inactive port(s) - Ethernet7, PeerEthernet7 |
| dc1-leaf3 | Logging | VerifyLoggingErrors | Verifies there are no syslog messages with a severity of ERRORS or higher. | ❌&nbsp;Failure | Device has reported syslog messages with a severity of ERRORS or higher:<br>Mar 17 03:45:39 dc1-leaf3 PhyEthtool-1: %ETH-3-NETLINKFAIL: Cannot init netlink stats cache : NETLINK Error Error fetching statistics  <extra parameters: '-31' ><br> Mar 17 03:45:45 dc1-leaf3 ProcMgr: %PROCMGR-3-SHUTDOWNREQUESTED: ProcMgr shutdown requested via SIGQUIT or SIGTERM to worker (PID=1486) -- Master ProcMgr (PID=1486) exiting.<br> Mar 17 03:45:45 dc1-leaf3 Stp: %FWK-3-SOCKET_CLOSE_REMOTE: Connection to StpTxRx (pid:1878) at tbl://stpTxRxListen/+n closed by peer (EOF)<br> Mar 17 03:45:45 dc1-leaf3 Stp: %FWK-3-MOUNT_PEER_CLOSED: Peer closed socket connection. (tbl://stpTxRxListen/+n-in)(StpTxRx (pid:1878))<br> <br> |
| dc1-leaf3 | MLAG | VerifyMlagInterfaces | Verifies there are no inactive or active-partial MLAG ports. | ❌&nbsp;Failure | MLAG status is not ok - Inactive Ports: 2 Partial Active Ports: 0 |
| dc1-leaf3 | System | VerifyNTP | Verifies if NTP is synchronised. | ❌&nbsp;Failure | NTP status mismatch - Expected: synchronised Actual: NTP is disabled. |
| dc1-leaf4 | Interfaces | VerifyInterfacesStatus | Verifies the operational states of specified interfaces to ensure they match expected configurations. | ❌&nbsp;Failure | Interface: Port-Channel7 - Status mismatch - Expected: up/up, Actual: down/lowerLayerDown<br>Interface: Port-Channel9 - Status mismatch - Expected: up/up, Actual: down/lowerLayerDown |
| dc1-leaf4 | Interfaces | VerifyPortChannels | Verifies there are no inactive ports in port channels. | ❌&nbsp;Failure | Interface: Port-Channel7 - Inactive port(s) - Ethernet7, PeerEthernet7<br>Interface: Port-Channel9 - Inactive port(s) - Ethernet9, PeerEthernet9 |
| dc1-leaf4 | Logging | VerifyLoggingErrors | Verifies there are no syslog messages with a severity of ERRORS or higher. | ❌&nbsp;Failure | Device has reported syslog messages with a severity of ERRORS or higher:<br>Mar 17 03:45:20 dc1-leaf4 PhyEthtool-1: %ETH-3-NETLINKFAIL: Cannot init netlink stats cache : NETLINK Error Error fetching statistics  <extra parameters: '-31' ><br> Mar 17 03:45:26 dc1-leaf4 ProcMgr: %PROCMGR-3-SHUTDOWNREQUESTED: ProcMgr shutdown requested via SIGQUIT or SIGTERM to worker (PID=1485) -- Master ProcMgr (PID=1485) exiting.<br> Mar 17 03:45:26 dc1-leaf4 Stp: %FWK-3-SOCKET_CLOSE_REMOTE: Connection to StpTxRx (pid:1876) at tbl://stpTxRxListen/+n closed by peer (EOF)<br> Mar 17 03:45:26 dc1-leaf4 Stp: %FWK-3-MOUNT_PEER_CLOSED: Peer closed socket connection. (tbl://stpTxRxListen/+n-in)(StpTxRx (pid:1876))<br> <br> |
| dc1-leaf4 | MLAG | VerifyMlagInterfaces | Verifies there are no inactive or active-partial MLAG ports. | ❌&nbsp;Failure | MLAG status is not ok - Inactive Ports: 2 Partial Active Ports: 0 |
| dc1-leaf4 | System | VerifyNTP | Verifies if NTP is synchronised. | ❌&nbsp;Failure | NTP status mismatch - Expected: synchronised Actual: NTP is disabled. |
| dc1-spine1 | Logging | VerifyLoggingErrors | Verifies there are no syslog messages with a severity of ERRORS or higher. | ❌&nbsp;Failure | Device has reported syslog messages with a severity of ERRORS or higher:<br>Mar 17 03:45:43 dc1-spine1 PhyEthtool-1: %ETH-3-NETLINKFAIL: Cannot init netlink stats cache : NETLINK Error Error fetching statistics  <extra parameters: '-31' ><br> Mar 17 03:45:49 dc1-spine1 ProcMgr: %PROCMGR-3-SHUTDOWNREQUESTED: ProcMgr shutdown requested via SIGQUIT or SIGTERM to worker (PID=1480) -- Master ProcMgr (PID=1480) exiting.<br> <br> |
| dc1-spine1 | System | VerifyNTP | Verifies if NTP is synchronised. | ❌&nbsp;Failure | NTP status mismatch - Expected: synchronised Actual: NTP is disabled. |
| dc1-spine2 | Logging | VerifyLoggingErrors | Verifies there are no syslog messages with a severity of ERRORS or higher. | ❌&nbsp;Failure | Device has reported syslog messages with a severity of ERRORS or higher:<br>Mar 17 03:45:48 dc1-spine2 PhyEthtool-1: %ETH-3-NETLINKFAIL: Cannot init netlink stats cache : NETLINK Error Error fetching statistics  <extra parameters: '-31' ><br> Mar 17 03:45:54 dc1-spine2 ProcMgr: %PROCMGR-3-SHUTDOWNREQUESTED: ProcMgr shutdown requested via SIGQUIT or SIGTERM to worker (PID=1481) -- Master ProcMgr (PID=1481) exiting.<br> Mar 17 03:45:54 dc1-spine2 StpTxRx: %FWK-3-SOCKET_CLOSE_REMOTE: Connection to Stp (pid:1879) at tbl://stpListen/+n closed by peer (EOF)<br> Mar 17 03:45:54 dc1-spine2 StpTxRx: %FWK-3-MOUNT_PEER_CLOSED: Peer closed socket connection. (tbl://stpListen/+n-in)(Stp (pid:1879))<br> <br> |
| dc1-spine2 | System | VerifyNTP | Verifies if NTP is synchronised. | ❌&nbsp;Failure | NTP status mismatch - Expected: synchronised Actual: NTP is disabled. |
| dc2-borderleaf1 | Logging | VerifyLoggingErrors | Verifies there are no syslog messages with a severity of ERRORS or higher. | ❌&nbsp;Failure | Device has reported syslog messages with a severity of ERRORS or higher:<br>Mar 17 03:45:18 localhost LoadConfig: %SYSDB-3-STARTUP_CONFIG_PARSE_ERROR: Errors encountered in parsing the startup-config<br> Mar 17 03:45:57 dc2-borderleaf1 PhyEthtool-1: %ETH-3-NETLINKFAIL: Cannot init netlink stats cache : NETLINK Error Error fetching statistics  <extra parameters: '-31' ><br> Mar 17 03:46:04 dc2-borderleaf1 ProcMgr: %PROCMGR-3-SHUTDOWNREQUESTED: ProcMgr shutdown requested via SIGQUIT or SIGTERM to worker (PID=1487) -- Master ProcMgr (PID=1487) exiting.<br> Mar 17 03:46:04 dc2-borderleaf1 Stp: %FWK-3-SOCKET_CLOSE_REMOTE: Connection to StpTxRx (pid:1901) at tbl://stpTxRxListen/+n closed by peer (EOF)<br> Mar 17 03:46:04 dc2-borderleaf1 Stp: %FWK-3-MOUNT_PEER_CLOSED: Peer closed socket connection. (tbl://stpTxRxListen/+n-in)(StpTxRx (pid:1901))<br> Mar 17 03:46:20 dc2-borderleaf1 LoadConfig: %SYSDB-3-STARTUP_CONFIG_PARSE_ERROR: Errors encountered in parsing the startup-config<br> <br> |
| dc2-borderleaf1 | System | VerifyNTP | Verifies if NTP is synchronised. | ❌&nbsp;Failure | NTP status mismatch - Expected: synchronised Actual: NTP is disabled. |
| dc2-borderleaf2 | Logging | VerifyLoggingErrors | Verifies there are no syslog messages with a severity of ERRORS or higher. | ❌&nbsp;Failure | Device has reported syslog messages with a severity of ERRORS or higher:<br>Mar 17 03:45:27 localhost LoadConfig: %SYSDB-3-STARTUP_CONFIG_PARSE_ERROR: Errors encountered in parsing the startup-config<br> Mar 17 03:45:52 dc2-borderleaf2 PhyEthtool-1: %ETH-3-NETLINKFAIL: Cannot init netlink stats cache : NETLINK Error Error fetching statistics  <extra parameters: '-31' ><br> Mar 17 03:46:00 dc2-borderleaf2 ProcMgr: %PROCMGR-3-SHUTDOWNREQUESTED: ProcMgr shutdown requested via SIGQUIT or SIGTERM to worker (PID=1482) -- Master ProcMgr (PID=1482) exiting.<br> Mar 17 03:46:00 dc2-borderleaf2 Stp: %FWK-3-SOCKET_CLOSE_REMOTE: Connection to StpTxRx (pid:1885) at tbl://stpTxRxListen/+n closed by peer (EOF)<br> Mar 17 03:46:00 dc2-borderleaf2 Stp: %FWK-3-MOUNT_PEER_CLOSED: Peer closed socket connection. (tbl://stpTxRxListen/+n-in)(StpTxRx (pid:1885))<br> Mar 17 03:46:20 dc2-borderleaf2 LoadConfig: %SYSDB-3-STARTUP_CONFIG_PARSE_ERROR: Errors encountered in parsing the startup-config<br> <br> |
| dc2-borderleaf2 | System | VerifyNTP | Verifies if NTP is synchronised. | ❌&nbsp;Failure | NTP status mismatch - Expected: synchronised Actual: NTP is disabled. |
| dc2-leaf1 | Logging | VerifyLoggingErrors | Verifies there are no syslog messages with a severity of ERRORS or higher. | ❌&nbsp;Failure | Device has reported syslog messages with a severity of ERRORS or higher:<br>Mar 17 03:46:00 dc2-leaf1 PhyEthtool-1: %ETH-3-NETLINKFAIL: Cannot init netlink stats cache : NETLINK Error Error fetching statistics  <extra parameters: '-31' ><br> Mar 17 03:46:07 dc2-leaf1 ProcMgr: %PROCMGR-3-SHUTDOWNREQUESTED: ProcMgr shutdown requested via SIGQUIT or SIGTERM to worker (PID=1483) -- Master ProcMgr (PID=1483) exiting.<br> Mar 17 03:46:07 dc2-leaf1 StpTxRx: %FWK-3-SOCKET_CLOSE_REMOTE: Connection to Stp (pid:1879) at tbl://stpListen/+n closed by peer (EOF)<br> Mar 17 03:46:07 dc2-leaf1 StpTxRx: %FWK-3-MOUNT_PEER_CLOSED: Peer closed socket connection. (tbl://stpListen/+n-in)(Stp (pid:1879))<br> <br> |
| dc2-leaf1 | System | VerifyNTP | Verifies if NTP is synchronised. | ❌&nbsp;Failure | NTP status mismatch - Expected: synchronised Actual: NTP is disabled. |
| dc2-leaf2 | Logging | VerifyLoggingErrors | Verifies there are no syslog messages with a severity of ERRORS or higher. | ❌&nbsp;Failure | Device has reported syslog messages with a severity of ERRORS or higher:<br>Mar 17 03:45:29 dc2-leaf2 PhyEthtool-1: %ETH-3-NETLINKFAIL: Cannot init netlink stats cache : NETLINK Error Error fetching statistics  <extra parameters: '-31' ><br> Mar 17 03:45:36 dc2-leaf2 ProcMgr: %PROCMGR-3-SHUTDOWNREQUESTED: ProcMgr shutdown requested via SIGQUIT or SIGTERM to worker (PID=1484) -- Master ProcMgr (PID=1484) exiting.<br> Mar 17 03:45:36 dc2-leaf2 Stp: %FWK-3-SOCKET_CLOSE_REMOTE: Connection to StpTxRx (pid:1869) at tbl://stpTxRxListen/+n closed by peer (EOF)<br> Mar 17 03:45:36 dc2-leaf2 Stp: %FWK-3-MOUNT_PEER_CLOSED: Peer closed socket connection. (tbl://stpTxRxListen/+n-in)(StpTxRx (pid:1869))<br> <br> |
| dc2-leaf2 | System | VerifyNTP | Verifies if NTP is synchronised. | ❌&nbsp;Failure | NTP status mismatch - Expected: synchronised Actual: NTP is disabled. |
| dc2-leaf3 | Logging | VerifyLoggingErrors | Verifies there are no syslog messages with a severity of ERRORS or higher. | ❌&nbsp;Failure | Device has reported syslog messages with a severity of ERRORS or higher:<br>Mar 17 03:45:32 dc2-leaf3 PhyEthtool-1: %ETH-3-NETLINKFAIL: Cannot init netlink stats cache : NETLINK Error Error fetching statistics  <extra parameters: '-31' ><br> Mar 17 03:45:39 dc2-leaf3 ProcMgr: %PROCMGR-3-SHUTDOWNREQUESTED: ProcMgr shutdown requested via SIGQUIT or SIGTERM to worker (PID=1485) -- Master ProcMgr (PID=1485) exiting.<br> <br> |
| dc2-leaf3 | System | VerifyNTP | Verifies if NTP is synchronised. | ❌&nbsp;Failure | NTP status mismatch - Expected: synchronised Actual: NTP is disabled. |
| dc2-leaf4 | Logging | VerifyLoggingErrors | Verifies there are no syslog messages with a severity of ERRORS or higher. | ❌&nbsp;Failure | Device has reported syslog messages with a severity of ERRORS or higher:<br>Mar 17 03:46:06 dc2-leaf4 PhyEthtool-1: %ETH-3-NETLINKFAIL: Cannot init netlink stats cache : NETLINK Error Error fetching statistics  <extra parameters: '-31' ><br> Mar 17 03:46:13 dc2-leaf4 ProcMgr: %PROCMGR-3-SHUTDOWNREQUESTED: ProcMgr shutdown requested via SIGQUIT or SIGTERM to worker (PID=1489) -- Master ProcMgr (PID=1489) exiting.<br> Mar 17 03:46:13 dc2-leaf4 ConfigAgent: %FWK-3-SOCKET_CLOSE_REMOTE: Connection to Sysdb (pid:1677) at tbl://sysdb/+n closed by peer (EOF)<br> Mar 17 03:46:13 dc2-leaf4 StageMgr: %FWK-3-SOCKET_CLOSE_REMOTE: Connection to Sysdb (pid:1677) at tbl://sysdb/+n closed by peer (EOF)<br> Mar 17 03:46:13 dc2-leaf4 StageMgr: %FWK-3-MOUNT_PEER_CLOSED: Peer closed socket connection. (tbl://sysdb/+n-in)(Sysdb (pid:1677))<br> Mar 17 03:46:13 dc2-leaf4 StageMgr: %FWK-3-MOUNT_CLOSED_EXIT: Process exiting.<br> Mar 17 03:46:13 dc2-leaf4 ConfigAgent: %FWK-3-MOUNT_PEER_CLOSED: Peer closed socket connection. (tbl://sysdb/+n-in)(Sysdb (pid:1677))<br> Mar 17 03:46:13 dc2-leaf4 ConfigAgent: %FWK-3-MOUNT_CLOSED_EXIT: Process exiting.<br> <br> |
| dc2-leaf4 | System | VerifyNTP | Verifies if NTP is synchronised. | ❌&nbsp;Failure | NTP status mismatch - Expected: synchronised Actual: NTP is disabled. |
| dc2-spine1 | Logging | VerifyLoggingErrors | Verifies there are no syslog messages with a severity of ERRORS or higher. | ❌&nbsp;Failure | Device has reported syslog messages with a severity of ERRORS or higher:<br>Mar 17 03:46:01 dc2-spine1 PhyEthtool-1: %ETH-3-NETLINKFAIL: Cannot init netlink stats cache : NETLINK Error Error fetching statistics  <extra parameters: '-31' ><br> Mar 17 03:46:07 dc2-spine1 ProcMgr: %PROCMGR-3-SHUTDOWNREQUESTED: ProcMgr shutdown requested via SIGQUIT or SIGTERM to worker (PID=1480) -- Master ProcMgr (PID=1480) exiting.<br> <br> |
| dc2-spine1 | System | VerifyNTP | Verifies if NTP is synchronised. | ❌&nbsp;Failure | NTP status mismatch - Expected: synchronised Actual: NTP is disabled. |
| dc2-spine2 | Logging | VerifyLoggingErrors | Verifies there are no syslog messages with a severity of ERRORS or higher. | ❌&nbsp;Failure | Device has reported syslog messages with a severity of ERRORS or higher:<br>Mar 17 03:45:03 dc2-spine2 PhyEthtool-1: %ETH-3-NETLINKFAIL: Cannot init netlink stats cache : NETLINK Error Error fetching statistics  <extra parameters: '-31' ><br> Mar 17 03:45:10 dc2-spine2 ProcMgr: %PROCMGR-3-SHUTDOWNREQUESTED: ProcMgr shutdown requested via SIGQUIT or SIGTERM to worker (PID=1485) -- Master ProcMgr (PID=1485) exiting.<br> Mar 17 03:45:10 dc2-spine2 Stp: %FWK-3-SOCKET_CLOSE_REMOTE: Connection to StpTxRx (pid:1853) at tbl://stpTxRxListen/+n closed by peer (EOF)<br> <br> |
| dc2-spine2 | System | VerifyNTP | Verifies if NTP is synchronised. | ❌&nbsp;Failure | NTP status mismatch - Expected: synchronised Actual: NTP is disabled. |
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
| dc1-spine1 | BGP | VerifyBGPPeerSession | Verifies the session state of BGP peers. | ✅&nbsp;Success | - |
| dc1-spine1 | Configuration | VerifyRunningConfigDiffs | Verifies there is no difference between the running-config and the startup-config. | ✅&nbsp;Success | - |
| dc1-spine1 | Configuration | VerifyZeroTouch | Verifies ZeroTouch is disabled. | ✅&nbsp;Success | - |
| dc1-spine1 | Connectivity | VerifyLLDPNeighbors | Verifies the connection status of the specified LLDP (Link Layer Discovery Protocol) neighbors. | ✅&nbsp;Success | - |
| dc1-spine1 | Connectivity | VerifyReachability | Verifies point-to-point reachability between Ethernet interfaces. | ✅&nbsp;Success | - |
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
| dc1-spine2 | BGP | VerifyBGPPeerSession | Verifies the session state of BGP peers. | ✅&nbsp;Success | - |
| dc1-spine2 | Configuration | VerifyRunningConfigDiffs | Verifies there is no difference between the running-config and the startup-config. | ✅&nbsp;Success | - |
| dc1-spine2 | Configuration | VerifyZeroTouch | Verifies ZeroTouch is disabled. | ✅&nbsp;Success | - |
| dc1-spine2 | Connectivity | VerifyLLDPNeighbors | Verifies the connection status of the specified LLDP (Link Layer Discovery Protocol) neighbors. | ✅&nbsp;Success | - |
| dc1-spine2 | Connectivity | VerifyReachability | Verifies point-to-point reachability between Ethernet interfaces. | ✅&nbsp;Success | - |
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
