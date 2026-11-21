# TP Integrador - Automatización de Redes con Python y API REST

Este repositorio contiene los scripts de automatización en Python utilizados para la interacción con la API REST del Cisco Packet Tracer Network Controller en el marco del Trabajo Práctico Integrador.

## Contenido del Repositorio

Los scripts se encuentran en la carpeta `src/` 

1. **`01_get-ticket.py`**: Solicita y obtiene el ticket de autenticación (`serviceTicket`) mediante una petición HTTP POST al endpoint `/api/v1/ticket`.
2. **`02_get-network-device.py`**: Consulta y despliega el inventario de dispositivos de infraestructura (routers y switches) registrados en el controlador desde el endpoint `/api/v1/network-device`.
3. **`03_get-host.py`**: Recupera el listado completo de hosts finales conectados a la red mediante una solicitud HTTP GET al endpoint `/api/v1/host`.
4. **`04_tabulate.py`**: Integra la autenticación automática y despliega en tablas formateadas en consola la información consolidada de infraestructura y hosts finales.
5. **`05_vlan_host_inventory.py` (Script Propio)**: Script desarrollado por el grupo que realiza la clasificación automática de los hosts finales agrupándolos según su dirección IP dentro de las VLANs y subredes definidas en la topología corporativa. Utiliza las librerías nativas de Python (`urllib.request` y `json`) para interactuar con el controlador.

