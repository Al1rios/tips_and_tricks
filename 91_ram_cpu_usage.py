
import psutil

memory = psutil.virtual_memory()


def ram_usage():
    print(f'Total available memory in gigabytes'
          f'{memory.total/(1024**3):.3f}')
    print(f'Total use memory in gigabytes'
          f'{memory.used/(1024**3):.3f}')
    print(f'Percentage of memory under use:'
          f'{memory.percent} %')
    
print(ram_usage())

cpu_core = psutil.cpu_percent(percpu=True)

for cpu, usage in enumerate(cpu_core):
    print(f'{cpu+1} cpu:{usage}%')

