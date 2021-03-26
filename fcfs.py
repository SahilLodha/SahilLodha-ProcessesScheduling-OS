from main import Process
import sys

processes = []
while True:
    temp = Process()
    processes.append(temp)
    flag = str(input('Want to continue[Y/N]: ')).lower()
    if flag == 'n':
        break

print("The entered Information is provided below:")
for proc in processes:
    print(proc)
    print("<--------- Next --------->")

flag = input("Is it correct [Y/N]: ").lower()
if flag == 'n':
    sys.exit("Wrong Input!")

print("\n<--------------- Implementing FCFS --------------->\n")
processes = Process.sort_processes(processes, 'arrivalTime')
end_time_last = 0

for proc in processes:
    if proc.arrivalTime >= end_time_last:
        proc.waitingTime = 0
        proc.startTime = proc.arrivalTime
        proc.endTime = proc.arrivalTime + proc.burstTime
    else:
        proc.waitingTime = end_time_last - proc.arrivalTime
        proc.endTime = end_time_last + proc.burstTime
        proc.startTime = end_time_last

    end_time_last = proc.endTime
    proc.leftovers = 0

for proc in processes:
    print(proc)
    print(f"Start Time: {proc.startTime}")
    print("<--------- Next --------->")

print(f'Hence the average waiting time is {Process.avg_waiting_time_FCFS(processes):.2f}')
print(f'The CPU Utilization is {sum([proc.burstTime for proc in processes])/processes[-1].endTime:.4f}')
print(f"The turn around time is {sum(proc.endTime - proc.startTime for proc in processes)/len(processes)}")