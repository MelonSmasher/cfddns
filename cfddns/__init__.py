from __future__ import print_function
from yaml import load
from cfddns.utils import get_external_ip
import CloudFlare
import sys


class Config(object):
    def __init__(self):
        with open('config/config.yaml') as data_file:
            # read the config file
            c = load(data_file)
            self.cf_api_key = c['cloudflare']['api_key']
            self.cf_email = c['cloudflare']['email']
            self.cf_zones = c['cloudflare']['zones']
            self.ip_urls = c['ip_urls']


class DDNSClient(object):
    def __init__(self, api_key, email, zones, ip_urls):
        """
        :param api_key:
        :param email:
        :param zones:
        :param ip_urls:
        """
        # client class variables
        self.api_key = api_key
        self.email = email
        self.zones = zones
        self.ip_urls = ip_urls
        self.external_ip = get_external_ip(self.ip_urls)

    # sets target dns records to the current external ip address
    def set_cf_dns_records(self):
        # create a cf client
        cf = CloudFlare.CloudFlare(email=self.email, token=self.api_key)
        # get our current cf zones
        current_zones = cf.zones.get()
        # get our target zones
        target_zones = self.zones
        # go through each current zone
        for zone in current_zones:
            # if that zone is a target zone
            if zone['name'] in target_zones:
                # get the current DNS records for that zone
                current_records = cf.zones.dns_records.get(zone['id'])
                # go through each of the current cf DNS records
                for cr in current_records:
                    # if that record is an A record
                    if str(cr['type']) == 'A':
                        # get the target records
                        target_records = target_zones[zone['name'].lower()]
                        # go through our target records
                        for tr in target_records:
                            # build the target fqdn
                            target_fqdn = '.'.join([tr, zone['name']]).lower()
                            # If we are targeting the root record
                            if tr == '@' and cr['name'].lower() == zone['name'].lower():
                                # Is the current ip different than the current external ip
                                if str(cr['content']) != str(self.external_ip):
                                    # make a copy of that record
                                    dns_record = cr
                                    # set the ip of that record to our external ip
                                    dns_record['content'] = self.external_ip
                                    # nice output
                                    sys.stdout.write(
                                        ''.join(
                                            [cr['name'].lower(), ': ', cr['content'], ' ---> ', self.external_ip]
                                        )
                                    )
                                    sys.stdout.flush()
                                    # try to update that record
                                    try:
                                        cf.zones.dns_records.put(zone['id'], cr['id'], data=dns_record)
                                        sys.stdout.write(" OK!")
                                    except CloudFlare.exceptions.CloudFlareAPIError as e:
                                        sys.stdout.write(" Fail!")
                                    # newline
                                    print('')
                            # if we are targeting a sub domain record
                            elif target_fqdn == cr['name'].lower():
                                if str(cr['content']) != str(self.external_ip):
                                    # make a copy of that record
                                    dns_record = cr
                                    # set the ip of that record to our external ip
                                    dns_record['content'] = self.external_ip
                                    # nice output
                                    sys.stdout.write(
                                        ''.join(
                                            [target_fqdn, ': ', cr['content'], ' ---> ', self.external_ip]
                                        )
                                    )
                                    sys.stdout.flush()
                                    # try to update that record
                                    try:
                                        cf.zones.dns_records.put(zone['id'], cr['id'], data=dns_record)
                                        sys.stdout.write(" OK!")
                                    except CloudFlare.exceptions.CloudFlareAPIError as e:
                                        sys.stdout.write(" Fail!")
                                    # newline
                                    print('')
