# Define the paths to the input files and the output file
list1_path = "/Users/macos/zohaib/List1.txt"
list2_path = "/Users/macos/zohaib/List2.txt"
list3_path = "/Users/macos/zohaib/List3.txt"
list5_path = "/Users/macos/zohaib/List5.txt"

# Function to extract the domain from a line
def extract_domain(line):
    parts = line.split(",")
    if len(parts) > 0:
        return parts[0].split(":")[1].strip()  # Extract the domain part from the line
    return ""

# Read the domains from list1.txt and list2.txt into a set
all_domains = set()
with open(list1_path, "r") as list1_file:
    for line in list1_file:
        domain = extract_domain(line)
        if domain:
            all_domains.add(domain)

with open(list2_path, "r") as list2_file:
    for line in list2_file:
        domain = extract_domain(line)
        if domain:
            all_domains.add(domain)

# Open list5.txt for writing
with open(list5_path, "w") as list5_file:
    # Read list3.txt and write only those lines to list5.txt which domains are not in list1.txt or list2.txt
    with open(list3_path, "r") as list3_file:
        for line in list3_file:
            domain = extract_domain(line)
            if domain and domain not in all_domains:
                list5_file.write(line)

print("The segregation is done. Check list5.txt for the result.")
