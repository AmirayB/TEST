import ipaddress

def calculate_network_and_broadcast(ip_with_subnet):
    # IP ünvanını və subnet maskasını təhlil edir
    network = ipaddress.ip_network(ip_with_subnet, strict=False)
    
    # Şəbəkə ünvanını və yayım ünvanını qaytarır
    return {
        "Network Address": str(network.network_address),
        "Broadcast Address": str(network.broadcast_address)
    }

# Nümunə
ip_with_subnet = input("Daxil; et:")
result = calculate_network_and_broadcast(ip_with_subnet)

print(f"IP/subnet: {ip_with_subnet}")
print(f"Network Address: {result['Network Address']}")
print(f"Broadcast Address: {result['Broadcast Address']}")