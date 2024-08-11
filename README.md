<h1>Computer Security Course Project </h1>
<h3>Overview</h3>
This project is part of my computer security course and includes both theoretical research and practical coding exercises. The project is divided into three main parts: web crawling and scraping, ARP and DNS spoofing experiments, and theoretical research on detecting web crawlers.

<h3>Web Crawling and Scraping</h3>
In this part, I developed a Python script using BeautifulSoup to crawl a sample news website (TechCrunch) and extract AI-related news articles along with their corresponding URLs. The extracted data is saved into a JSON file.

Script Overview
The script performs the following steps:

Sends an HTTP request to the TechCrunch AI news category page.
Parses the HTML content using BeautifulSoup.
Extracts AI-related news articles, their URLs, authors, and published dates.
Saves the extracted data into a JSON file and the URLs into a separate JSON file.


<h3>ARP and DNS Spoofing Experiments</h3>
This part involves conducting ARP spoofing and DNS spoofing experiments on a local network using NetfilterQueue and Scapy. Additionally, I used Snort to detect Man-in-the-Middle (MITM) attacks.

Experiment Overview
ARP Spoofing: Redirects network traffic by sending false ARP messages.
DNS Spoofing: Redirects DNS queries to a malicious server.
MITM Detection: Uses Snort to detect and alert on MITM attacks.

<h3>Detecting Web Crawlers</h3>
The final part of the project is theoretical research on how to detect web crawlers. This includes methods such as analyzing user-agent strings, monitoring request patterns, and using honeypots.

Key Points
User-Agent Analysis: Identifying bots based on their user-agent strings.
Request Patterns: Detecting unusual request patterns that indicate automated behavior.
Honeypots: Setting up traps to identify and block malicious bots.
