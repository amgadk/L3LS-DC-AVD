import ssl
import requests
import time
from cvprac.cvp_client import CvpClient

ssl._create_default_https_context = ssl._create_unverified_context
requests.packages.urllib3.disable_warnings()

cvp_client = CvpClient()
cvp_ip = "10.18.150.27"
cvp_token = "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJkaWQiOjc1NjE1NzIwMzA5NDQ5MDM0MjAsImRzbiI6ImF2ZCIsImRzdCI6ImFjY291bnQiLCJleHAiOjE3NjE3NzY1MjcsImlhdCI6MTc2MDU2NjkzMSwib2dpIjozLCJvZ24iOiJEZWZhdWx0Iiwic2lkIjoiN2UyNGUxYzQ0NTczZTI2MzhhMmJkOTRlNTFjMDU3ZjNjYTA0YjA5MmQzNmFhY2MxZjRmMDA2Y2Y1ODdkZWQ1MC1KeDhjMVFOLVBacGtkbTVaaTFGWWstNUVPenh4WlU0a09CQ1JRSk51In0.ZPLpVjdTi1dDFR3Ko7irHEJEkRqmVZYyDkxHQ1fALVPlurolIMaHbx7ENYFH7EWcEiBkAGyF4X57P_jLAy8a68kWAMNYv0irpcGdfcUeNrQj0XmREsHSmdjcTQU0vHCRMnvQplPgfZLFRORpSc2f3qvlcjw__rNMDWRMIQm9t_VMBMLMdOhprmAJ1HApzQq2R4gqbNgVPJLEP2n9nmSgxfDiNDaGE7TtNV3xqdWOK7RAh11OH3Du-GlWZ0dlw92rS5xgdgbAUDQ6r0Jl2FHNGZ12J83lK5TWawlircP_VzWIUqcw-r4gNCpfAFOIv1Tr3wEuyUdfXZaUjnOy7-h6mFCX_XiLWKh0ME0i7Y8zRYU9L4ninChpSHLs8KF0EvrwxCSR2dYKbQSwMgtj6XkmiG4wHEZK_1G-PJ65q2DyTcaGX3uIHUUPNSlt2HEuuK5u0nsg1y-1Qd3zg-nikBtlQBVB16u53K0C3FXelQ4CHuQbJTD4LwtxCVRYAw7jpVw8d8GCRfH1r7api63UWo48DKMMdNWOl6r6O2-4aWHQXS1az7XpgNdjqr8BZGojuDE0fdXIojtp8FjYP-YLzrl52wsPxP71i_NqwUeXLoXy046ONOn0AnSLxWmSvGRfPqfe1KnPNTantTsE9To_JFNz-1uu8tXnJ3YIxyYASD68ewc"



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
