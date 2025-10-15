from azure.identity import DefaultAzureCredential
from azure.mgmt.resource import ResourceManagementClient

# Authenticate and list resource groups
subscription_id = "1c3f46a4-9e04-4558-80b6-53570868027b"  # Replace with your Azure subscription ID

credential = DefaultAzureCredential()
client = ResourceManagementClient(credential, subscription_id)

print("Listing resource groups in your subscription:\n")
for rg in client.resource_groups.list():
    print(f"Name: {rg.name}, Location: {rg.location}")

print("\n===========================================")
print("✅ Script executed successfully")
