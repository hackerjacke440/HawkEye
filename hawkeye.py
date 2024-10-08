import whois
import dns.resolver
import requests
import argparse

# WHOIS Lookup
def whois_lookup(domain):
    try:
        whois_info = whois.whois(domain)
        return whois_info
    except Exception as e:
        return f"Error fetching WHOIS data: {e}"

# DNS Lookup
def dns_lookup(domain):
    try:
        resolver = dns.resolver.Resolver()
        result = resolver.query(domain, 'A')
        return [str(ip) for ip in result]
    except Exception as e:
        return f"Error fetching DNS records: {e}"

# Reverse IP Lookup (Example using HackerTarget API)
def reverse_ip_lookup(ip):
    try:
        response = requests.get(f"https://api.hackertarget.com/reverseiplookup/?q={ip}")
        return response.text if response.status_code == 200 else "Error with Reverse IP lookup."
    except Exception as e:
        return f"Error fetching Reverse IP data: {e}"

# IP Geolocation (Using ipinfo.io API)
def ip_geolocation(ip):
    try:
        response = requests.get(f"https://ipinfo.io/{ip}/json")
        return response.json() if response.status_code == 200 else "Error fetching IP geolocation."
    except Exception as e:
        return f"Error fetching geolocation data: {e}"

def main():
    parser = argparse.ArgumentParser(description="HawkEye - A Basic Threat Intelligence Tool")
    parser.add_argument("target", help="Target domain or IP")
    args = parser.parse_args()
    
    target = args.target

    print(f"\n[+] Gathering information for {target}...\n")

    # WHOIS Lookup
    if '.' in target:  # Basic check if it's a domain
        print("[WHOIS Lookup]")
        whois_data = whois_lookup(target)
        print(whois_data)
        print("\n")

        # DNS Lookup
        print("[DNS Lookup]")
        dns_data = dns_lookup(target)
        print(dns_data)
        print("\n")

    # Reverse IP Lookup
    print("[Reverse IP Lookup]")
    reverse_ip_data = reverse_ip_lookup(target)
    print(reverse_ip_data)
    print("\n")

    # IP Geolocation
    print("[IP Geolocation]")
    geo_data = ip_geolocation(target)
    print(geo_data)

if __name__ == "__main__":
    main()
