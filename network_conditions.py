def is_float(value):
    try:
        float(value)
        return True
    except ValueError:
        return False

def get_network_conditions(selected_speed):
    if isinstance(selected_speed, tuple):
        upload_speed, download_speed = selected_speed

        # Check if upload_speed is a valid float string
        if is_float(upload_speed):
            upload_kbps = float(upload_speed) * 1000
        else:
            upload_kbps = 0  # or some default value

        # Check if download_speed is a valid float string
        if is_float(download_speed):
            download_kbps = float(download_speed) * 1000
        else:
            download_kbps = 0  # or some default value

        return {
            'offline': False,
            'latency': 5,  # You can adjust this value
            'download_throughput': download_kbps,
            'upload_throughput': upload_kbps
        }
    else:
        # Here, you can define the network conditions for each of the predefined speeds (3G good, 3G weak, etc.)
        if selected_speed == "3G good":
            return {
                'offline': False,
                'latency': 100,  # Example value
                'download_throughput': 750 * 1024,  # Example value
                'upload_throughput': 250 * 1024  # Example value
            }
        # Add conditions for other speeds similarly
        # ...
        # For now, if no matching condition is found, return a default condition
        return {
            'offline': False,
            'latency': 5,
            'download_throughput': 0,
            'upload_throughput': 0
        }
