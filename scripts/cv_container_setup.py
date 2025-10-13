import ssl
import requests
import time
from cvprac.cvp_client import CvpClient

ssl._create_default_https_context = ssl._create_unverified_context
requests.packages.urllib3.disable_warnings()

cvp_client = CvpClient()
cvp_ip = "10.18.142.51"
cvp_token = "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJkaWQiOjc1NjA1NDg1MTAxNzM0OTU1NDgsImRzbiI6ImF2ZCIsImRzdCI6ImFjY291bnQiLCJleHAiOjE3NjE2MDA4OTIsImlhdCI6MTc2MDM5MTI5Niwib2dpIjozLCJvZ24iOiJEZWZhdWx0Iiwic2lkIjoiOTI2YTBlMGRlOTlkZDM2YjMyYzBkZTkwODU2YmVjNjNiZWI1N2M2ZmVmOTMxNGU4MzdmYjljYzIzZTlmY2Q2Ny1nanVQeTdhUndhY1lWb19DaXpPUXN1di1Jc3JCTnF4WG5vZmtLSlE0In0.d2lzwDIovb-CIUsDwBf-ZmczeXiUBlDS5zf1dfjB4oM28sOfTL1HueHIlmLGJKs4TO_89sHX1oZi3tSZlEwrTWvsERVHz5Wvxj18UStkWIbKgZ4YFlm8gQ0KtKSq6WISoh5StUvv8MbFJqDHB1PQteJTtNjQP6K8r5DLEEQpa9qi9IJC6ksYa8RzYYKeX3_rnbI28ScUorhnfe1UVex6z8NVOswzmsW74Z8CQ93UxIb7ijqH78pE2uzR98s_I3OXYbs6lPasQwVTUPVaN_8gF1it-vH7AUOOI9Tld1kT7SghzJWrXXjz35clhYcfr8OZNICDqFsO6M4qkQlrjhgg6WZ7XlfHSI3tl7qOjhlAAakjXsxJUtyo5M25_GvN-3LP_jK3jYv2iud_49rZrWyQI8BGaXeabuTp_691fuQ-y4YPRLboK7p87l8yCcuWcgDQgk38ohRrOThMfPO3DmFYItfmORZNxfnTqR5zqBYIC0ZXNAgGzqClh484kALgBmfJByFEh474JtXUTDXZlcy7saoziUWBGQLz33Ex2b44DAZyJMXYwh5_vX9XZmiT-3wHCbMXJMNM-myi5ljacZode9CHs5SvVKbFqmozghh34GASPJuiUH6G5ANu9TUfAq1T8XvvdMAgJEbxY1jzlmsjGKGUHMyEdKrR1zZZQRW_X10"



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
