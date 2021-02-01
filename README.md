# CloudFlare Dynamic DNS Client

Sets target DNS record IP addresses to the current external IP address.

---

## Setup:

```bash
# Get the code
cd /opt/
git clone https://github.com/MelonSmasher/cfddns.git;
# Link the config file
ln -s /opt/cfddns/config /etc/cfddns;
# Create a new config
cp /opt/cfddns/config/config.example.yaml /opt/cfddns/config/config.yaml;
# edit the config with your CF information
vi /etc/cfddns/config.yaml;
# install libraries
pip install -r /opt/cfddns/requirements.txt;
```

## Usage:

Run manually:

```bash
cd /opt/cfddns;
./cfddns.py;
```

Cron job every 5 minutes:
 
 ```bash
 */5 * * * * cd /opt/cfddns; python2 /opt/cfddns/cfddns.py | tee /var/log/cfddns.log
 ```
