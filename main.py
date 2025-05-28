from ipaddress import ip_network, ip_address
from jinja2 import Template

with open("templates/docker-example.j2") as f:
    template_str = f.read()

start_index = 1
end_index = 10
base_subnet = ip_network("192.168.10.0/30")
subnet_step = 4  # /30 = 4 ip addresses: network, host1, host2, broadcast

template = Template(template_str)
services = []
used_subnets = set()

for i in range(start_index, end_index + 1):
    # Calculate new subnet with a step of subnet_step
    subnet_base = int(base_subnet.network_address) + (i - start_index) * subnet_step
    subnet = ip_network(f"{ip_address(subnet_base)}/30", strict=False)
    
    # Check for duplicate subnets
    if str(subnet) in used_subnets:
        raise ValueError(f"Duplicate subnet detected: {subnet}")
    used_subnets.add(str(subnet))
    
    # Get the second host in the subnet
    ip_addr = list(subnet.hosts())[1]
    
    services.append({"index": i, "ip_address": str(ip_addr), "subnet": str(subnet)})

output = template.render(services=services)

with open("output/docker-compose.yml", "w") as f:
    f.write(output)

print(f"Generated docker-compose.yml for {len(services)} services.")
