def is_float(value):
    try:
        float(value)
        return True
    except ValueError:
        return False

def get_network_conditions(selected_speed):
    if isinstance(selected_speed, tuple):
        upload_speed, download_speed = selected_speed

        if is_float(upload_speed):
            upload_kbps = float(upload_speed) * 1000
        else:
            upload_kbps = 0

        if is_float(download_speed):
            download_kbps = float(download_speed) * 1000
        else:
            download_kbps = 0

        return {
            'offline': False,
            'latency': 5,
            'download_throughput': download_kbps,
            'upload_throughput': upload_kbps
        }
    else:
        if selected_speed == "3G good":
            return {
                'offline': False,
                'latency': 100,
                'download_throughput': 750 * 1024,
                'upload_throughput': 250 * 1024
            }
        elif selected_speed == "3G weak":
            return {
                'offline': False,
                'latency': 300,
                'download_throughput': 200 * 1024,
                'upload_throughput': 100 * 1024
            }
        elif selected_speed == "4G good":
            return {
                'offline': False,
                'latency': 50,
                'download_throughput': 1000 * 1024,
                'upload_throughput': 500 * 1024
            }
        elif selected_speed == "4G weak":
            return {
                'offline': False,
                'latency': 150,
                'download_throughput': 500 * 1024,
                'upload_throughput': 200 * 1024
            }
        else:
            return {
                'offline': False,
                'latency': 5,
                'download_throughput': 0,
                'upload_throughput': 0
            }
