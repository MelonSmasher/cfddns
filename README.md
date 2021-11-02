# CloudFlare Dynamic DNS Client

Sets target DNS record IP addresses to the current external IP address.

---

## Setup:

You'll need your Cloudflare API key and Cloudflare account email for the config file.

There is an example config in [config.example.yaml](config.example.yaml).

### Docker

```bash
git clone https://github.com/MelonSmasher/cfddns.git && cfddns;
cp config/config.yaml.example config/config.yaml
# Edit config/config.yaml with your values
docker run -d \
  --name cfddns \
  --restart always \
  -v "/path/to/config/config.yaml:/cfddns/config/config.yaml" \
  -e "TTL=1800" \
  melonsmasher/cfddns
```

### Docker Compose

```bash
git clone https://github.com/MelonSmasher/cfddns.git && cfddns;
docker-compose up;
```

### Manual Install

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

#### Usage:

Run manually:

```bash
cd /opt/cfddns;
./cfddns.py;
```

Cron job every 5 minutes:

 ```bash
 */5 * * * * cd /opt/cfddns; python2 /opt/cfddns/cfddns.py | tee /var/log/cfddns.log
 ```
