# Application Layer

*Extracted from [`Application Layer.pdf`](<../class_materials/Application Layer.pdf>) by `tools/extract_notes.py`.*
*Generated file -- edit the source, not this.*

---

---

## Page 1

Application Layer
Application Layer: 2-1

---

## Page 2

Quiz example 1
What does ISP stand for?
a)
Internet Service Provider
b)
Internet Service Producer
c)
Internet Speed Producer
d)
Incredible Super Powers
Application Layer: 2-2

---

## Page 3

Quiz example 1
What does ISP stand for?
a)
Internet Service Provider
b)
Internet Service Producer
c)
Internet Speed Producer
d)
Incredible Super Powers
Application Layer: 2-3

---

## Page 4

Quiz example 2
What OSI layer routes the data from source to destination?
a)
Transport
b)
Link
c)
Network
d)
Physical
Application Layer: 2-4

---

## Page 5

Quiz example 2
What OSI layer routes the data from source to destination?
a)
Transport
b)
Link
c)
Network
d)
Physical
Application Layer: 2-5

---

## Page 6

Application layer: overview
Application Layer: 2-6
Our goals: 
▪conceptual and 
implementation aspects of 
application-layer protocols
• transport-layer service 
models
• client-server paradigm
• peer-to-peer paradigm
▪learn about protocols by 
examining popular 
application-layer protocols 
and infrastructure
• HTTP
• DNS
• video streaming systems, CDNs
▪programming network 
applications
• socket API

---

## Page 7

Application layer: overview
Application Layer: 2-7
▪Principles of network applications
▪Web and HTTP
▪The Domain Name System DNS
▪P2P applications
▪video streaming and content 
distribution networks
▪socket programming with UDP and 
TCP

---

## Page 8

Some network apps
Application Layer: 2-8
▪Social networking
▪Web
▪text messaging
▪e-mail
▪multi-user network games
▪streaming stored video 
(YouTube, Hulu, Netflix) 
▪P2P file sharing
▪voice over IP (e.g., Skype)
▪real-time video conferencing 
(e.g., Zoom)
▪Internet search
▪remote login
▪…

---

## Page 9

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
application
transport
network
data link
physical
application
transport
network
data link
physical
application
transport
network
data link
physical
Creating a network app
Application Layer: 2-9
Write programs that:
▪Run on (different) end systems
▪Communicate over network
▪e.g., web server software 
communicates with browser software
No need to write software for 
network-core devices
▪network-core devices do not run user 
applications 
▪applications on end systems allow for 
rapid app development, propagation

---

## Page 10

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
Client-server paradigm
Application Layer: 2-10
server: 
▪always-on host
▪permanent IP address
▪often in data centers, for scaling
clients:
▪contact, communicate with server
▪may be intermittently connected
▪may have dynamic IP addresses
▪do not communicate directly with 
each other
▪examples: HTTP, IMAP, FTP

---

## Page 11

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
Peer-peer architecture
Application Layer: 2-11
▪no always-on server
▪arbitrary end systems directly 
communicate
▪peers request service from other 
peers, provide service in return to 
other peers
• self scalability – new peers bring new 
service capacity, as well as new service 
demands
▪peers are intermittently connected 
and change IP addresses
• complex management
▪example: P2P file sharing

---

## Page 12

Processes communicating
Application Layer: 2-12
Process: program running 
within a host
▪within same host, two 
processes communicate 
using inter-process 
communication (defined by 
OS)
▪processes in different hosts 
communicate by exchanging 
messages
▪note: applications with 
P2P architectures have 
client processes & 
server processes
client process: process that 
initiates communication
server process: process 
that waits to be contacted
clients, servers

---

## Page 13

Sockets
Application Layer: 2-13
▪process sends/receives messages to/from its socket
▪socket analogous to door
• sending process shoves message out door
• sending process relies on transport infrastructure on other side of door to 
deliver message to socket at receiving process
• two sockets involved: one on each side
Internet
controlled
by OS
controlled by
app developer
transport
application
physical
link
network
process
transport
application
physical
link
network
process
socket

---

## Page 14

Addressing processes
Application Layer: 2-14
▪to receive messages, process  
must have identifier
▪host device has unique 32-bit 
IP address
▪Q: does IP address of host on 
which process runs suffice for 
identifying the process?
▪identifier includes both IP address and 
port numbers associated with process 
on host.
▪example port numbers:
• HTTP server: 80
• mail server: 25
▪to send HTTP message to 
gaia.cs.uga.edu web server:
• IP address: 128.119.245.12
• port number: 80
▪A: no, many processes 
can be running on 
same host

---

## Page 15

An application-layer protocol defines:
Application Layer: 2-15
▪types of messages exchanged, 
• e.g., request, response 
▪message syntax:
• what fields in messages & how 
fields are delineated
▪message semantics 
• meaning of information in fields
▪rules for when and how processes 
send & respond to messages
open protocols:
▪defined in RFCs, everyone has 
access to protocol definition
▪allows for interoperability
▪e.g., HTTP, SMTP
proprietary protocols:
▪e.g., Skype, Zoom

---

## Page 16

What transport service does an app need?
Application Layer: 2-16
data integrity
▪some apps (e.g., file transfer, 
web transactions) require 
100% reliable data transfer 
▪other apps (e.g., audio) can 
tolerate some loss
timing
▪some apps (e.g., Internet 
telephony, interactive games) 
require low delay to be “effective”
throughput
▪some apps (e.g., multimedia) 
require minimum amount of 
throughput to be “effective”
▪other apps (“elastic apps”) 
make use of whatever 
throughput they get 
security
▪encryption, data integrity…

---

## Page 17

Transport Service Requirements: Common Apps
Application Layer: 2-17
Application
Data loss
Throughput
Time sensitive
File 
Transfer/download
No loss
Elastic
No
E-mail
No loss
Elastic
No
Web Documents
No loss
Elastic
No
Real-time 
audio/video
Loss-tolerant
Audio: 5Kbps-1Mbps
Yes, 10’s msec
Streaming 
audio/video
Loss-tolerant
Audio: 5Kbps-1Mbps
Yes, few sec
Interactive games
Loss-tolerant
Kbps+
Yes, 10’s msec
Text messaging
No loss
Elastic
Yes OR No

---

## Page 18

Internet transport protocols services
Application Layer: 2-18
TCP service:
▪reliable transport between sending 
and receiving process
▪flow control: sender won’t 
overwhelm receiver 
▪congestion control: throttle sender 
when network overloaded
▪connection-oriented: setup required 
between client and server processes
▪does not provide: timing, minimum 
throughput guarantee, security
UDP service:
▪unreliable data transfer 
between sending and receiving 
process
▪does not provide: reliability, 
flow control, congestion 
control, timing, throughput 
guarantee, security, or 
connection setup.
Q: why bother?  Why is there a UDP?

---

## Page 19

Internet transport protocols services
Application Layer: 2-19
TCP service:
▪reliable transport between sending 
and receiving process
▪flow control: sender won’t 
overwhelm receiver 
▪congestion control: throttle sender 
when network overloaded
▪connection-oriented: setup required 
between client and server processes
▪does not provide: timing, minimum 
throughput guarantee, security
UDP service:
▪unreliable data transfer 
between sending and receiving 
process
▪does not provide: reliability, 
flow control, congestion 
control, timing, throughput 
guarantee, security, or 
connection setup.
Q: why bother?  Why is there a UDP?
A: Speed, app handles reliability, 
latency

---

## Page 20

Internet applications, and transport protocols
Application Layer: 2-20
Application
Application Layer Protocol
Transport Protocol
File Transfer/download
FTP [RFC 959]
TCP
E-mail
SMTP [RFC 5321]
TCP
Web Documents
HTTP 1.1 [RFC 7320]
TCP
Real-time audio/video
SIP [RFC 3261], RTP [RFC 3550], 
or proprietary
TCP or UDP
Streaming audio/video
HTTP [RFC 7320], DASH
TCP
Interactive games
WOW, FPS (proprietary) 
TCP or UDP

---

## Page 21

Securing TCP
Application Layer: 2-21
Vanilla TCP & UDP sockets:
▪no encryption
▪cleartext passwords sent into socket 
traverse Internet in cleartext (!)
Transport Layer Security (TLS) 
▪provides encrypted TCP connections
▪data integrity
▪end-point authentication
TSL implemented in 
application layer
▪apps use TSL libraries, that 
use TCP in turn
▪cleartext sent into “socket”  
traverse Internet encrypted

---

## Page 22

Application layer: overview
Application Layer: 2-22
▪Principles of network applications
▪Web and HTTP
▪The Domain Name System DNS
▪P2P applications
▪video streaming and content 
distribution networks
▪socket programming with UDP and 
TCP

---

## Page 23

Web and HTTP
Application Layer: 2-23
First, a quick review…
▪web page consists of objects, each of which can be stored on 
different Web servers
▪object can be HTML file, JPEG image, audio file,…
▪web page consists of base HTML-file which includes several 
referenced objects, each addressable by a URL, e.g.,
www.someschool.edu/someDept/pic.gif
host name
path name

---

## Page 24

HTTP overview
Application Layer: 2-24
HTTP: hypertext transfer protocol
▪Web’s application-layer protocol
▪client/server model:
• client: browser that requests, 
receives, (using HTTP protocol) and 
“displays” Web objects 
• server: Web server sends (using 
HTTP protocol) objects in response 
to requests
iPhone running
Safari browser
PC running
Firefox browser
server running
Apache Web
server

---

## Page 25

HTTP overview (continued)
Application Layer: 2-25
HTTP uses TCP:
▪client initiates TCP connection 
(creates socket) to server,  port 80
▪server accepts TCP connection 
from client
▪HTTP messages (application-layer 
protocol messages) exchanged 
between browser (HTTP client) and 
Web server (HTTP server)
▪TCP connection closed
HTTP is “stateless”
▪server maintains no 
information about past client 
requests
protocols that maintain “state” 
are complex!
▪past history (state) must be 
maintained
▪if server/client crashes, their views 
of “state” may be inconsistent, 
must be reconciled
aside

---

## Page 26

HTTP connections: two types
Application Layer: 2-26
Non-persistent HTTP
1. TCP connection opened
2. at most one object sent 
over TCP connection
3. TCP connection closed
downloading multiple 
objects required multiple 
connections
Persistent HTTP
▪TCP connection opened to 
a server
▪multiple objects can be 
sent over single TCP 
connection between client, 
and that server
▪TCP connection closed

---

## Page 27

Non-persistent HTTP: example
Application Layer: 2-27
User enters URL:
1a. HTTP client initiates TCP 
connection to HTTP server 
(process) at www.someSchool.edu on 
port 80
2. HTTP client sends HTTP 
request message (containing 
URL) into TCP connection 
socket. Message indicates 
that client wants object 
someDepartment/home.index
1b. HTTP server at host 
www.someSchool.edu waiting for TCP 
connection at port 80  “accepts” 
connection, notifying client
3. HTTP server receives request message, 
forms response message containing 
requested object, and sends message 
into its socket
time
(containing text, references to 10 jpeg images)
https://daytonabeach.erau.edu/-
/media/images/university/degree-images/masters-
unmanned-autonomous-systems-engineering.jpg

---

## Page 28

Non-persistent HTTP: example (cont.)
Application Layer: 2-28
5. HTTP client receives response 
message containing html file, 
displays html.  Parsing html file, 
finds 10 referenced jpeg  objects
6. Steps 1-5 repeated for 
each of 10 jpeg objects
4. HTTP server closes TCP 
connection. 
time
User enters URL:
(containing text, references to 10 jpeg images)
https://daytonabeach.erau.edu/-
/media/images/university/degree-images/masters-
unmanned-autonomous-systems-engineering.jpg

---

## Page 29

Non-persistent HTTP: response time
Application Layer: 2-29
RTT (definition): time for a small 
packet to travel from client to 
server and back
HTTP response time (per object):
▪one RTT to initiate TCP connection
▪one RTT for HTTP request and first few 
bytes of HTTP response to return
▪object/file transmission time
time to 
transmit 
file
initiate TCP
connection
RTT
request file
RTT
file received
time
time
Non-persistent HTTP response time =  2RTT+ file transmission time

---

## Page 30

Persistent HTTP (HTTP 1.1)
Application Layer: 2-30
Non-persistent HTTP issues:
▪requires 2 RTTs per object
▪OS overhead for each TCP 
connection
▪browsers often open multiple 
parallel TCP connections to 
fetch referenced objects in 
parallel
Persistent  HTTP (HTTP1.1):
▪server leaves connection open after 
sending response
▪subsequent HTTP messages between 
same client/server sent over open 
connection
▪client sends requests as soon as it 
encounters a referenced object
▪as little as one RTT for all the referenced 
objects (cutting response time in half)

---

## Page 31

HTTP request message
Application Layer: 2-31
▪two types of HTTP messages: request, response
▪HTTP request message:
• ASCII (human-readable format)
header
 lines
GET /index.html HTTP/1.1\r\n
Host: www-net.cs.uga.edu\r\n
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 
10.15; rv:80.0) Gecko/20100101 Firefox/80.0 \r\n
Accept: text/html,application/xhtml+xml\r\n
Accept-Language: en-us,en;q=0.5\r\n
Accept-Encoding: gzip,deflate\r\n
Connection: keep-alive\r\n
\r\n
carriage return character
line-feed character
request line (GET, POST, 
HEAD commands)
carriage return, line feed 
at start of line indicates 
end of header lines

---

## Page 32

HTTP request message: general format
Application Layer: 2-32
request
line
header
lines
body
method
sp
sp
cr
lf
version
URL
cr
lf
value
header field name
cr
lf
value
header field name
~~
~~
cr
lf
entity body
~~
~~

---

## Page 33

Other HTTP request messages
Application Layer: 2-33
POST method:
▪web page often includes form 
input
▪user input sent from client to 
server in entity body of HTTP 
POST request message
GET method (for sending data to server):
▪include user data in URL field of HTTP 
GET request message (following a ‘?’):
www.somesite.com/animalsearch?monkeys&banana
HEAD method:
▪requests headers (only) that 
would be returned if specified 
URL were requested with an HTTP 
GET method. 
PUT method:
▪uploads new file (object) to server
▪completely replaces file that exists 
at specified URL with content in 
entity body of PUT HTTP request 
message

---

## Page 34

HTTP response message
Application Layer: 2-34
status line (protocol
status code status phrase)
header
 lines
data, e.g.,  requested
HTML file
HTTP/1.1 200 OK
Date: Tue, 08 Sep 2020 00:53:20 GMT
Server: Apache/2.4.6 (CentOS) 
OpenSSL/1.0.2k-fips PHP/7.4.9 
mod_perl/2.0.11 Perl/v5.16.3
Last-Modified: Tue, 01 Mar 2016 18:57:50 GMT
ETag: "a5b-52d015789ee9e"
Accept-Ranges: bytes
Content-Length: 2651
Content-Type: text/html; charset=UTF-8
\r\n
data data data data data ...

---

## Page 35

HTTP response status codes
Application Layer: 2-35
200 OK
• request succeeded, requested object later in this message
301 Moved Permanently
• requested object moved, new location specified later in this message (in Location: field)
400 Bad Request
• request msg not understood by server
404 Not Found
• requested document not found on this server
505 HTTP Version Not Supported
▪status code appears in 1st line in server-to-client response message.
▪some sample codes:

---

## Page 36

Maintaining user/server state: cookies
Application Layer: 2-36
Recall: HTTP GET/response interaction 
is stateless
▪no notion of multi-step exchanges of HTTP 
messages to complete a Web “transaction” 
• no need for client/server to track “state” of 
multi-step exchange
• all HTTP requests are independent of each other
• no need for client/server to “recover” from a 
partially-completed-but-never-completely-
completed transaction
a stateful protocol: client makes 
two changes to X, or none at all
time
time
X
X
X’
X’’
X’’
t’
Q: what happens if network connection or client crashes at t’ ?

---

## Page 37

Maintaining user/server state: cookies
Application Layer: 2-37
Web sites and client browser use cookies 
to maintain some state between 
transactions
four components:
1) cookie header line of HTTP response 
message
2) cookie header line in next HTTP request 
message
3) cookie file kept on user’s host, managed by 
user’s browser
4) back-end database at Web site
Example:
▪Susan uses browser on laptop, visits 
specific e-commerce site for first 
time
▪when initial HTTP requests arrives at 
site, site creates: 
• unique ID (aka “cookie”)
• entry in backend database for ID
• subsequent HTTP requests from 
Susan to this site will contain cookie 
ID value, allowing site to “identify” 
Susan

---

## Page 38

Maintaining user/server state: cookies
Application Layer: 2-38
client
server
usual HTTP response msg
usual HTTP response msg
cookie file
one week later:
usual HTTP request msg
cookie: 1678
cookie-
specific
action
access
ebay 8734
usual HTTP request msg
Amazon server
creates ID
1678 for user
create
    entry
usual HTTP response 
set-cookie: 1678 
ebay 8734
amazon 1678
usual HTTP request msg
cookie: 1678
cookie-
specific
action
access
ebay 8734
amazon 1678
backend
database
time
time

---

## Page 39

HTTP cookies: comments
Application Layer: 2-39
What cookies can be used for:
▪authorization
▪shopping carts
▪recommendations
▪user session state (Web e-mail)
cookies and privacy:
▪cookies permit sites to 
learn a lot about you on 
their site.
▪third party persistent 
cookies (tracking cookies) 
allow common identity 
(cookie value) to be 
tracked across multiple 
web sites
aside
Challenge: How to keep state?
▪at protocol endpoints: maintain state at 
sender/receiver over multiple 
transactions
▪in messages: cookies in HTTP messages 
carry state

---

## Page 40

Web caches
Application Layer: 2-40
▪user configures browser to 
point to a (local) Web cache
▪browser sends all HTTP 
requests to cache
• if object in cache: cache 
returns object to client
• else cache requests object 
from origin server, caches 
received object, then 
returns object to client
Goal: satisfy client requests without involving origin server
client
Web 
cache
client
origin 
server

---

## Page 41

Web caches (aka proxy servers)
Application Layer: 2-41
▪Web cache acts as both 
client and server
• server for original 
requesting client
• client to origin server
Why Web caching?
▪reduce response time for client 
request 
• cache is closer to client
▪reduce traffic on an institution’s 
access link
▪Internet is dense with caches 
• enables “poor” content providers 
to more effectively deliver content
▪server tells cache about 
object’s allowable caching in 
response header:

---

## Page 42

Caching example
Application Layer: 2-42
origin
servers
public
 Internet
institutional
network
1 Gbps LAN
1.54 Mbps 
access link
Performance:
▪access link utilization = .974
▪LAN utilization: .0015
▪end-end delay  =  Internet delay +
                                     access link delay + LAN delay 
                                 =  2 sec + minutes + μsec
Scenario:
▪access link rate: 1.54 Mbps
▪RTT from institutional router to server: 2 sec
▪web object size: 100K bits
▪average request rate from browsers to origin 
servers: 15/sec
▪avg data rate to browsers: 1.50 Mbps
problem: large 
queueing delays 
at high utilization!

---

## Page 43

Performance:
▪access link utilization = .97
▪LAN utilization: .0015
▪end-end delay  =  Internet delay +
                                     access link delay + LAN delay 
                                 =  2 sec + minutes + usecs
Option 1: buy a faster access link
Application Layer: 2-43
origin
servers
public
 Internet
institutional
network
1 Gbps LAN
1.54 Mbps 
access link
Scenario:
▪access link rate: 1.54 Mbps
▪RTT from institutional router to server: 2 sec
▪web object size: 100K bits
▪average request rate from browsers to origin 
servers: 15/sec
▪avg data rate to browsers: 1.50 Mbps
154 Mbps
154 Mbps
.0097
msecs
Cost: faster access link (expensive!)

---

## Page 44

Performance:
▪LAN utilization: .?
▪access link utilization = ?
▪average end-end delay  = ? 
Option 2: install a web cache
Application Layer: 2-44
origin
servers
public
 Internet
institutional
network
1 Gbps LAN
1.54 Mbps 
access link
Scenario:
▪access link rate: 1.54 Mbps
▪RTT from institutional router to server: 2 sec
▪web object size: 100K bits
▪average request rate from browsers to origin 
servers: 15/sec
▪avg data rate to browsers: 1.50 Mbps
How to compute link 
utilization, delay?
Cost: web cache (cheap!)
local web cache

---

## Page 45

Calculating access link utilization, end-end delay 
with cache:
Application Layer: 2-45
origin
servers
public
 Internet
institutional
network
1 Gbps LAN
1.54 Mbps 
access link
local web cache
suppose cache hit rate is 0.4:  
▪40% requests served by cache, with low 
(msec) delay 
▪60% requests satisfied at origin 
•  rate to browsers over access link 
       = 0.6 * 1.50 Mbps  =  .9 Mbps 
• access link utilization = 0.9/1.54 = .58 means 
low (msec) queueing delay at access link
▪average end-end delay:
= 0.6 * (delay from origin servers)
           + 0.4 * (delay when satisfied at cache)
= 0.6 (2.XX) + 0.4 (~msecs) = ~ 1.2 secs
lower average end-end delay than with 154 Mbps link (and cheaper too!)

---

## Page 46

Conditional GET
Application Layer: 2-46
Goal: don’t send object if cache has 
up-to-date cached version
• no object transmission delay (or use 
of network resources)
▪client: specify date of cached copy 
in HTTP request
If-modified-since: <date>
▪server: response contains no 
object if cached copy is up-to-date: 
HTTP/1.0 304 Not Modified
HTTP request msg
If-modified-since: <date>
HTTP response
HTTP/1.0 
304 Not Modified
object 
not 
modified
after
<date>
HTTP request msg
If-modified-since: <date>
HTTP response
HTTP/1.0 200 OK
<data>
object 
modified
after 
<date>
client
server

---

## Page 47

HTTP/2
Application Layer: 2-47
Key goal: decreased delay in multi-object HTTP requests
HTTP1.1: introduced multiple, pipelined GETs over single TCP 
connection
▪server responds in-order (FCFS: first-come-first-served scheduling) to 
GET requests
▪with FCFS, small object may have to wait for transmission (head-of-
line (HOL) blocking) behind large object(s)
▪loss recovery (retransmitting lost TCP segments) stalls object 
transmission

---

## Page 48

HTTP/2
Application Layer: 2-48
HTTP/2: [RFC 7540, 2015] increased flexibility at server in sending 
objects to client:
▪methods, status codes, most header fields unchanged from HTTP 1.1
▪transmission order of requested objects based on client-specified 
object priority (not necessarily FCFS)
▪push unrequested objects to client
▪divide objects into frames, schedule frames to mitigate HOL blocking
Key goal: decreased delay in multi-object HTTP requests

---

## Page 49

HTTP/2: mitigating HOL blocking
Application Layer: 2-49
HTTP 1.1: client requests 1 large object (e.g., video file) and 3 smaller 
objects
client
server
GET O1
GET O2
GET O3
GET O4
O1 O2
O3O4
object data requested
O1
O2
O3
O4
objects delivered in order requested: O2, O3, O4 wait behind O1

---

## Page 50

HTTP/2: mitigating HOL blocking
Application Layer: 2-50
HTTP/2: objects divided into frames, frame transmission interleaved
client
server
GET O1
GET O2
GET O3
GET O4
O2
O4
object data requested
O1
O2
O3
O4
O2, O3, O4 delivered quickly, O1 slightly delayed
O3
O1

---

## Page 51

HTTP/2 to HTTP/3
Application Layer: 2-51
HTTP/2 over single TCP connection means:
▪recovery from packet loss still stalls all object transmissions
• as in HTTP 1.1, browsers have incentive to open multiple parallel 
TCP connections to reduce stalling, increase overall throughput
▪no security over vanilla TCP connection
▪HTTP/3: adds security, per object error- and congestion-
control (more pipelining) over UDP
• more on HTTP/3 in transport layer

---

## Page 52

Application layer: overview
Application Layer: 2-52
▪Principles of network applications
▪Web and HTTP
▪The Domain Name System DNS
▪P2P applications
▪video streaming and content 
distribution networks
▪socket programming with UDP and 
TCP

---

## Page 53

DNS: Domain Name System
Application Layer: 2-53
people: many identifiers:
• SSN, name, passport #
Internet hosts, routers:
• IP address (32 bit) - used for 
addressing datagrams
• “name”, e.g., cs.uga.edu - used 
by humans
Q: how to map between IP 
address and name, and vice 
versa ?
Domain Name System (DNS):
▪distributed database implemented in 
hierarchy of many name servers
▪application-layer protocol: hosts, DNS 
servers communicate to resolve 
names (address/name translation)
• note: core Internet function, 
implemented as application-layer 
protocol
• complexity at network’s “edge”

---

## Page 54

DNS: services, structure
Application Layer: 2-54
DNS services:
▪hostname-to-IP-address translation
▪host aliasing
• canonical, alias names
▪mail server aliasing
▪load distribution
• replicated Web servers: many IP 
addresses correspond to one 
name

---

## Page 55

DNS: services, structure
Application Layer: 2-55
Q: Why not centralize DNS?
▪single point of failure
▪traffic volume
▪distant centralized database
▪maintenance
A: doesn‘t scale!
▪Comcast DNS servers alone: 
600B DNS queries/day
▪Akamai DNS servers alone: 
2.2T DNS queries/day
Centralized
Distributed

---

## Page 56

Thinking about the DNS
Application Layer: 2-56
humongous distributed database:
▪~ billion records, each simple
handles many trillions of queries/day:
▪many more reads than writes
▪performance matters: almost every 
Internet transaction interacts with 
DNS - msecs count!
organizationally, physically decentralized:
▪millions of different organizations 
responsible for their records
“bulletproof”: reliability, security

---

## Page 57

DNS: a distributed, hierarchical database
Application Layer: 2-57
Client wants IP address for www.amazon.com; 1st approximation:
▪client queries root server to find .com DNS server
▪client queries .com DNS server to get amazon.com DNS server
▪client queries amazon.com DNS server to get  IP address for www.amazon.com
.com DNS servers
.org DNS servers
.edu DNS servers
…
…
Top Level Domain
Root DNS Servers
Root
erau.edu
DNS servers
uga.edu
DNS servers
yahoo.com
DNS servers
amazon.com
DNS servers
pbs.org
DNS servers
Authoritative
…
…
…
…

---

## Page 58

DNS: root name servers
Application Layer: 2-58
▪official, contact-of-last-resort by 
name servers that can not 
resolve name

---

## Page 59

DNS: root name servers
Application Layer: 2-59
▪official, contact-of-last-resort by 
name servers that can not 
resolve name
▪incredibly important Internet 
function
• Internet couldn’t function without it!
• DNSSEC – provides security 
(authentication, message integrity)
▪ICANN (Internet Corporation for 
Assigned Names and Numbers) 
manages root DNS domain
13 logical root name “servers” 
worldwide each “server” replicated 
many times (~200 servers in US)

---

## Page 60

Top-Level Domain, and authoritative servers
Application Layer: 2-60
Top-Level Domain (TLD) servers:
▪responsible for .com, .org, .net, .edu, .aero, .jobs, .museums, and all top-level 
country domains, e.g.: .cn, .uk, .fr, .ca, .jp
▪Verisign : authoritative registry for .com, .net TLD
▪Educause: .edu TLD
authoritative DNS servers: 
▪organization’s own DNS server(s), providing authoritative hostname to IP 
mappings for organization’s named hosts 
▪can be maintained by organization or service provider

---

## Page 61

Local DNS name servers
Application Layer: 2-61
▪when host makes DNS query, it is sent to its local DNS server
• Local DNS server returns reply, answering:
• from its local cache of recent name-to-address translation pairs (possibly out 
of date!)
• forwarding request into DNS hierarchy for resolution
• each ISP has local DNS name server; to find yours: 
• MacOS: % scutil --dns
• Windows: >ipconfig /all
▪local DNS server doesn’t strictly belong to hierarchy

---

## Page 62

DNS name resolution: iterated query
Application Layer: 2-62
Example: host at engineering.erau.edu 
wants IP address for gaia.cs.uga.edu
Iterated query:
▪contacted server replies 
with name of server to 
contact
▪“I don’t know this name, 
but ask this server”
requesting host at
engineering.erau.edu
gaia.cs.uga.edu
root DNS server
local DNS server
dns.erau.edu
1
2
3
4
5
6
authoritative DNS server
dns.cs.uga.edu
7
8
TLD DNS server

---

## Page 63

DNS name resolution: recursive query
Application Layer: 2-63
requesting host at
engineering.erau.edu
gaia.cs.uga.edu
root DNS server
local DNS server
dns.erau.edu
1
2
3
4
5
6
authoritative DNS server
dns.cs.uga.edu
7
8
TLD DNS server
Recursive query:
▪puts burden of name 
resolution on 
contacted name 
server
▪heavy load at upper 
levels of hierarchy?
Example: host at engineering.erau.edu 
wants IP address for gaia.cs.uga.edu

---

## Page 64

Caching DNS Information
Application Layer: 2-64
▪once (any) name server learns mapping, it caches mapping, 
and immediately returns a cached mapping in response to a 
query
• caching improves response time
• cache entries timeout (disappear) after some time (TTL)
• TLD servers typically cached in local name servers
▪cached entries may be out-of-date
• if named host changes IP address, may not be known Internet-
wide until all TTLs expire!
• best-effort name-to-address translation!

---

## Page 65

DNS records
Application Layer: 2-65
DNS: distributed database storing resource records (RR)
type=NS
▪name is domain (e.g., foo.com)
▪value is hostname of 
authoritative name server for 
this domain (e.g., dns.foo.com)
RR format: (name, value, type, ttl)
type=A
▪name is hostname
▪value is IP address
type=CNAME
▪name is alias name for some “canonical” 
(the real) name
▪www.ibm.com is really servereast.backup2.ibm.com
▪value is canonical name
type=MX
▪value is name of SMTP mail 
server associated with name
E.g., (relay1.bar.foo.com, 145.37.93.126, A, 300)
E.g., (foo.com, dns.foo.com, NS, 300)
E.g., (ibm.com, servereast.backup2.ibm.com, CNAME, 300)
E.g., (foo.com, mail.bar.foo.com, MX, 300)

---

## Page 66

identification
flags
# questions
questions (variable # of questions)
# additional RRs
# authority RRs
# answer RRs
answers (variable # of RRs)
authority (variable # of RRs)
additional info (variable # of RRs)
2 bytes
2 bytes
DNS protocol messages
Application Layer: 2-66
DNS query and reply messages, both have same format:
message header:
▪identification: 16 bit # for query, 
reply to query uses same #
▪flags:
• query or reply
• recursion desired 
• recursion available
• reply is authoritative

---

## Page 67

identification
flags
# questions
questions (variable # of questions)
# additional RRs
# authority RRs
# answer RRs
answers (variable # of RRs)
authority (variable # of RRs)
additional info (variable # of RRs)
2 bytes
2 bytes
DNS query and reply messages, both have same  format:
name, type fields for a query
RRs in response to query
records for authoritative servers
additional “ helpful” info that may 
be used
DNS protocol messages
Application Layer: 2-67

---

## Page 68

Getting your info into the DNS
Application Layer: 2-68
example: new startup “Network Utopia”
▪register name networkutopia.com at DNS registrar (e.g., Network 
Solutions)
• provide names, IP addresses of authoritative name server (primary and 
secondary)
• registrar inserts NS, A RRs into .com TLD server:
 (networkutopia.com, dns1.networkutopia.com, NS)
 (dns1.networkutopia.com, 212.212.212.1, A)
▪create authoritative server locally with IP address 212.212.212.1
• type A record for www.networkuptopia.com
• type MX record for networkutopia.com

---

## Page 69

DNS security
Application Layer: 2-69
DDoS attacks
▪bombard root servers with 
traffic
• not successful to date
• traffic filtering
• local DNS servers cache IPs of TLD 
servers, allowing root server 
bypass
▪bombard TLD servers
• potentially more dangerous
Spoofing attacks
▪intercept DNS queries, 
returning bogus replies
▪DNS cache poisoning
▪RFC 4033: DNSSEC 
authentication services

---

## Page 70

Application layer: overview
Application Layer: 2-70
▪Principles of network applications
▪Web and HTTP
▪The Domain Name System DNS
▪P2P applications
▪video streaming and content 
distribution networks
▪socket programming with UDP and 
TCP

---

## Page 71

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
Peer-to-peer (P2P) architecture
Application Layer: 2-71
▪no always-on server
▪arbitrary end systems directly communicate
▪peers request service from other peers, 
provide service in return to other peers
• self scalability – new peers bring new service 
capacity, and new service demands
▪peers are intermittently connected and 
change IP addresses
• complex management
▪examples: P2P file sharing (BitTorrent), streaming 
(KanKan), VoIP (Skype)

---

## Page 72

File distribution: client-server vs P2P
Introduction: 1-72
Q: how much time to distribute file (size F) from one server to N peers?
• peer upload/download capacity is limited resource
us
uN
dN
server
network (with abundant
 bandwidth)
file, size F
us: server upload 
capacity
ui: peer i upload 
capacity
di: peer i download 
capacity
u2
d2
u1
d1
di
ui

---

## Page 73

File distribution time: client-server
Introduction: 1-73
▪server transmission: must sequentially 
send (upload) N file copies:
• time to send one copy: F/us 
• time to send N copies: NF/us
▪client: each client must 
download file copy
• dmin = min client 
download rate
• min client download 
time: F/dmin 
us
network
di
ui
F
increases linearly in N
time to  distribute F 
to N clients using 
client-server approach Dcs > max{NF/us,,F/dmin}

---

## Page 74

File distribution time: P2P
Application Layer: 2-74
▪server transmission: must upload at 
least one copy:
• time to send one copy: F/us 
▪client: each client must download file copy
• min client download time: F/dmin 
us
network
di
ui
F
▪clients: as aggregate must download NF bits
• max upload rate (limiting max download rate) is us + ui
time to  distribute F 
to N clients using 
P2P approach 
DP2P > max{F/us,,F/dmin,,NF/(us + ui)} 
… but so does this, as each peer brings service capacity
increases linearly in N …

---

## Page 75

Client-server vs. P2P: example
Application Layer: 2-75
client upload rate = u,  F/u = 1 hour,  us = 10u,  dmin ≥ us
0
0.5
1
1.5
2
2.5
3
3.5
0
5
10
15
20
25
30
35
N
Minimum Distribution Time
P2P
Client-Server

---

## Page 76

P2P file distribution: BitTorrent 
Application Layer: 2-76
▪file divided 
into 256Kb 
chunks
▪peers in 
torrent 
send/receive 
file chunks
tracker: tracks 
peers 
participating in 
torrent
torrent: group of peers 
exchanging chunks of a 
file
Alice arrives
•
obtains list of 
peers from 
tracker and 
begins 
exchanging 
•
file chunks with 
peers in torrent

---

## Page 77

P2P file distribution: BitTorrent 
Application Layer: 2-77
▪peer joining torrent: 
• has no chunks, but will accumulate them 
over time from other peers
• registers with tracker to get list of peers, 
connects to subset of peers 
(“neighbors”)
▪while downloading, peer uploads chunks to other peers
▪peer may change peers with whom it exchanges chunks
▪churn: peers may come and go
▪once peer has entire file, it may (selfishly) leave or (altruistically) remain 
in torrent

---

## Page 78

BitTorrent: requesting, sending file chunks
Application Layer: 2-78
Requesting chunks:
▪at any given time, different 
peers have different 
subsets of file chunks
▪periodically, Alice asks 
each peer for list of chunks 
that they have
▪Alice requests missing 
chunks from peers, rarest 
first
Sending chunks: tit-for-tat
▪Alice sends chunks to those four 
peers currently sending her chunks 
at highest rate 
• other peers are choked by Alice (do 
not receive chunks from her)
• re-evaluate top 4 every 10 secs
▪every 30 secs: randomly select 
another peer, starts sending 
chunks
• “optimistically unchoke” this peer
• newly chosen peer may join top 4

---

## Page 79

BitTorrent: tit-for-tat
Application Layer: 2-79
(1) Alice “optimistically unchokes” Bob
(2) Alice becomes one of Bob’s top-four providers; Bob reciprocates
(3) Bob becomes one of Alice’s top-four providers
higher upload rate: find better trading 
partners, get file faster !

---

## Page 80

Application layer: overview
Application Layer: 2-80
▪Principles of network applications
▪Web and HTTP
▪The Domain Name System DNS
▪P2P applications
▪video streaming and content 
distribution networks
▪socket programming with UDP and 
TCP

---

## Page 81

Video Streaming and CDNs: context
Application Layer: 2-81
▪stream video traffic: major 
consumer of Internet bandwidth
• Netflix, YouTube, Amazon Prime: 80% of 
residential ISP traffic (2020)
▪challenge:  scale - how to reach 
~1B users?
▪challenge: heterogeneity
▪different users have different capabilities (e.g., wired 
versus mobile; bandwidth rich versus bandwidth poor)
▪solution: distributed, application-level infrastructure

---

## Page 82

Multimedia: video
Application Layer: 2-82
▪video: sequence of images 
displayed at constant rate
• e.g., 24 images/sec
▪digital image: array of pixels
• each pixel represented by bits
▪coding: use redundancy within and 
between images to decrease # bits 
used to encode image
• spatial (within image)
• temporal (from one image to 
next)
……………………..
spatial coding example: instead 
of sending N values of same 
color (all purple), send only two 
values: color value (purple) and 
number of repeated values (N)
……………….…….
frame i
frame i+1
temporal coding example: 
instead of sending 
complete frame at i+1, 
send only differences from 
frame i

---

## Page 83

Multimedia: video
Application Layer: 2-83
……………………..
spatial coding example: instead 
of sending N values of same 
color (all purple), send only two 
values: color  value (purple)  and 
number of repeated values (N)
……………….…….
frame i
frame i+1
temporal coding example: 
instead of sending 
complete frame at i+1, 
send only differences from 
frame i
▪CBR: (constant bit rate): video 
encoding rate fixed
▪VBR: (variable bit rate): video 
encoding rate changes as amount of 
spatial, temporal coding changes 
▪examples:
• MPEG1 (CD-ROM) 1.5 Mbps
• MPEG2 (DVD) 3-6 Mbps
• MPEG4 (often used in Internet,  
64Kbps – 12 Mbps)

---

## Page 84

Streaming stored video
Main challenges: 
server-to-client bandwidth will vary over time, with changing network congestion levels (in house, 
access network, network core, video server)
packet loss, delay due to congestion will delay playout, or result in poor video quality
Application Layer: 2-84
simple scenario:
video server
(stored video)
client
Internet

---

## Page 85

Streaming stored video
Application Layer: 2-85
1. video
recorded 
(e.g., 30 
frames/sec)
2. video
sent
streaming: Client playing out early part of 
video, while server still sending later part of 
video
time
3. video received, played out at client
(30 frames/sec)
network delay
(fixed in this 
example)

---

## Page 86

Streaming stored video: challenges
Application Layer: 2-86
▪continuous playout constraint: during client 
video playout, playout timing must match 
original timing 
• … but network delays are variable (jitter), so will 
need client-side buffer to match continuous playout 
constraint
▪other challenges:
• client interactivity: pause, fast-forward, rewind, 
jump through video
• video packets may be lost, retransmitted

---

## Page 87

Streaming stored video: playout buffering
Application Layer: 2-87
constant bit 
      rate video
transmission
time
variable
network
delay
client video
reception
constant bit 
     rate video
 playout at client
client playout
delay
buffered
video
▪client-side buffering and playout delay: compensate for 
network-added delay, delay jitter

---

## Page 88

Streaming multimedia: DASH
Application Layer: 2-88
server:
▪divides video file into multiple chunks
▪each chunk encoded at multiple different rates
▪different rate encodings stored in different files
▪files replicated in various CDN nodes
▪manifest file: provides URLs for different chunks
client
?
client:
▪periodically estimates server-to-client bandwidth
▪consulting manifest, requests one chunk at a time 
• chooses maximum coding rate sustainable given current bandwidth
• can choose different coding rates at different points in time (depending 
on available bandwidth at time), and from different servers
...
...
...
Dynamic, Adaptive 
Streaming over HTTP

---

## Page 89

...
...
...
Streaming multimedia: DASH
Application Layer: 2-89
▪“intelligence” at client: client 
determines
• when to request chunk (so that buffer 
starvation, or overflow does not occur)
• what encoding rate to request (higher 
quality when more bandwidth 
available) 
• where to request chunk (can request 
from URL server that is “close” to client 
or has high available bandwidth) 
Streaming video = encoding + DASH + playout buffering
client
?

---

## Page 90

Content distribution networks (CDNs)
Application Layer: 2-90
challenge: how to stream content (selected from millions of 
videos) to hundreds of thousands of simultaneous users?
▪option 1: single, large “mega-server”
• single point of failure
• point of network congestion
• long (and possibly congested) path to 
distant clients
….quite simply: this solution doesn’t scale

---

## Page 91

Content distribution networks (CDNs)
Application Layer: 2-91
challenge: how to stream content (selected from millions of 
videos) to hundreds of thousands of simultaneous users?
• enter deep: push CDN servers deep into many access networks 
• close to users
• Akamai: 240,000 servers deployed 
   in > 120 countries (2015)
▪option 2: store/serve multiple copies of videos at multiple 
geographically distributed sites (CDN)
• bring home: smaller number (10’s) of 
larger clusters in IXPs near access nets
• used by Limelight

---

## Page 92

Content distribution networks (CDNs)
▪subscriber requests content, service provider returns manifest
Application Layer: 2-92
▪CDN: stores copies of content (e.g. MADMEN) at CDN nodes 
where’s Madmen?
manifest file
• using manifest, client retrieves content at highest supportable rate
• may choose different rate or copy if network path congested

---

## Page 93

Internet host-host communication as a service
Content distribution networks (CDNs)
OTT challenges: coping with a congested Internet from the “edge”
▪what content to place in which CDN node?
▪from which CDN node to retrieve content? At which rate?
Application Layer: 2-93
OTT: “over the top”

---

## Page 94

Application layer: overview
Application Layer: 2-94
▪Principles of network applications
▪Web and HTTP
▪The Domain Name System DNS
▪P2P applications
▪video streaming and content 
distribution networks
▪socket programming with UDP and 
TCP

---

## Page 95

Socket programming 
Application Layer: 2-95
goal: learn how to build client/server applications that 
communicate using sockets
socket: door between application process and end-end-transport 
protocol 
Internet
controlled
by OS
controlled by
app developer
transport
application
physical
link
network
process
transport
application
physical
link
network
process
socket

---

## Page 96

Socket programming 
Two socket types for two transport services:
▪UDP: unreliable datagram 
▪TCP: reliable, byte stream-oriented
Application Layer: 2-96
Application Example:
1. client reads a line of characters (data) from its keyboard and sends 
data to server
2. server receives the data and converts characters to uppercase
3. server sends modified data to client
4. client receives modified data and displays line on its screen

---

## Page 97

Socket programming with UDP 
UDP: no “connection” between client 
and server:
no handshaking before sending data
sender explicitly attaches IP destination address and port 
# to each packet
receiver extracts sender IP address and port# from 
received packet
Application Layer: 2-97
UDP: transmitted data may be lost or received out-of-order
Application viewpoint:
▪UDP provides unreliable transfer  of groups of bytes (“datagrams”)  
between client and server processes

---

## Page 98

Client/server socket interaction: UDP
Application Layer: 2-98
close
clientSocket
read datagram from
clientSocket
create socket:
clientSocket =
socket(AF_INET,SOCK_DGRAM)
Create datagram with serverIP address
And port=x; send datagram via
clientSocket
create socket, port= x:
serverSocket =
socket(AF_INET,SOCK_DGRAM)
read datagram from
serverSocket
write reply to
serverSocket
specifying 
client address,
port number
server (running on serverIP)
client

---

## Page 99

Example app: UDP client
Application Layer: 2-99
from socket import *
serverName = ‘hostname’
serverPort = 12000
clientSocket = socket(AF_INET, 
                                   SOCK_DGRAM)
message = raw_input(’Input lowercase sentence:’)
clientSocket.sendto(message.encode(),
                                      (serverName, serverPort))
modifiedMessage, serverAddress = 
                                   clientSocket.recvfrom(2048)
print modifiedMessage.decode()
clientSocket.close()
Python UDPClient
include Python’s socket library
create UDP socket for server
get user keyboard input 
attach server name, port to message; send into socket
print out received string and close socket
read reply characters from socket into string

---

## Page 100

Example app: UDP server
Application Layer: 2-100
Python UDPServer
from socket import *
serverPort = 12000
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('', serverPort))
print (“The server is ready to receive”)
while True:
    message, clientAddress = serverSocket.recvfrom(2048)
    modifiedMessage = message.decode().upper()
    serverSocket.sendto(modifiedMessage.encode(),
                                      clientAddress)
create UDP socket
bind socket to local port number 12000
loop forever
Read from UDP socket into message, getting 
client’s address (client IP and port)
send upper case string back to this client

---

## Page 101

Socket programming with TCP
Client must contact server
server process must first be running
server must have created socket 
(door) that welcomes client’s contact
Client contacts server by:
Creating TCP socket, specifying IP 
address, port number of server 
process
when client creates socket: client TCP 
establishes connection to server TCP
Application Layer: 2-101
▪when contacted by client, server 
TCP creates new socket for server 
process to communicate with that 
particular client
• allows server to talk with multiple 
clients
• source port numbers used to 
distinguish clients (more in Chap 3)
TCP provides reliable, in-order
byte-stream transfer (“pipe”) 
between client and server 
processes
Application viewpoint

---

## Page 102

Client/server socket interaction: TCP
Application Layer: 2-102
server (running on hostid)
client
wait for incoming
connection request
connectionSocket =
serverSocket.accept()
create socket,
port=x, for incoming 
request:
serverSocket = socket()
create socket,
connect to hostid, port=x
clientSocket = socket()
send request using
clientSocket
read request from
connectionSocket
write reply to
connectionSocket
TCP 
connection setup
close
connectionSocket
read reply from
clientSocket
close
clientSocket

---

## Page 103

Example app: TCP client
Application Layer: 2-103
from socket import *
serverName = ’servername’
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName,serverPort))
sentence = raw_input(‘Input lowercase sentence:’)
clientSocket.send(sentence.encode())
modifiedSentence = clientSocket.recv(1024)
print (‘From Server:’, modifiedSentence.decode())
clientSocket.close()
Python TCPClient
create TCP socket for server, 
remote port 12000
No need to attach server name, port

---

## Page 104

Example app: TCP server
Application Layer: 2-104
from socket import *
serverPort = 12000
serverSocket = socket(AF_INET,SOCK_STREAM)
serverSocket.bind((‘’,serverPort))
serverSocket.listen(1)
print ‘The server is ready to receive’
while True:
     connectionSocket, addr = serverSocket.accept()
     
     sentence = connectionSocket.recv(1024).decode()
     capitalizedSentence = sentence.upper()
     connectionSocket.send(capitalizedSentence.
                                                            encode())
     connectionSocket.close()
Python TCPServer
create TCP welcoming socket
server begins listening for  
incoming TCP requests
loop forever
server waits on accept() for incoming 
requests, new socket created on return
read bytes from socket (but 
not address as in UDP)
close connection to this client (but not 
welcoming socket)

---

## Page 105

Summary
▪application architectures
• client-server
• P2P
▪application service requirements:
• reliability, bandwidth, delay
▪Internet transport service model
• connection-oriented, reliable: TCP
• unreliable, datagrams: UDP
▪
specific protocols:
• HTTP
• SMTP, IMAP
• DNS
• P2P: BitTorrent
▪
video streaming, CDNs
▪
socket programming: 
    TCP, UDP sockets
Application Layer: 2-105

---

## Page 106

Application Layer - Summary
typical request/reply message exchange:
◦client requests info or service
◦server responds with data, status code
message formats:
◦headers: fields giving info about data
◦data: info(payload)  being communicated
Application Layer: 2-106
Most importantly: learned about protocols!
important themes: 
▪centralized vs. decentralized 
▪stateless vs. stateful
▪scalability
▪reliable vs. unreliable 
message transfer 
▪“complexity at network 
edge”
