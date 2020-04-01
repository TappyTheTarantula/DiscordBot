# zerotier.py

import requests
import json
import os

class zerotier:
    def __init__(self, apitoken, network):
        self.apitoken = apitoken
        self.network = network

        # Should log in
        request = requests.get("https://my.zerotier.com/api/status", headers={"Authorization":"bearer {}".format(self.apitoken)})

    def members(self):
        request = requests.get("https://my.zerotier.com/api/network/{}/member".format(self.network), headers={"Authorization":"bearer {}".format(self.apitoken)})
        return request.json()

    def linkmembers(self):
        pass

    def linkmember(self):
        pass

    def stringmembers(self):
        memberstring = ""
        for member in self.members():
            online = ""
            if(member["online"]):
                online = "ONLINE"
            else:
                online = "OFFLINE"
            memberstring += "{}\t{}\t{}\n".format(member["config"]["ipAssignments"][0], online, member["name"])
        return memberstring[:-1]

    # def stringmember(self, node):
    #     for 

def main():
    from dotenv import load_dotenv
    load_dotenv()

    ZEROTIER_NETWORK = os.getenv('ZEROTIER_NETWORK')
    ZEROTIER_TOKEN = os.getenv('ZEROTIER_TOKEN')

    api = zerotier(ZEROTIER_TOKEN, ZEROTIER_NETWORK)

    print(api.stringmembers())

if(__name__ == "__main__"):
    main()