import ssl
import requests
import time
from cvprac.cvp_client import CvpClient

ssl._create_default_https_context = ssl._create_unverified_context
requests.packages.urllib3.disable_warnings()

cvp_client = CvpClient()
cvp_ip = "10.18.137.110"
cvp_token = "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJkaWQiOjc1NTk0NzA5MTE0Njg4NjM3NDMsImRzbiI6ImF2ZCIsImRzdCI6ImFjY291bnQiLCJleHAiOjE3NjE4OTI0NjcsImlhdCI6MTc2MDA3ODA3MSwib2dpIjozLCJvZ24iOiJEZWZhdWx0Iiwic2lkIjoiMTAxYTlmYzA5ZTUyNDY5ZjA3ZWZmMTk3NzcxMWVkOWM2YzgyYTc1ZWE2MDllYjY0NDM3NTVjMGE0MWY4MGNjMi0wWUFZMWowalR0WmhVTjlEZUxFS1BuQU90VE5NRDVvRDBPd0VPMkxZIn0.AVoGWgB4uJweBhUdDQkA1AGu47sjdDTmliBKzWIz1K1JPjw-MmrW90IDqQPeX_TB8h_YSTlH8oRbX0JzmKUR6aGmBYeVdJSVbfPNOMCjTmy50XuFmnn9MaLiI2gNP1mduBpjiUwlbB-kSfYQZD33EnmDySLR5NvsEVkIuh0L5VlzW1Ee4-rS-qFTN7yjj17smXQcbaOAW-wqXwCaDlGDsP_6mQTUeqRkEgIfe9zSwmeBzCu9VHK3pU4Kv0ebxbw-0Nacq1mACYxiO9b-yZYTMsjGTuteT388C_9_MCE5TZzdvUg3Cbjkl40DnIlvZcnYMQI2ErGLsw1U-8mBq39__OYo8cioRtb1L1MvJglCOUBvzPv_Rd7P1InmBHFffkJ5WTwpFy_64X3SPfA9TfD5wq-k0r0ikk3SYGNW_Rwnj7wefQpgP0b4tpyPe6JrOj_GhFeqWPtv1CJkVPvdglRnYc4wwmpZDOeI_AkxB0gl_iCWatPxmE95zQT4cgmsEmJVCKmFh7Ix34zigc__IZoNzSi9mjOnMoTtHFviaAJ1Ayv0KUtYEutUgWda6zZzSALyNv1iVjn0wZw85ngpFrx5xJsJrVZSSz_mqrOdB3BrjB7ZM7u2sfBYvydSZj0Vm2Cv0CBMUafPVbNOxTqc21dPhwF0teFuiEj2vWrVutqL6Z4"



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
