import json
import urllib.request

base_url = "http://localhost:58000/api/v1"

print("==========================================================")
print(" SCRIPT PROPIO: CLASIFICACION DE HOSTS POR VLAN Y SUBRED")
print("==========================================================\n")

# 1. Obtencion del Ticket
headers_post = {"Content-Type": "application/json"}
body_post = json.dumps({"username": "cisco", "password": "class"}).encode('utf-8')
req_ticket = urllib.request.Request(f"{base_url}/ticket", data=body_post, headers=headers_post, method='POST')

try:
    with urllib.request.urlopen(req_ticket) as resp:
        ticket = json.loads(resp.read().decode('utf-8'))["response"]["serviceTicket"]
        print(f"[*] Autenticacion exitosa. Ticket: {ticket}\n")
except Exception as e:
    print(f"[!] Error de autenticacion: {e}")
    exit()

# 2. Consulta de Hosts
headers_get = {"X-Auth-Token": ticket}
req_host = urllib.request.Request(f"{base_url}/host", headers=headers_get, method='GET')

# Mapeo de Subredes / VLANs de la empresa
vlan_mapping = {
    "10.36.10.": "VLAN 10 - Sucursal 1 (Usuarios)",
    "10.36.20.": "VLAN 20 - Sucursal 1 (Impresoras)",
    "10.36.40.": "VLAN 40 - Sucursal 3 (LAN General)",
    "10.36.50.": "VLAN 50 - Data Center / Servidores",
    "10.36.99.": "VLAN 99 - Gestion y Administracion"
}

grouped_hosts = {vlan: [] for vlan in vlan_mapping.values()}
grouped_hosts["Otras Subredes"] = []

with urllib.request.urlopen(req_host) as resp:
    hosts_data = json.loads(resp.read().decode('utf-8')).get("response", [])
    
    for h in hosts_data:
        ip = h.get("hostIp", "")
        name = h.get("hostName", "N/A")
        mac = h.get("hostMac", "N/A")
        
        assigned = False
        for prefix, vlan_name in vlan_mapping.items():
            if ip.startswith(prefix):
                grouped_hosts[vlan_name].append((name, ip, mac))
                assigned = True
                break
        if not assigned:
            grouped_hosts["Otras Subredes"].append((name, ip, mac))

# 3. Impresion del Reporte Clasificado
for vlan, hosts in grouped_hosts.items():
    if hosts:
        print(f"=== {vlan} (Total: {len(hosts)}) ===")
        print(f"{'HOSTNAME':<20} {'DIRECCION IP':<16} {'DIRECCION MAC':<18}")
        print("-" * 56)
        for h in hosts:
            print(f"{h[0]:<20} {h[1]:<16} {h[2]:<18}")
        print()

print("==========================================================")
print(" Auditaria completada exitosamente.")
print("==========================================================")

