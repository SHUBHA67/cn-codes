def get_ip_class(ip_address):
    octets = ip_address.split('.')
    first_octet = int(octets[0])
    if 1 <= first_octet <= 126:
        return 'Class A'
    elif 128 <= first_octet <= 191:
        return 'Class B'
    elif 192 <= first_octet <= 223:
        return 'Class C'
    else:
        return 'Unknown Class'

def convert_to_binary(ip_address):
    binary_octets = [bin(int(octet))[2:].zfill(8) for octet in ip_address.split('.')]
    binary_ip = '.'.join(binary_octets)
    return binary_ip

def generate_subnet(ip_address, subnet_mask):
    ip_octets = ip_address.split('.')
    mask_octets = subnet_mask.split('.')
    subnet_octets = [str(int(ip_octet) & int(mask_octet)) for ip_octet, mask_octet in zip(ip_octets, mask_octets)]
    subnet = '.'.join(subnet_octets)
    return subnet

def main():
    ip_address = input("Enter the initial IP address: ")
    ip_class = get_ip_class(ip_address)
    print(f"The class of the initial IP address is: {ip_class}")
    binary_ip = convert_to_binary(ip_address)
    print(f"The binary representation of the IP address is: {binary_ip}")
    subnet_mask = input("Enter the subnet mask: ")
    subnet = generate_subnet(ip_address, subnet_mask)
    print(f"The subnet address is: {subnet}")

if __name__ == "__main__":
    main()
