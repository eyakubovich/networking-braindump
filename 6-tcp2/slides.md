# Networking Brain Dump

### Episode 6: Still more TCP

---
# Last time on NBD...
- UDP
  - Datagrams on top of IP
  - Ports and checksum
- TCP
  - Reliable byte stream

---
# A note about 3-way handshake
- Protection against IP spoofing
- If client spoofs an IP:
  - Server replies to it
  - Does not get routed to the client
  - Can't complete handshake

---
# Flow control
- Fast sender and slow receiver
- Receivers buffers will fill up
- Will start dropping packets
- Will cause retransmissions
- Can we avoid it?

---
# Flow control
- TCP header includes a "Window" (RWND) field
- Tells the peer how much room left in the rx-buffer
- Sender will not send more than RWND bytes

---
# Flow control
- Recall: sender bounded by tx-buffer room
- min(tx-buffer-free, RWND)
- Receiver can control BDP

---
# Window scaling
- RWND field is 16-bits!
- Limits to 64KB -- ouch!
- Use a multiplier
  - Argreed upon during handshake
  - Uses TCP Option 3

---
# Congestion control
- Internet meltdown of the 1980's
- Intermediate routers get overwhelmed
  - Drop packets
  - Endpoints retransmit
  - Makes things worse

---
# Congestion control
- Sender maintains a CWND
- Limits how much it can send
- Sets CWND low
- Increases CWND (on ACKs)
- Decreases on signs of trouble

---
# Congestion control (classic)
- Slow start:
  - Rapid increase of CWND
  - Doubles the CWND every RTT
  - Stops when CWND >= SSthresh
- Congestion avoidance:
  - Linear increase of CWND
- On packet loss:
  - Halfs the CWND

---
# Congestion control
- Still hot area of research
- Many variants
- No single best strategy
  - Different for WAN vs LAN
- Prime reason for underutilization

---
# IP Masquerading (NAT)
- How IPv4 was saved
- Recall RFC1918 addresses:
  - 10.x.x.x
  - 192.168.x.x
  - 172.16.x.x - 172.31.x.x
  - Don't get routed on the Internet
- Assigned to hosts within an org

---
# IP Masquerading (NAT)
- How does an RFC1918 host watch YouTube?
- Edge router has a public IP
- Substitutes RFC1918 addresses for its own
- Substitutes source port

---
# IP Masquerading: example
- Your laptop to YouTube:
  - `Src:  10.100.201.23 : 36547`
  - `Dst:  216.58.194.206 : 80`

- Router performs SNAT:
  - `Src: 4.14.106.6 : 41798`
  - `Dst: 216.58.194.206 : 80`

---
# IP Masquerading: example
- YouTube to you:
  - `Src: 216.58.194.206 : 80`
  - `Dst: 4.14.106.6 : 41798`

- Router performs SNAT:
  - `Src: 216.58.194.206 : 80`
  - `Dst: 10.100.201.23 : 36547`

---
# IP Masquerading
- Greatly expands hosts on the Internet
- Resource intensive -- tracks connections
- Can be nested
- Curse of the middleboxes

---
# Bonus session
- What's interesting to you?
- Ken suggested SDN and Docker
