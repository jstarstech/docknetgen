# Docker Compose Networks Generator

This script generates a `docker-compose.yml` file with a specified number of services,  
each assigned a unique subnet and IP address. It's useful when you need strict network isolation  
between containers (e.g., for proxy rotation, simulation environments, or testing purposes).

## Features

- Generates services with individual `/30` subnets (2 usable IPs).
- Assigns a unique static IP to each container.
- Prevents duplicate subnets.
- Fully templated via Jinja2.
- Easy to customize and extend.

## Requirements

- Python 3.6+
- [Jinja2](https://palletsprojects.com/p/jinja/)

Install dependencies (if needed):

```bash
pip install jinja2
```
