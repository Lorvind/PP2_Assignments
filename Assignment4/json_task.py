import json

with open("sample-data.json") as f:
    data = json.load(f)

print("Interface status")
print('='*80)
print(f"{'DN':50} {'Description':20} {'Speed':8} {'MTU':6}")
print('-'*50, '-'*20, '-'*6, '-'*6)

for item in data["imdata"]:
    attributes = item["l1PhysIf"]["attributes"]
    dn = attributes["dn"]
    speed = attributes["speed"]
    mtu = attributes["mtu"]

    print(f"{dn:50} {'':20} {speed:8} {mtu:6}")