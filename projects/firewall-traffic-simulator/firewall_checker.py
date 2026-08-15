# Import required modules
import random
from collections import Counter


# Generate a random IP address for simulated network traffic
def generate_random_ip():
    return f"192.168.1.{random.randint(0, 20)}"


# Generate a random destination port
def generate_random_port():
    return random.choice(ports)


# Check an IP address AND port against the firewall rules
def check_firewall_rules(ip, rules, port):
    for rule_ip, action in rules.items():

        # Block only if the IP is blocked AND it is using a blocked port
        if ip == rule_ip and port in blocked_port_list:
            return action

    # Allow traffic by default if no blocking rule matches
    return "allow"


# Ports used to generate simulated traffic
ports = [21, 22, 53, 80, 443, 3389, 8080]


# Ports that the firewall considers blocked
blocked_port_list = [21, 22, 3389]


# Main firewall simulation
def main():

    # Define firewall rules for blocked IP addresses
    firewall_rules = {
        "192.168.1.1": "block",
        "192.168.1.4": "block",
        "192.168.1.9": "block",
        "192.168.1.13": "block",
        "192.168.1.16": "block",
        "192.168.1.19": "block",
    }

    # Initialize counters
    ip_attempts = Counter()
    allowed_count = 0
    blocked_count = 0
    blocked_port_attempts = Counter()

    # Simulate incoming network connections
    for _ in range(100):

        # Generate connection data
        ip_address = generate_random_ip()
        connection_port = generate_random_port()
        random_number = random.randint(0, 9999)

        # Count this IP attempt
        ip_attempts[ip_address] += 1
        

        # Determine whether traffic is allowed or blocked
        action = check_firewall_rules(
            ip_address,
            firewall_rules,
            connection_port
        )
       
        with open("FireWall.log", "a") as log_file:
            log_file.write(
        f"IP: {ip_address}, Port: {connection_port}, Action: {action}\n"
    )

        # Display the simulated connection
        print(
            f"IP: {ip_address}, "
            f"Port: {connection_port}, "
            f"Action: {action}, "
            f"Random: {random_number}"
        )

        # Track allowed and blocked traffic
        if action == "allow":
            allowed_count += 1

        elif action == "block":
            blocked_count += 1

        # Generate an alert when a blocked IP reaches 5 total attempts
        if ip_attempts[ip_address] == 5 and ip_address in firewall_rules:
            print(f"WARNING: Suspicious activity from {ip_address}")

        # Count blocked IP/port combinations
        if action == "block" and connection_port in blocked_port_list:
            blocked_port_attempts[(ip_address, connection_port)] += 1

    # Display overall traffic statistics
    print("\n========= SECURITY SUMMARY =========")
    print(f"Total Connections: {sum(ip_attempts.values())}")
    print(f"ALLOWED CONNECTIONS: {allowed_count}")
    print(f"BLOCKED CONNECTIONS: {blocked_count}")
    print(f"Unique Source IPs: {len(ip_attempts)}")

    # Display the five IP addresses with the most attempts
    print("\nTOP TALKERS:")

    for ip, count in ip_attempts.most_common(5):
        print(f"{ip}: {count} attempts")

    # Display suspicious blocked IP addresses
    print("\nSUSPICIOUS IPs:")

    for ip, count in ip_attempts.items():
        if count >= 5 and ip in firewall_rules:
            print(f"{ip}: {count} attempts - ALERT")

    # Display blocked IP/port combinations
    print("\nBLOCKED IP / PORT ATTEMPTS:")

    for (ip, port), count in blocked_port_attempts.items():
        print(f"{ip} -> Port {port}: {count} attempts")


print("=======================================")


# Run main() only when this file is executed directly
if __name__ == "__main__":
    main()