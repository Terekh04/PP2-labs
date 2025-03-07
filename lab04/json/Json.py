import json
with open("C:/Users/vasya/githowto/repositories/work/lab04/json/sample-data.json") as file:
    data = json.load(file)

interfaces = data["imdata"]

print("Interface Status")

print("=" * 65)

print(f"{'DN':50} {'Description':20} {'Speed':10}")

print("-" * 65)


for item in interfaces:
    dn = item["l1PhysIf"]["attributes"]["dn"]

    description = item["l1PhysIf"]["attributes"].get("descr", "inherit")

    speed = item["l1PhysIf"]["attributes"].get("speed", "inherit")
    
    print(f"{dn:50} {description:20} {speed:8}")