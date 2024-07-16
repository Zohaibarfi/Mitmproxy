import re

# Task 1: Copy the content of 1.txt directly into list.txt
with open("/Users/macos/zohaib/1.txt", "r") as f1:
    with open("/Users/macos/zohaib/List2.txt", "w") as f3:
        for line in f1:
            f3.write(line)

# Task 2: Extract domains and IPs from lines with TLS handshake errors in domains.txt
# and append them to list.txt with their respective reasons
failure_entries = set()  # To store unique failure entries
with open("/Users/macos/zohaib/domains.txt", "r") as domains_file:
    for line in domains_file:
        if "Client TLS handshake failed" in line:
            domain_match = re.search(r'for (.*?) ', line)
            if domain_match:
                domain = domain_match.group(1)
                ip_match = re.search(r'\((.*?)\)', line)
                if ip_match:
                    ip = ip_match.group(1).split(":")[0]
                    if not ip.isdigit():
                        # Search for the IP address in domains.txt
                        with open("/Users/macos/zohaib/domains.txt", "r") as search_file:
                            for search_line in search_file:
                                if domain in search_line:
                                    ip_search_match = re.search(r'server connect .*?\((.*?)\)', search_line)
                                    if ip_search_match:
                                        ip = ip_search_match.group(1).split(":")[0]
                                        break
                    reason_match = re.search(r'\((.*?)\)', line.split("(", 1)[1])
                    if reason_match:
                        reason = reason_match.group(1)
                        # Task 3: Ensure only unique entries are added to list.txt
                        if (domain, ip) not in failure_entries:
                            # Task 4: Ensure the format of entries in list.txt is correct
                            with open("/Users/macos/zohaib/List2.txt", "a") as list2_file:
                                list2_file.write(f"Domain: {domain}, IP: {ip}, Status: failure, Reason: {reason}\n")
                                failure_entries.add((domain, ip))

# Task 5: Avoid adding :443 at the end of IPs
# Task 6: Avoid adding entries for domains and IPs that are already present in 1.txt
success_entries = set()  # To store unique success entries
with open("/Users/macos/zohaib/domains.txt", "r") as domains_file:
    for line in domains_file:
        # Extract domain and IP from server connect lines
        if "server connect" in line:
            domain_match = re.search(r'for (.*?)\:', line)
            if domain_match:
                domain = domain_match.group(1)
                ip_match = re.search(r'\((.*?)\)', line)
                if ip_match:
                    ip = ip_match.group(1).split(":")[0]
                    if not ip.isdigit():
                        # Search for the IP address in domains.txt
                        with open("/Users/macos/zohaib/domains.txt", "r") as search_file:
                            for search_line in search_file:
                                if domain in search_line:
                                    ip_search_match = re.search(r'server connect .*?\((.*?)\)', search_line)
                                    if ip_search_match:
                                        ip = ip_search_match.group(1).split(":")[0]
                                        break
                    # Task 5: Avoid adding :443 at the end of IPs
                    # Task 6: Avoid adding entries for domains and IPs that are already present in 1.txt
                    if (domain, ip) not in success_entries and (domain, ip) not in failure_entries:
                        with open("/Users/macos/zohaib/List2.txt", "a") as list2_file:
                            list2_file.write(f"Domain: {domain}, IP: {ip}, Status: success, Reason: unknown\n")
                            success_entries.add((domain, ip))
