# HawkEye

**HawkEye** is a comprehensive threat intelligence gathering tool designed to fetch essential information for a given domain or IP address. 

## Features

- **WHOIS Information**: Retrieve registration details of domains.
- **DNS Records**: Access various DNS record types associated with a domain.
- **Reverse IP Lookup**: Identify domains hosted on a specific IP address.
- **Geolocation**: Get geographical information based on the provided IP address.

## Installation

To get started with **HawkEye**, follow these steps:

1. **Clone the repository**:

   ```bash
   git clone https://github.com/hackerjacke440/HawkEye.git
   ```

2. **Navigate into the project directory**:

   ```bash
   cd HawkEye
   ```

3. **Run the application**:

   ```bash
   python hawkeye.py
   ```

Here's a professional and clear usage section for **HawkEye** based on the provided code:

---

## Usage

To utilize **HawkEye**, follow these steps:

1. **Run the Script**: Execute the script from the command line by providing a target domain or IP address as an argument.

   ```bash
   python hawkeye.py <target>
   ```

   - `<target>`: The domain (e.g., `example.com`) or IP address (e.g., `192.168.1.1`) you want to investigate.

2. **Output Information**: The tool will gather and display various types of information about the provided target, including:

   - **WHOIS Lookup**: Registration details of the domain.
   - **DNS Lookup**: A records associated with the domain.
   - **Reverse IP Lookup**: Domains hosted on the specified IP address using the HackerTarget API.
   - **IP Geolocation**: Geographic information related to the IP address using the ipinfo.io API.

### Example

To perform a WHOIS lookup and gather information for a domain, use the following command:

```bash
python hawkeye.py example.com
```

This will output the results for WHOIS data, DNS records, reverse IP lookup, and geolocation.

## Contributing

Contributions are welcome! If you'd like to contribute to **HawkEye**, please fork the repository and submit a pull request.
