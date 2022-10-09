import sys
import time
from random import uniform
from termcolor import colored
import psutil
import platform
from datetime import datetime
import GPUtil
from tabulate import tabulate


def slowprint(s, col='green', slow=1./50, isChangeSpeed=False):
    """Print slower"""
    if isChangeSpeed == False:
        for c in s + '\n':
            sys.stdout.write(colored(c, col))
            sys.stdout.flush()
            time.sleep(slow)
    else:
        for c in s + '\n':
            sys.stdout.write(colored(c, col))
            sys.stdout.flush()
            a = uniform(1./25, 0.6)
            time.sleep(a)


def get_size(bytes, suffix="B"):
    """
    Scale bytes to its proper format
        1253656 => '1.20MB'
        1253656678 => '1.17GB'
    """
    factor = 1024
    for unit in ["", "K", "M", "G", "T", "P"]:
        if bytes < factor:
            return f"{bytes:.2f}{unit}{suffix}"
        bytes /= factor


def print_sys():
    print(1)
    uname = platform.uname()
    output = "="*40 + "System Information" + "="*40 + f"""
System: {uname.system}
Node Name: {uname.node}
Release: {uname.release}
Version: {uname.version}
Machine: {uname.machine}
Processor: {uname.processor}"""
    slowprint(output)


def print_bt():
    boot_time_timestamp = psutil.boot_time()
    bt = datetime.fromtimestamp(boot_time_timestamp)
    output = "="*40 + "Boot Time" + "="*40 + \
        f"\nBoot Time: {bt.year}/{bt.month}/{bt.day} {bt.hour}:{bt.minute}:{bt.second}"
    slowprint(output)


def print_cpu():
    output = "="*40 + "CPU Info" + "="*40
    output += "\nPhysical cores:" + str(psutil.cpu_count(logical=False))
    output += "\nTotal cores:" + str(psutil.cpu_count(logical=True))
    cpufreq = psutil.cpu_freq()
    output += f"""\nMax Frequency: {cpufreq.max:.2f}Mhz
Min Frequency: {cpufreq.min:.2f}Mhz
Current Frequency: {cpufreq.current:.2f}Mhz
\nCPU Usage Per Core:"""
    for i, percentage in enumerate(psutil.cpu_percent(percpu=True, interval=1)):
        output += f"\n[{str(i+1)}] Core {i}: {percentage}%\n    Total CPU Usage: {psutil.cpu_percent()}%"
    slowprint(output)


def print_mem():
    output = "="*40 + "Memory Information" + "="*40
    svmem = psutil.virtual_memory()
    output += f"\nTotal: {get_size(svmem.total)}"
    output += f"\nAvailable: {get_size(svmem.available)}"
    output += f"\nUsed: {get_size(svmem.used)}"
    output += f"\nPercentage: {svmem.percent}%"
    slowprint(output)


def print_swap():
    output = "="*40 + "SWAP Memory" + "="*40

    swap = psutil.swap_memory()
    output += f"\nTotal: {get_size(swap.total)}"
    output += f"\nFree: {get_size(swap.free)}"
    output += f"\nUsed: {get_size(swap.used)}"
    output += f"\nPercentage: {swap.percent}%"
    slowprint(output)


def print_dsk():
    output = "="*40 + "Disk Information" + "="*40
    output += "\nPartitions and Usage:"
    partitions = psutil.disk_partitions()
    i = 1
    for partition in partitions:
        output += f"\n\n[{i}] Device: {partition.device}:"
        output += f"\n    Mountpoint: {partition.mountpoint}"
        output += f"\n    File system type: {partition.fstype}"
        try:
            partition_usage = psutil.disk_usage(partition.mountpoint)
        except PermissionError:
            continue
        output += f"\n    Total Size: {get_size(partition_usage.total)}"
        output += f"\n    Used: {get_size(partition_usage.used)}"
        output += f"\n    Free: {get_size(partition_usage.free)}"
        output += f"\n    Percentage: {partition_usage.percent}%"
        i += 1
    disk_io = psutil.disk_io_counters()
    output += f"\n\nTotal read: {get_size(disk_io.read_bytes)}"
    output += f"\nTotal write: {get_size(disk_io.write_bytes)}"
    slowprint(output)


def print_net():
    output = "="*40 + "Network Information" + "="*40
    if_addrs = psutil.net_if_addrs()
    i = 1
    for interface_name, interface_addresses in if_addrs.items():
        for address in interface_addresses:
            output += f"\n\n[{i}] Interface: {interface_name}:"
            if str(address.family) == 'AddressFamily.AF_INET':
                output += f"\n    " + (11 + len(interface_name)) * '-'
                output += f"\n    IP Address:    {address.address}\t"
                output += f"\n    Netmask:       {address.netmask}\t"
                output += f"\n    Broadcast IP:  {address.broadcast}\t"
            elif str(address.family) == 'AddressFamily.AF_PACKET':
                output += f"\n    MAC Address:   {address.address}\t"
                output += f"\n    Netmask:       {address.netmask}\t"
                output += f"\n    Broadcast MAC: {address.broadcast}\t"
            else:
                output += f"\n    None."
            i += 1
    net_io = psutil.net_io_counters()
    output += f"\n\nTotal Bytes Sent: {get_size(net_io.bytes_sent)}"
    output += f"\nTotal Bytes Received: {get_size(net_io.bytes_recv)}"
    slowprint(output)


def print_gpu():
    output = "="*40 + "GPU Details" + "="*40
    gpus = GPUtil.getGPUs()
    list_gpus = []
    for gpu in gpus:
        gpu_id = gpu.id
        gpu_name = gpu.name
        gpu_load = f"{gpu.load*100}%"
        gpu_free_memory = f"{gpu.memoryFree}MB"
        gpu_used_memory = f"{gpu.memoryUsed}MB"
        gpu_total_memory = f"{gpu.memoryTotal}MB"
        gpu_temperature = f"{gpu.temperature} °C"
        gpu_uuid = gpu.uuid
        list_gpus.append((
            gpu_id, gpu_name, gpu_load, gpu_free_memory, gpu_used_memory,
            gpu_total_memory, gpu_temperature, gpu_uuid
        ))
    slowprint(output)
    print(tabulate(list_gpus, headers=("id", "name", "load", "free memory", "used memory", "total memory",
                                       "temperature", "uuid")))


if __name__ == "__main__":
    inp = 'h'
    while True:
        inp = input(colored('\nfor help enter h --->', 'blue')).lower()
        if inp == 'h':
            slowprint("""options:
1. enter 'sys' for System Information
2. enter 'bt' for Boot Time
3. enter 'cpu' for CPU Info
4. enter 'mem' for Memory Information
5. enter 'swap' for SWAP Memory
6. enter 'dsk' for Disk Information
7. enter 'net' for Network Information
8. enter 'gpu' for GPU Details""")
        elif inp == 'sys':
            print_sys()
        elif inp == 'bt':
            print_bt()
        elif inp == 'cpu':
            print_cpu()
        elif inp == 'mem':
            print_mem()
        elif inp == 'swap':
            print_swap()
        elif inp == 'dsk':
            print_dsk()
        elif inp == 'net':
            print_net()
        elif inp == 'gpu':
            print_gpu()
        elif inp in ['e', 'q', 'exit', 'quit', 'bye']:
            slowprint('bye bye mate ................')
            exit()
        else:
            slowprint('invalid input!', 'red', isChangeSpeed=True)
