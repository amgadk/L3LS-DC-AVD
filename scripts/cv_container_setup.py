import ssl
import requests
from cvprac.cvp_client import CvpClient

ssl._create_default_https_context = ssl._create_unverified_context
requests.packages.urllib3.disable_warnings()

cvp_client = CvpClient()
cvp_ip = "10.18.138.107"
cvp_token = "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJkaWQiOjc1NTk0MTY4ODkzNzAyMTQ2NDIsImRzbiI6ImN2cHJhYyIsImRzdCI6ImFjY291bnQiLCJleHAiOjE3NjE4ODE2MTcsImlhdCI6MTc2MDA2NzIyMSwib2dpIjozLCJvZ24iOiJEZWZhdWx0Iiwic2lkIjoiZGExNzZiYmFkYzg3OTE1ZDNjZjY0ODU1Y2QzYzBjMzQ5ZDA3ZDk2ZDM5ZDczMWQ2NTc1NTI4OWRhN2Q1YzIxNy1OdXFzdkUtRDdnZE1rQlU4SVBkeEoyWlJTSlZuVHFrVkVtUVB3NXR0In0.J1h4hKrpoMt-41I-afS280RHm1w5AC46BzDMfXF0cETNElzcKdVCOiPkxCV3w18V1QOzUHoUQ_oiG6DdRgulamUyghmf0J4h4-9H2Ilcf9H20Pe1_jnWBWg-XWpOy1ume9rC7cnMtuPhQt6wU0AI-5ls5v4RwItjuj2qTXust5xTRw6jNGOXzpVk8C3pGTfk9NY9_NrRg8VieDQgv-i5OFvjWgQ4lk0p3EviMPzK0C1gV3-UluBbnnC0hvkx1vukbzKP4ZzRaYjEaKA0l-Ongx7Xpt0PcQxGAC32JwPQSOzbFZ4FqVKK4zL82fAnc_QBYp4yXK828sM8r480tlhpmo-j20OKFCiXDbGOHql2KhOPOzS6OQU-zrdSN8zkBnLV6jfrZhrF294xl7hUCUt0XurlaPdqheXkISvzIVSART0FpJPmCtAo__w8yZHgNt3Q_OdYkyD0IRSvMpdUGXuGJGE2dv_z3pK3ZqWPaRHlaDRhoXC90_tLAiGPww9dmrP-K5ixhMyZdP9QhtqQExZ-wlfy3Tu7XqxKZPLir-yPvSbZMxDRdvaJCCG6didkK7jCuHRgkS_ypXn5kupSvRZPH8LKs6ENZsaje6km2X-1xng4gqDc6jSSvtovutwv4vXZhYQr4C2I96rtg62fpO1WZAociHdgNgpjj6KmB7ho6No"



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
        #time.sleep(5)
        #print("Waiting for 5 seconds")

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
