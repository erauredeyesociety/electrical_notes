# Introduction CPSC 462

*Extracted from [`Introduction CPSC 462.pdf`](<../class_materials/Introduction CPSC 462.pdf>) by `tools/extract_notes.py`.*
*Generated file -- edit the source, not this.*

> ⚠ **Low text density** -- 396 chars/page over 85 pages. This document is mostly images; the text below is only what the PDF text layer carries. Open the original for the diagrams.

---

---

## Page 1

Introduction: 1-1
Introduction to Computer Networks

---

## Page 2

Introduction
Goal: 
Get “feel,” “big picture,” 
introduction to terminology
Overview/roadmap:
What is the Internet? What is a protocol?
Network edge: hosts, access network, 
physical media
Network core: packet/circuit switching, 
internet structure
Performance: loss, delay, throughput
Protocol layers, service models
Security
History
Introduction: 1-2

---

## Page 3

Roadmap
What is the Internet?
What is a protocol?
Network edge: hosts, access network, 
physical media
Network core: packet/circuit switching, 
internet structure
Performance: loss, delay, throughput
Security
Protocol layers, service models
History
Introduction: 1-3

---

## Page 4

Internet
The Internet
Introduction: 1-4
mobile network
home network
enterprise
          network
national or global ISP
local or 
regional ISP
datacenter 
network
content 
provider 
network
Packet switches: forward 
packets (chunks of data)
▪routers, switches
Billions of connected 
computing devices: 
▪hosts = end systems 
▪running network apps/programs 
at the Internet’s “edge”

---

## Page 5

Internet
The Internet
Introduction: 1-5
mobile network
home network
enterprise
          network
national or global ISP
local or 
regional ISP
datacenter 
network
content 
provider 
network
Communication links
▪fiber, copper, radio, satellite
▪transmission rate: bandwidth
Networks
▪collection of devices, routers, 
links: managed by an organization

---

## Page 6

“Fun” Internet-connected devices
Introduction: 1-6
Web-enabled toaster +
weather forecaster
Internet phones
Slingbox: remote
control cable TV
Security Camera
IP picture frame
Internet 
refrigerator
Tweet-a-watt: 
monitor energy use
sensorized,
bed
mattress
Amazon Echo
Others?
Pacemaker & Monitor
AR devices
Fitbit
Gaming devices
cars
scooters
bikes

---

## Page 7

The Internet: a “nuts and bolts” view
Internet: “network of networks”
◦Interconnected ISPs
Introduction: 1-7
mobile network
home network
enterprise
          network
national or global ISP
local or 
regional ISP
datacenter 
network
content 
provider 
network
▪protocols are everywhere
• control sending, receiving of messages
• e.g., HTTP (Web), streaming video, 
Skype, TCP, UDP, IP, WiFi, 4G, Ethernet
Ethernet
HTTP
Skype
IP
WiFi
4G
TCP
Streaming
video
▪Internet standards
• RFC: Request for Comments
• IETF: Internet Engineering Task 
Force

---

## Page 8

The Internet: a “services” view
Infrastructure that provides services to 
applications:
◦Web, streaming video, multimedia teleconferencing, 
email, games, e-commerce, social media, inter-
connected appliances, …
Introduction: 1-8
mobile network
home network
enterprise
          network
national or global ISP
local or 
regional ISP
datacenter 
network
content 
provider 
network
HTTP
Skype
Streaming
video
▪provides programming interface to 
distributed applications:
• Different devices allow 
sending/receiving  apps to “connect” 
to, use  Internet transport service
• provides service options, analogous to 
postal service

---

## Page 9

Roadmap
What is the Internet?
What is a protocol?
Network edge: hosts, access network, 
physical media
Network core: packet/circuit switching, 
internet structure
Performance: loss, delay, throughput
Security
Protocol layers, service models
History
Introduction: 1-9

---

## Page 10

What’s a protocol?
Introduction: 1-10
Human protocols:
▪“what’s the time?”
▪“I have a question”
▪introductions
Network protocols:
▪computers (devices) rather than humans
▪all communication activity in Internet 
governed by protocols
Protocols define the format, order of 
messages sent and received among 
network entities, and actions taken 
on message transmission, receipt 
Rules for:
… specific messages sent
… specific actions taken 
when message received, 
or other events

---

## Page 11

What’s a protocol?
Introduction: 1-11
A human protocol and a computer network protocol:
Hi
Hi
What time 
is it?
2:00
time
TCP connection
response
<file>
TCP connection
request
GET http://https://erau.edu/

---

## Page 12

Roadmap
What is the Internet?
What is a protocol?
Network edge: hosts, access network, 
physical media
Network core: packet/circuit switching, 
internet structure
Performance: loss, delay, throughput
Security
Protocol layers, service models
History
Introduction: 1-12

---

## Page 13

A closer look at Internet structure
Network edge:
hosts: clients and servers
servers often in data centers
Introduction: 1-13
mobile network
home network
enterprise
          network
national or global ISP
local or 
regional ISP
datacenter 
network
content 
provider 
network

---

## Page 14

A closer look at Internet structure
Network edge:
hosts: clients and servers
servers often in data centers
Access networks, physical media:
wired, wireless communication links 
Introduction: 1-14
mobile network
home network
enterprise
          network
national or global ISP
local or 
regional ISP
datacenter 
network
content 
provider 
network

---

## Page 15

A closer look at Internet structure
Network edge:
hosts: clients and servers
servers often in data centers
Access networks, physical media:
wired, wireless communication links 
Network core: 
▪interconnected routers
▪network of networks
Introduction: 1-15
mobile network
home network
enterprise
          network
national or global ISP
local or 
regional ISP
datacenter 
network
content 
provider 
network

---

## Page 16

Access networks and physical media
Q: How to connect end systems to 
edge router?
residential access nets
institutional access networks (school, 
company)
mobile access networks (WiFi, 4G/5G)
Introduction: 1-16
mobile network
home network
enterprise
          network
national or global ISP
local or 
regional ISP
datacenter 
network
content 
provider 
network

---

## Page 17

ISP
Access networks: digital subscriber line (DSL)
Introduction: 1-17
central office
telephone
network
DSLAM
voice, data transmitted
at different frequencies over
dedicated line to central office
▪use existing telephone line to central office DSLAM
• data over DSL phone line goes to Internet
• voice over DSL phone line goes to telephone net
▪24-52 Mbps dedicated downstream transmission rate 
▪3.5-16 Mbps dedicated upstream transmission rate
DSL
modem
splitter
(DSL access 
multiplexer)
DSL provides a 
dedicated access 
line from the 
customer to the 
telephone 
company's 
equipment. It is 
usually 
asymmetric: 
downloading is 
faster than 
uploading.

---

## Page 18

Access networks: cable-based access
Introduction: 1-18
cable
modem
splitter
…
cable headend
data, TV transmitted at different 
frequencies over shared cable 
distribution network
▪HFC: hybrid fiber coax
• asymmetric: 
• up to 40 Mbps – 1.2 Gbps downstream transmission rate
• 30-100 Mbps upstream transmission rate
▪network of cable, fiber attaches homes to ISP router
• homes share access network to cable headend 
(cable modem termination system)
CMTS
ISP

---

## Page 19

Access networks: home networks
Introduction: 1-19
to/from headend or 
central office
cable or DSL modem
router, firewall, NAT
wired Ethernet (1 Gbps)
WiFi wireless access 
point (450 Mbps)
Wireless and wired
devices
often combined 
in single box

---

## Page 20

Wireless access networks
Introduction: 1-20
Shared wireless access network connects end system to router
▪via base station aka “access point”
Wireless local area networks 
(WLANs)
▪typically within or around 
building (~100 ft)
▪802.11b/g/n (WiFi): 11, 54, 450 
Mbps transmission rate
to Internet
to Internet
Wide-area cellular access networks
▪provided by mobile, cellular network 
operator (10’s km)
▪10’s Mbps 
▪5G cellular networks

---

## Page 21

Access networks: enterprise networks
Introduction: 1-21
▪companies, universities, etc.
▪mix of wired, wireless link technologies, connecting a mix of switches 
and routers (we’ll cover differences shortly)
▪Ethernet: wired access at 100Mbps, 1Gbps, 10Gbps 
▪WiFi: wireless access points at 11, 54, 450 Mbps 
Ethernet 
switch
institutional mail,
web servers
institutional router
Enterprise link to 
ISP (Internet)

---

## Page 22

Access networks: data center networks
Introduction: 1-22
▪high-bandwidth links (10s to 100s 
Gbps) connect hundreds to thousands 
of servers together, and to Internet
mobile network
home network
enterprise
          network
national or global ISP
local or 
regional ISP
datacenter 
network
content 
provider 
network
Courtesy: Massachusetts Green High Performance Computing 
Center (mghpcc.org)

---

## Page 23

Host: sends packets of data
Introduction: 1-23
host sending function:
▪takes application message
▪breaks into smaller chunks, 
known as packets, of length L bits
▪transmits packet into access 
network at transmission rate R
• link transmission rate, aka link 
capacity, aka link bandwidth
R: link transmission rate
host
1
2
two packets, 
L bits each
packet
transmission
delay
time needed to
transmit L-bit
packet into link
L (bits)
R (bits/sec)
=
=

---

## Page 24

Links: physical media
Introduction: 1-24
▪bit: propagates between
transmitter/receiver pairs
▪physical link: what lies 
between transmitter & 
receiver
▪guided media: 
• signals propagate in solid 
media: copper, fiber, coax
▪unguided media: 
• signals propagate freely, 
e.g., radio
Twisted pair (TP)
▪two insulated copper wires
• Category 5: 100 Mbps, 1 Gbps Ethernet
• Category 6: 10Gbps Ethernet

---

## Page 25

Links: physical media
Introduction: 1-25
Coaxial cable:
▪two concentric copper conductors
▪bidirectional
▪broadband:
• multiple frequency channels on cable
• 100’s Mbps per channel
Fiber optic cable:
▪glass fiber carrying light pulses, each 
pulse a bit
▪high-speed operation:
• high-speed point-to-point 
transmission (10’s-100’s Gbps)
▪low error rate: 
• repeaters spaced far apart 
• immune to electromagnetic noise

---

## Page 26

Links: physical media
Introduction: 1-26
Wireless radio
▪signal carried in various “bands” 
in electromagnetic spectrum
▪no physical “wire”
▪broadcast, “half-duplex” 
(sender to receiver or receiver to 
sender)
▪propagation environment 
effects:
• reflection 
• obstruction by objects
• Interference/noise
Radio link types:
▪Wireless LAN (WiFi)
• 10-100’s Mbps; 10’s of meters
▪wide-area (e.g., 4G cellular)
• 10’s Mbps over ~10 Km 
▪Bluetooth: cable replacement
• short distances, limited rates
▪terrestrial microwave
• point-to-point; 45 Mbps channels
▪satellite
• up to 45 Mbps per channel
• 270 msec end-end delay

---

## Page 27

Roadmap
What is the Internet?
What is a protocol?
Network edge: hosts, access network, 
physical media
Network core: packet/circuit switching, 
internet structure
Performance: loss, delay, throughput
Security
Protocol layers, service models
History
Introduction: 1-27

---

## Page 28

The network core
mesh of interconnected routers
packet-switching: hosts break application-layer 
messages into packets
◦network forwards packets from one 
router to the next, across links on path 
from source to destination
Introduction: 1-28
mobile network
home network
enterprise
          network
national or global ISP
local or 
regional ISP
datacenter 
network
content 
provider 
network

---

## Page 29

Two key network-core functions
Forwarding: 
aka “switching”
local action: move arriving 
packets from router’s input 
link to appropriate router 
output link
Introduction: 1-29
1
2
3
destination address in arriving
packet’s header
routing algorithm
header value output link
0100
0101
0111
1001
3
2
2
1
local forwarding table
local forwarding table
Routing: 
▪global action: 
determine source-
destination paths 
taken by packets
▪routing algorithms
routing algorithm

---

## Page 30

routing
Introduction: 1-30

---

## Page 31

forwarding
forwarding
Introduction: 1-31

---

## Page 32

Packet-switching: store-and-forward
packet transmission delay: takes L/R seconds to 
transmit (push out) L-bit packet into link at R bps
store and forward: entire packet must  arrive at 
router before it can be transmitted on next link
Introduction: 1-32
source
R bps
destination
1
2
3
L bits
per packet
R bps
One-hop numerical example:
▪L = 10 Kbits
▪R = 100 Mbps
▪one-hop transmission delay 
= 0.1 msec

---

## Page 33

Packet-switching: queueing
Introduction: 1-33
A
B
C
R = 100 Mb/s
R = 1.5 Mb/s
D
E
queue of packets
waiting for transmission 
over output link
Queueing occurs when work arrives faster than it can be serviced:

---

## Page 34

Packet-switching: queueing
Packet queuing and loss: if arrival rate (in bps) to link exceeds transmission rate (bps) 
of link for some period of time:
packets will queue, waiting to be transmitted on output link 
packets can be dropped (lost) if memory (buffer) in router fills up
Introduction: 1-34
A
B
C
R = 100 Mb/s
R = 1.5 Mb/s
D
E
queue of packets
waiting for transmission 
over output link

---

## Page 35

Alternative to packet switching: circuit switching
end-end resources allocated to, reserved for “call” 
between source and destination
in this diagram, each link has four circuits. 
◦call gets 2nd circuit in top link and 1st circuit in right 
link.
dedicated resources: no sharing
◦circuit-like (guaranteed) performance
circuit segment idle if not used by call (no 
sharing)
Introduction: 1-35
▪commonly used in traditional telephone networks

---

## Page 36

Circuit switching: FDM and TDM
Frequency Division Multiplexing (FDM)
optical, electromagnetic frequencies divided 
into (narrow) frequency bands
•Each call allocated its own band, can transmit 
at max rate of that narrow band 
Introduction: 1-36
frequency
time
frequency
time
4 users
Time Division Multiplexing (TDM)
▪time divided into slots
▪each call allocated periodic slot(s), can 
transmit at maximum rate of (wider) 
frequency band (only) during its time 
slot(s)

---

## Page 37

Packet switching versus circuit switching
Introduction: 1-37
Example:
▪1 Gb/s link
▪each user: 
• 100 Mb/s when “active”
• active 10% of time
Q: how many users can use this network under circuit-switching and packet switching?
Calculator
N 
users
1 Gbps link
▪circuit-switching: 10 users
▪packet switching - queueing:  with 35 users, probability > 10 active at same 
time is less than .0004 *

---

## Page 38

Packet switching versus circuit switching
Introduction: 1-38
▪great for “bursty” data – sometimes has data to send, but at other times not
• resource sharing
• simpler, no call setup
▪excessive congestion possible: packet delay and loss due to buffer overflow
• protocols needed for reliable data transfer, congestion control
Is packet switching a “slam dunk winner”?

---

## Page 39

Internet structure: a “network of networks”
hosts connect to Internet via access 
Internet Service Providers (ISPs)
access ISPs in turn must be 
interconnected
◦so that any two hosts (anywhere!) can send 
packets to each other
resulting network of networks is very 
complex
mobile network
home network
enterprise
          network
national or global ISP
local or 
regional ISP
datacenter 
network
content 
provider 
network

---

## Page 40

Internet structure: a “network of networks”
Introduction: 1-40
Question: given millions of access ISPs, how to connect them together?
access
net
access
net
access
net
access
net
access
net
access
net
access
net
access
net
access
net
access
net
access
net
access
net
access
net
access
net
access
net
access
net

---

## Page 41

Internet structure: a “network of networks”
Introduction: 1-41
Question: given millions of access ISPs, how to connect them together?
access
net
access
net
access
net
access
net
access
net
access
net
access
net
access
net
access
net
access
net
access
net
access
net
access
net
access
net
access
net
access
net
connecting each access ISP to 
each other directly doesn’t scale: 
O(N2) connections.

---

## Page 42

Internet structure: a “network of networks”
Introduction: 1-42
Option: connect each access ISP to one global transit ISP? 
Customer and provider ISPs have economic agreement.
global
ISP
access
net
access
net
access
net
access
net
access
net
access
net
access
net
access
net
access
net
access
net
access
net
access
net
access
net
access
net
access
net
access
net

---

## Page 43

ISP A
ISP C
ISP B
Internet structure: a “network of networks”
Introduction: 1-43
access
net
access
net
access
net
access
net
access
net
access
net
access
net
access
net
access
net
access
net
access
net
access
net
access
net
access
net
access
net
access
net
But if one global ISP is viable business, there will be competitors ….

---

## Page 44

ISP A
ISP C
ISP B
Internet structure: a “network of networks”
Introduction: 1-44
access
net
access
net
access
net
access
net
access
net
access
net
access
net
access
net
access
net
access
net
access
net
access
net
access
net
access
net
access
net
access
net
But if one global ISP is viable business, there will be competitors …. who will 
want to be connected
IXP
peering link
Internet exchange point 
IXP

---

## Page 45

ISP A
ISP C
ISP B
Internet structure: a “network of networks”
Introduction: 1-45
access
net
access
net
access
net
access
net
access
net
access
net
access
net
access
net
access
net
access
net
access
net
… and regional networks may arise to connect access nets to ISPs 
IXP
IXP
access
net
access
net
regional ISP
access
net
access
net
access
net

---

## Page 46

ISP A
ISP C
ISP B
Internet structure: a “network of networks”
Introduction: 1-46
access
net
access
net
access
net
access
net
access
net
access
net
access
net
access
net
access
net
access
net
access
net
… and content provider networks  (e.g., Google, Microsoft…) may run 
their own network, to bring services, content close to end users
IXP
IXP
access
net
access
net
access
net
access
net
access
net
Content provider network
regional ISP
Internet exchange point 
peering link

---

## Page 47

Internet structure: a “network of networks”
Introduction: 1-47
access
ISP
access
ISP
access
ISP
access
ISP
access
ISP
access
ISP
access
ISP
access
ISP
At “center”: small # of well-connected large networks
▪“tier-1” commercial ISPs (e.g., Level 3, Sprint, AT&T, NTT), national & international coverage
▪content provider networks (e.g., Google, Facebook): private network that connects its 
data centers to Internet, often bypassing tier-1, regional ISPs
Regional ISP
Regional ISP
Tier 1 ISP
Tier 1 ISP
IXP
Google
IXP
IXP

---

## Page 48

Roadmap
What is the Internet?
What is a protocol?
Network edge: hosts, access network, 
physical media
Network core: packet/circuit switching, 
internet structure
Performance: delay, loss, throughput
Security
Protocol layers, service models
History
Introduction: 1-48

---

## Page 49

How do packet delay and loss occur?
packets queue in router buffers, waiting for turn for transmission
▪queue length grows when arrival rate to link (temporarily) exceeds output link capacity 
▪packet loss occurs when memory to hold queued packets fills up
Introduction: 1-49
A
B
packet being transmitted (transmission delay)
packets in buffers (queueing delay)
free (available) buffers: arriving packets 
dropped (loss) if no free buffers

---

## Page 50

Packet delay: four sources
Introduction: 1-50
dproc: nodal processing 
▪check bit errors
▪determine output link
▪typically < microsecs
dqueue: queueing delay
▪time waiting at output link for 
transmission 
▪depends on congestion level of 
router
propagation
nodal
processing
queueing
dnodal = dproc + dqueue + dtrans +  dprop
A
B
transmission

---

## Page 51

Packet delay: four sources
Introduction: 1-51
propagation
nodal
processing
queueing
dnodal = dproc + dqueue + dtrans +  dprop
A
B
transmission
dtrans: transmission delay:
▪L: packet length (bits) 
▪R: link transmission rate (bps)
▪dtrans = L/R
dprop: propagation delay:
▪d: length of physical link
▪s: propagation speed (~2x108 m/sec)
▪dprop = d/s
dtrans and dprop
very different

---

## Page 52

Caravan analogy
Introduction: 1-52
▪car ~ bit; caravan ~ packet; toll 
service ~ link transmission
▪toll booth takes 12 sec to service 
car (bit transmission time)
▪“propagate” at  100 km/hr
▪Q: How long until caravan is lined 
up before 2nd toll booth?
▪time to “push” entire caravan 
through toll booth onto 
highway = 12*10 = 120 sec
▪time for last car to propagate 
from 1st to 2nd toll both: 
100km/(100km/hr) = 1 hr
▪A: 62 minutes
toll booth
toll  booth
(aka link)
ten-car caravan
(aka 10-bit packet)
100 km
100 km
toll booth
toll booth

---

## Page 53

Packet queueing delay 
Introduction: 1-53
▪a: average packet arrival rate
▪L: packet length (bits)
▪R: link bandwidth (bit transmission rate)
▪La/R ~ 0: avg. queueing delay small
▪La/R -> 1: avg. queueing delay large
▪La/R > 1: more “work” arriving  is 
more than can be serviced -  average 
delay infinite!
La/R ~ 0
La/R -> 1
traffic intensity = La/R
average  queueing 
delay
1
service rate of bits
R
arrival rate of bits
L a
.
:
“traffic 
intensity”

---

## Page 54

“Real” Internet delays and routes
Introduction: 1-54
▪what do “real” Internet delay & loss look like? 
▪traceroute program: provides delay measurement from 
source to router along end-end Internet path towards 
destination.  For all i:
3 probes
3 probes
3 probes
• sends three packets that will reach router i on path towards 
destination (with time-to-live field value of i)
• router i will return packets to sender
• sender measures time interval between transmission and reply

---

## Page 55

Real Internet delays and routes
Introduction: 1-55
1  cs-gw (128.119.240.254)  1 ms  1 ms  2 ms
2  border1-rt-fa5-1-0.gw.umass.edu (128.119.3.145)  1 ms  1 ms  2 ms
3  cht-vbns.gw.umass.edu (128.119.3.130)  6 ms 5 ms 5 ms
4  jn1-at1-0-0-19.wor.vbns.net (204.147.132.129)  16 ms 11 ms 13 ms 
5  jn1-so7-0-0-0.wae.vbns.net (204.147.136.136)  21 ms 18 ms 18 ms 
6  abilene-vbns.abilene.ucaid.edu (198.32.11.9)  22 ms  18 ms  22 ms
7  nycm-wash.abilene.ucaid.edu (198.32.8.46)  22 ms  22 ms  22 ms
8  62.40.103.253 (62.40.103.253)  104 ms 109 ms 106 ms
9  de2-1.de1.de.geant.net (62.40.96.129)  109 ms 102 ms 104 ms
10  de.fr1.fr.geant.net (62.40.96.50)  113 ms 121 ms 114 ms
11  renater-gw.fr1.fr.geant.net (62.40.103.54)  112 ms  114 ms  112 ms
12  nio-n2.cssi.renater.fr (193.51.206.13)  111 ms  114 ms  116 ms
13  nice.cssi.renater.fr (195.220.98.102)  123 ms  125 ms  124 ms
14  r3t2-nice.cssi.renater.fr (195.220.98.110)  126 ms  126 ms  124 ms
15  eurecom-valbonne.r3t2.ft.net (193.48.50.54)  135 ms  128 ms  133 ms
16  194.214.211.25 (194.214.211.25)  126 ms  128 ms  126 ms
17  * * *
18  * * *
19  fantasia.eurecom.fr (193.55.113.142)  132 ms  128 ms  136 ms
traceroute: gaia.cs.umass.edu to www.eurecom.fr
* Do some traceroutes from exotic countries at www.traceroute.org
* means no response (probe lost, router not replying)
3 delay measurements from 
gaia.cs.umass.edu to cs-gw.cs.umass.edu 
3 delay measurements
to border1-rt-fa5-1-0.gw.umass.edu 
looks like delays 
decrease! Why?
trans-oceanic link
traceroute (on Mac terminal)
tracert (on Windows command line)
tracepath (on a Linux command line)

---

## Page 56

Packet loss
Introduction: 1-56
A
B
packet being transmitted
buffer 
(waiting area)
packet arriving to
full buffer is lost
▪queue (buffer) preceding link in buffer has finite capacity
▪packet arriving to full queue dropped (aka lost)
▪lost packet may be retransmitted by previous node, by source end 
system, or not at all

---

## Page 57

Throughput
Introduction: 1-57
▪throughput: rate (bits/time unit) at which bits are being sent from 
sender to receiver
• instantaneous: rate at given point in time
• average: rate over longer period of time
link capacity
 Rs bits/sec
link capacity
 Rc bits/sec
server sends bits 
(fluid) into pipe
pipe that can carry
fluid at rate
 (Rs bits/sec)
pipe that can carry
fluid at rate
 (Rc bits/sec)

---

## Page 58

Throughput
Introduction: 1-58
Rs < Rc  What is average end-end throughput?
Rs bits/sec
Rc bits/sec
Rs > Rc  What is average end-end throughput?
link on end-end path that constrains  end-end throughput
bottleneck link
Rs bits/sec
Rc bits/sec

---

## Page 59

Throughput: network scenario
Introduction: 1-59
10 connections (fairly) share backbone 
bottleneck link R bits/sec
Rs
Rs
Rs
Rc
Rc
Rc
R
▪per-connection end-
end throughput: 
min(Rc,Rs,R/10)
▪in practice: Rc or Rs is 
often bottleneck

---

## Page 60

Roadmap
What is the Internet?
What is a protocol?
Network edge: hosts, access network, 
physical media
Network core: packet/circuit switching, 
internet structure
Performance: loss, delay, throughput
Security
Protocol layers, service models
History
Introduction: 1-60

---

## Page 61

Network security
Introduction: 1-61
▪Internet not originally designed with (much) security in 
mind
• original vision: “a group of mutually trusting users attached to a 
transparent network” 
• Internet protocol designers playing “catch-up”
• security considerations in all layers!

---

## Page 62

Network security
Introduction: 1-62
▪Internet not originally designed with (much) security in 
mind
• original vision: “a group of mutually trusting users attached to a 
transparent network” ☺
• Internet protocol designers playing “catch-up”
• security considerations in all layers!
▪We now need to think about:
• how bad guys can attack computer networks
• how we can defend networks against attacks
• how to design architectures that are immune to attacks

---

## Page 63

Bad guys: packet interception
Introduction: 1-63
packet “sniffing”: 
▪broadcast media (shared Ethernet, wireless)
▪promiscuous network interface reads/records all packets (e.g., 
including passwords!) passing by
A
B
C
src:B dest:A     payload
Wireshark software used for our labs is a (free) packet-sniffer

---

## Page 64

Bad guys:  fake identity
Introduction: 1-64
IP spoofing: injection of packet with false source address
A
B
C
src:B dest:A     payload

---

## Page 65

Bad guys: denial of service
Introduction: 1-65
target
Denial of Service (DoS): attackers make resources (server, 
bandwidth) unavailable to legitimate traffic by 
overwhelming resource with bogus traffic
1. select target
2. break into hosts 
around the network 
(see botnet)
3. send packets to target 
from compromised 
hosts

---

## Page 66

Lines of defense:
Introduction: 1-66
▪authentication: proving you are who you say you are
• cellular networks provides hardware identity via SIM card; no such 
hardware assist in traditional Internet
▪confidentiality: via encryption
▪integrity checks: digital signatures prevent/detect tampering
▪access restrictions:  password-protected VPNs
▪firewalls: specialized “middleboxes” in access and core 
networks:
▪off-by-default: filter incoming packets to restrict senders, receivers, 
applications 
▪detecting/reacting to DOS attacks

---

## Page 67

Roadmap
What is the Internet?
What is a protocol?
Network edge: hosts, access network, 
physical media
Network core: packet/circuit switching, 
internet structure
Performance: loss, delay, throughput
Security
Protocol layers, service models
History
Introduction: 1-67

---

## Page 68

Protocol “layers” and reference models
Introduction: 1-68
Networks are complex,
with many “pieces”:
▪hosts
▪routers
▪links of various media
▪applications
▪protocols
▪hardware, software
Question: is there any 
hope of organizing 
structure of network?
▪and/or our discussion 
of networks?

---

## Page 69

Example: organization of air travel
Introduction: 1-69
▪
a series of steps, involving many services
ticket (purchase)
baggage (check)
gates (load)
runway takeoff
airplane routing
ticket (complain)
baggage (claim)
gates (unload)
runway landing
airplane routing
airplane routing
How would you define/discuss the system of airline travel?
end-to-end transfer of person plus baggage

---

## Page 70

Example: organization of air travel
Introduction: 1-70
ticket (purchase)
baggage (check)
gates (load)
runway takeoff
airplane routing
ticket (complain)
baggage (claim)
gates (unload)
runway landing
airplane routing
airplane routing
ticketing service
baggage service
gate service
runway service
routing service
layers: each layer implements a service
▪via its own internal-layer actions
▪relying on services provided by layer below

---

## Page 71

Why layering?
Introduction: 1-71
Approach to designing/discussing complex systems:
▪explicit structure allows identification, 
relationship of system’s pieces
• layered reference model for discussion
▪modularization eases maintenance, 
updating of system
• change in layer's service implementation: 
transparent to rest of system
• e.g., change in gate procedure doesn’t 
affect rest of system

---

## Page 72

Layered Internet protocol stack
Introduction: 1-72
▪application: supporting network applications
• HTTP, IMAP, SMTP, DNS
▪transport: process-process data transfer
• TCP, UDP
▪network: routing of datagrams from source to 
destination
• IP, routing protocols
▪link: data transfer between neighboring  
network elements
• Ethernet, 802.11 (WiFi), PPP
▪physical: bits “on the wire”
link
application
network
transport
physical
application
transport
network
link
physical

---

## Page 73

Services, Layering and Encapsulation
Introduction: 1-73
source
▪transport-layer protocol encapsulates 
application-layer message, M, with 
transport layer-layer header Ht to create a 
transport-layer segment
• Ht used by transport layer protocol to 
implement its service
application
transport
network
link
physical
destination
application
transport
network
link
physical
Transport-layer protocol transfers M (e.g., reliably) from 
one process to another, using services of network layer
Ht
M
Application exchanges messages to implement some 
application service using services of transport layer
M

---

## Page 74

Services, Layering and Encapsulation
Introduction: 1-74
source
Transport-layer protocol transfers M (e.g., reliably) from 
one process to another, using services of network layer
Ht
M
▪network-layer protocol encapsulates 
transport-layer segment  [Ht | M] with 
network layer-layer header Hn to create a 
network-layer datagram 
• Hn used by network layer protocol to 
implement its service
application
transport
network
link
physical
destination
M
application
transport
network
link
physical
M
Ht
Hn
Network-layer protocol transfers transport-layer segment 
[Ht | M] from one host to another, using link layer services

---

## Page 75

Services, Layering and Encapsulation
Introduction: 1-75
source
Ht
M
▪link-layer protocol encapsulates network 
datagram [Hn| [Ht |M], with link-layer header 
Hl to create a link-layer frame 
application
transport
network
link
physical
destination
M
application
transport
network
link
physical
M
Ht
Hn
Link-layer protocol transfers datagram [Hn| [Ht |M] from 
host to neighboring host
M
Ht
Hn
Hl
Network-layer protocol transfers transport-layer segment 
[Ht | M] from one host to another, using link layer services

---

## Page 76

Services, Layering and Encapsulation
Introduction: 1-76
source
application
transport
network
link
physical
destination
application
transport
network
link
physical
Ht
M
M
M
Ht
Hn
M
Ht
Hn
Hl
M
Ht
Hn
Ht
M
M
message
segment
datagram
frame
M
Ht
Hn
Hl

---

## Page 77

network
link
physical
application
transport
network
link
physical
application
transport
network
link
physical
Encapsulation: an end-end view
Introduction: 1-77
source
Ht
Hn
M
segment
Ht
datagram
destination
Ht
Hn
Hl
M
Ht
Hn
M
Ht
M
M
Ht
Hn
Hl
M
Ht
Hn
M
Ht
Hn
M
Ht
Hn
Hl
M
router
switch
message
M
Ht
M
Hn
frame
link
physical

---

## Page 78

ISO/OSI reference model
Introduction: 1-78
Two layers not found in Internet 
protocol stack!
▪presentation: allow applications to 
interpret meaning of data, e.g., encryption, 
compression, machine-specific conventions
▪session: synchronization, checkpointing, 
recovery of data exchange
▪Internet stack “missing” these layers!
• these services, if needed, must be 
implemented in application
• needed?
application
presentation
session
transport
network
link
physical
The seven layer OSI/ISO 
reference model

---

## Page 79

Roadmap
What is the Internet?
What is a protocol?
Network edge: hosts, access network, 
physical media
Network core: packet/circuit switching, 
internet structure
Performance: loss, delay, throughput
Security
Protocol layers, service models
History
Introduction: 1-79

---

## Page 80

Internet history
▪1961: Kleinrock - queueing 
theory shows effectiveness of 
packet-switching
▪1964: Baran - packet-switching 
in military nets
▪1967: ARPAnet conceived by 
Advanced Research Projects 
Agency
▪1969: first ARPAnet node 
operational
▪1972: 
• ARPAnet public demo
• NCP (Network Control Protocol) 
first host-host protocol 
• first e-mail program
• ARPAnet has 15 nodes
1961-1972: Early packet-switching principles

---

## Page 81

Internet history
Introduction: 1-81
▪1970: ALOHAnet satellite 
network in Hawaii
▪1974: Cerf and Kahn - 
architecture for interconnecting 
networks
▪1976: Ethernet at Xerox PARC
▪late70’s: proprietary 
architectures: DECnet, SNA, XNA
▪1979: ARPAnet has 200 nodes
1972-1980: Internetworking, new and proprietary networks
Cerf and Kahn’s internetworking 
principles:
▪minimalism, autonomy - no 
internal changes required to 
interconnect networks
▪best-effort service model
▪stateless routing
▪decentralized control
define today’s Internet architecture

---

## Page 82

Internet history
Introduction: 1-82
▪1983: deployment of TCP/IP
▪1982: smtp e-mail protocol 
defined 
▪1983: DNS defined for name-
to-IP-address translation
▪1985: ftp protocol defined
▪1988: TCP congestion control
▪new national networks: CSnet, 
BITnet, NSFnet, Minitel
▪100,000 hosts connected to 
confederation of networks
1980-1990: new protocols, a proliferation of networks

---

## Page 83

Internet history
Introduction: 1-83
▪early 1990s: ARPAnet 
decommissioned
▪1991: NSF lifts restrictions on 
commercial use of NSFnet 
(decommissioned, 1995)
▪early 1990s: Web
• hypertext [Bush 1945, Nelson 1960’s]
• HTML, HTTP: Berners-Lee
• 1994: Mosaic, later Netscape
• late 1990s: commercialization of the 
Web
late 1990s – 2000s:
▪more killer apps: instant 
messaging, P2P file sharing
▪network security to forefront
▪est. 50 million host, 100 million+ 
users
▪backbone links running at Gbps
1990, 2000s: commercialization, the Web, new applications

---

## Page 84

Internet history
Introduction: 1-84
▪aggressive deployment of broadband home access (10-100’s Mbps)
▪2008: software-defined networking (SDN)
▪increasing ubiquity of high-speed wireless access: 4G/5G, WiFi
▪service providers (Google, FB, Microsoft) create their own networks
• bypass commercial Internet to connect “close” to end user, providing 
“instantaneous” access to social media, search, video content, …
▪enterprises run their services in “cloud” (e.g., Amazon Web Services, 
Microsoft Azure)
▪rise of smartphones: more mobile than fixed devices on Internet (2017)
▪~18B devices attached to Internet (2017)
2005-present: scale, SDN, mobility, cloud

---

## Page 85

Summary
Introduction: 1-85
We’ve covered a “ton” of material!
▪Internet overview
▪what’s a protocol?
▪network edge, access network, core
• packet-switching versus circuit-
switching
• Internet structure
▪performance: loss, delay, throughput
▪layering, service models
▪security
▪history
You now have: 
▪context, overview, 
vocabulary,  “feel” 
of networking
▪more depth, 
detail, and fun to 
follow!
