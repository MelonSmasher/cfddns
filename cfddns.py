#!/usr/bin/env python2

from __future__ import print_function
from cfddns import Config, DDNSClient


def main():
    config = Config()
    client = DDNSClient(config.cf_api_key, config.cf_email, config.cf_zones, config.ip_urls)
    client.set_cf_dns_records()


if __name__ == "__main__":
    main()
