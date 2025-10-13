import ssl
import requests
import time
from cvprac.cvp_client import CvpClient

ssl._create_default_https_context = ssl._create_unverified_context
requests.packages.urllib3.disable_warnings()

cvp_client = CvpClient()
cvp_ip = "10.18.134.68"
cvp_token = "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJkaWQiOjc1NjA1NDk3Mjk5NDQyMDc2MTIsImRzbiI6ImF2ZCIsImRzdCI6ImFjY291bnQiLCJleHAiOjE3NjE1NDM1MTUsImlhdCI6MTc2MDMzMzkxOCwib2dpIjozLCJvZ24iOiJEZWZhdWx0Iiwic2lkIjoiMDJhYjBjZWExOGMzNWE4ZjNkM2YwOTQ5M2M2NDdiYjhmNjkxMzY5YjFiMTlhNTlkNjVmM2VlNzhjMzk5NDNiYy1BVDVLbjVsX25wU2VvVVNndEtsUFNmUVFLS0lvRWJTcGFaVGFjU2Q1In0.pj7xmcB8rtkeiwruNDQ5j5wbyBTXlk05S2OQdomCBX7KMcjwZSp7YefzMF29LDwDJT5DOu7nbB2zouSSwo6jN9NDT1B2I757BPDgBX9IeKu0Nrs6sMhdGZIURFkQ_mqNFYBxxRPstP1Gv45pgwRcPIaUd7ytgBtRX6oyagjs0Dm6GNi-mhQbdw9x_vYIszShrl2ePaCY4n5buEW9G4v_1vvF-r0FHDwgvvLFLq2h9dzmf-jbZhEmDr_roZ_J6FUFGYCk_oRBv4XTxiiKDIg4xCJpCYjXDVVkor59DX9HHzdSePudi6wiIbgAC4Y4UAJHfQFmHkYQ7OgpVVwsvdlNle0y2zztSJnjlEuBIoDey3e3v72bMEylAjcSJC1X1AHh2T7__y9JRhwftGnP-d71-3N_b0fehrJXL-wRBY-_pZA455jcWlCasXoROSO5rQg3zSMT2OFeK_v5gNSfwa6-0lvbXNg-Km1hWU3yebtbg4DodkBSXhZq7n4xUAwV9jrF3oiURLdihOXxezOx2sXsrPu8gdc4E2_JzUZ_fGS1iV0l2mlfANrAJsERw8Y9GKBYKAy5Q41SSIS9D8LzFSkm5PwE1lDZhFkRqvH658-bQRJ406i5bEp6x-UcLQJ-N0MI-kR72NPWbvIpAMQ7SQVLNla4HFCZZ8AAXcOdk140Aes"



def cvp_connection():
    """
    Connect to CloudVision instance.

    Parameters:
    self (object): The instance of the class.

    self.cvp_ip (str): The IP address of the CloudVision instance.
    self.is_cvaas (bool): A flag indicating whether the CloudVision instance is a Cloud Vision as a Service (CVAAS) instance.
    self.cvp_token (str): The API token for authentication with the CloudVision instance.

    Returns:
    None. The function establishes a connection to the CloudVision instance.
    """
    cvp_client.connect(
        nodes=[cvp_ip],
        username="",
        password="",
        api_token=cvp_token,
    )

def cvp_move_devices():
    """
    This function moves devices from the 'Undefined' container to the 'Tenant' container in CVP.

    Parameters:
    None

    Returns:
    None
    """
    cvp_connection()

    device_list = [
        {"deviceName": device["fqdn"]}
        for device in cvp_client.api.get_devices_in_container("Undefined")
    ]

    for device in device_list:
        device_info = cvp_client.api.get_device_by_name(
            device["deviceName"]
        )
        new_container = cvp_client.api.get_container_by_name("Tenant")
        cvp_client.api.move_device_to_container(
            "python", device_info, new_container
        )

    cvp_execute_pending_tasks()


def cvp_create_configlets():
    """
    This function creates and applies configlets to devices in the 'Tenant' container.

    Parameters:
    None

    Returns:
    None
    """
    time.sleep(20)
    print("Waiting for 20 seconds")
    cvp_connection()

    device_list = cvp_client.api.get_devices_in_container("Tenant")
    device_info = [
        {"name": device["fqdn"], "macAddress": device["systemMacAddress"]}
        for device in device_list
    ]

    for info in device_info:
        device_mac = info["macAddress"]
        device_short_name = info["name"]
        dev_mgmt = f"{device_short_name}_management"

        get_config = cvp_client.api.get_device_configuration(
            device_mac
        )
        cvp_client.api.add_configlet(dev_mgmt, get_config)

        device_name = cvp_client.api.get_device_by_name(
            device_short_name
        )
        mgmt_configlet = cvp_client.api.get_configlet_by_name(dev_mgmt)
        mgmt_configlet_key = [
            {"name": mgmt_configlet["name"], "key": mgmt_configlet["key"]}
        ]

        cvp_client.api.apply_configlets_to_device(
            "Management Configs", device_name, mgmt_configlet_key
        )


    cvp_execute_pending_tasks()

def cvp_execute_pending_tasks():
    """
    Execute all pending tasks in CVP.

    This function retrieves all pending tasks from CVP using the CVP API and executes each task.

    Parameters:
    None

    Returns:
    None
    """
    tasks = cvp_client.api.get_tasks_by_status("Pending")
    for task in tasks:
        cvp_client.api.execute_task(task["workOrderId"])

cvp_move_devices()
cvp_create_configlets()
