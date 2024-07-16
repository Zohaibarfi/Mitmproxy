# Mitmproxy
Mitmproxy is a powerful network analysis tool that allows you to gain insights into the data exchanged between your device and the internet. It operates as an interactive HTTPS proxy, enabling detailed monitoring and manipulation of network traffic.
Mitmproxy offers several applications to suit different needs:
  mitmproxy: Terminal-based console for server-only mode.
  mitmweb: Web-based console for intuitive interaction and configuration.
  mitmdump: Command-line tool for recording and replaying HTTP traffic.

# Setting up Mitmproxy for Emulator Device :
Run below commands:
1. pip install mitmproxy - This command installs the Mitmproxy.
2. mitmproxy --host - This command opens the Mitmproxy Network Flow

Now for the setup in Emulator device we will need the Mitmproxy certificate. To install this,
in browser of the emulator device visit “http://mitm.it” and click on the Android logo.

First we configure the network settings. Go to “Settings,” “Wi-Fi” and long-press on your
connected network. Choose “Modify network config”

Click “Show Advanced Options” and change the Proxy settings to manual. Then change the
Proxy Hostname to your IP Address, and the port to 8080.

Now to install certificate :

➢ Go to Settings, Security and click “Install from device storage”

➢ Enter “mitmproxy-ca-cert” and click “OK”

Mitmproxy is now setup in your android emulator device. Surf on various apps and see the
network traffic in the flow screen.

# Here we will capture Network Traffic of Emulator Device:
In order to comprehensively analyze network traffic, it is essential to capture specific data
points that provide insights into the interactions between devices and servers. These data
points include domains, IP addresses, timestamps for successful connections made by
servers, as well as details for failed server connections such as domains, IP addresses,
timestamps, the URL to which the connection is redirected, and the reason for the failure.

# Run below commands to capture Network Traffic :
1. mitmweb -s /path/to/mitmfinal.py > /path/to/domains.txt - This command open a mitmweb     
   interface in terminal and in browser.
2. python3 mitmfinalpart1.py - This command will store Standalone Emulator Network Flow.
3. python3 mitmfinalpart2.py - This command will store Pre-Installed Apps Network Flow.
4. python3 mitmfinalpart3.py - This command will store Installed Apps Network Flow.
5. python3 mitmsegregation.py - This command will segregate the Network Flow of only the 
   Installed Apps.
