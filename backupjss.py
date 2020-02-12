import requests
import os
import json

# global variables
my_login = os.getenv("my_login")
my_pass = os.getenv("my_pass")
my_company = os.getenv("my_company")

# get configuration profiles
def get_configuration_profiles():
    cp = requests.get(
        f"https://{my_company}.jamfcloud.com/JSSResource/osxconfigurationprofiles",
        auth=(my_login, my_pass),
        headers={"accept": "application/json"},
    )

    configurationprofiles_total = len(cp.json()["os_x_configuration_profiles"])
    i = 0
    configurationprofiles_list = []
    while i < configurationprofiles_total:
        id = cp.json()["os_x_configuration_profiles"][i]["id"]
        i += 1
        cp2 = requests.get(
            f"https://{my_company}.jamfcloud.com/JSSResource/osxconfigurationprofiles/id/{id}",
            auth=(my_login, my_pass),
            headers={"accept": "application/json"},
        )
        payload = cp2.json()["os_x_configuration_profile"]["general"]["payloads"]
        name = cp2.json()["os_x_configuration_profile"]["general"]["name"]
        name = name.replace(" ", "_")

        # Write xml to file
        with open(f"Configuration_Profiles/{name}.xml", "w") as writer:
            writer.write(payload)


# get policies
def get_policies():
    po = requests.get(
        f"https://{my_company}.jamfcloud.com/JSSResource/policies/createdBy/jss",
        auth=(my_login, my_pass),
        headers={"accept": "application/json"},
    )

    policies_total = len(po.json()["policies"])
    i = 0
    policies_list = []
    while i < policies_total:
        id = po.json()["policies"][i]["id"]
        i += 1
        po2 = requests.get(
            f"https://{my_company}.jamfcloud.com/JSSResource/policies/id/{id}",
            auth=(my_login, my_pass),
            headers={"accept": "application/json"},
        )
        payload = po2.json()
        payload = str(payload)
        name = po2.json()["policy"]["general"]["name"]
        name = name.replace(" ", "_").replace("/", "_")

        # Write xml to file
        with open(f"Policies/{name}.json", "w") as writer:
            writer.write(payload)


# get smart computer groups | not finished
def get_smart_computer_groups():
    return


# get static computer groups | not finished
def get_static_computer_groups():
    return


# run functions
get_configuration_profiles()
get_policies()
