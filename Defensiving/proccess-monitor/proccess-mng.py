import psutil
import time
from subprocess import call
from prettytable import PrettyTable


def main():
    while True:

        call('clear')
        print("==============================Process Monitor\
        ======================================")

        #  battery
        battery = psutil.sensors_battery().percent
        print("----Battery Available: %d " % (battery,) + "%")

        #  Network
        print("----Networks----")
        table = PrettyTable(['Network', 'Status', 'Speed'])
        for key in psutil.net_if_stats().keys():
            name = key
            up = "Up" if psutil.net_if_stats()[key].isup else "Down"
            speed = psutil.net_if_stats()[key].speed
            table.add_row([name, up, speed])
        print(table)

        # memory
        print("----Memory----")
        memory_table = PrettyTable(["Total(GB)", "Used(GB)",
                                    "Available(GB)", "Percentage"])
        vm = psutil.virtual_memory()
        memory_table.add_row([
            f'{vm.total / 1e9:.3f}',
            f'{vm.used / 1e9:.3f}',
            f'{vm.available / 1e9:.3f}',
            vm.percent
        ])
        print(memory_table)

        # show top 10 proccesses with cpu usage
        print("----Processes----")
        process_table = PrettyTable(['PID', 'PNAME', 'STATUS',
                                    'CPU', 'NUM THREADS', 'MEMORY(MB)'])

        proc = []
        for pid in psutil.pids()[-200:]:
            try:
                p = psutil.Process(pid)
                p.cpu_percent()
                proc.append(p)

            except Exception as e:
                pass

        # sort
        top = {}
        time.sleep(0.1)
        for p in proc:
            top[p] = p.cpu_percent() / psutil.cpu_count()

        top_list = sorted(top.items(), key=lambda x: x[1])
        top10 = top_list[-10:]
        top10.reverse()

        for p, cpu_percent in top10:

            try:
                with p.oneshot():
                    process_table.add_row([
                        str(p.pid),
                        p.name(),
                        p.status(),
                        f'{cpu_percent:.2f}' + "%",
                        p.num_threads(),
                        f'{p.memory_info().rss / 1e6:.3f}'
                    ])

            except Exception as e:
                pass
        print(process_table)

        time.sleep(2)


if __name__ == '__main__':
    main()
