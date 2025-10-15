# Azure Security Automation Lab

This project demonstrates how I automated basic **Azure resource operations** using **Python** and the **Azure SDK** — a practical step toward security compliance automation in cloud environments.

---

## 🧠 Overview

Using Azure CLI and Python, I:
- Authenticated securely with `DefaultAzureCredential`
- Created and verified a Resource Group in **East US**
- Listed existing resource groups programmatically
- Validated automation output using CLI and SDK commands

This mirrors how enterprises automate **policy validation**, **access checks**, and **resource inventory** under NIST 800-53 / 171 controls.

---

##⚙️ Tools & Libraries

- **Azure CLI**
- **Python 3.10+**
- **Azure SDK for Python**
  - `azure-identity`
  - `azure-mgmt-resource`

Install dependencies:
```bash
pip install -r requirements.txt
