def fcfs(processes):
    processes.sort(key=lambda x: x.arrival_time)
    schedule = []
    time = 0
    for p in processes:
        if time < p.arrival_time:
            time = p.arrival_time
        start, finish = time, time + p.burst_time
        schedule.append((p.pid, start, finish))
        time = finish
    return schedule

def sjf(processes):
    remaining = sorted(processes, key=lambda x: (x.arrival_time, x.burst_time))
    schedule = []
    time = 0
    while remaining:
        available = [p for p in remaining if p.arrival_time <= time]
        if not available:
            time = remaining.arrival_time
            continue
        job = min(available, key=lambda x: x.burst_time)
        start = time
        finish = start + job.burst_time
        schedule.append((job.pid, start, finish))
        time = finish
        remaining.remove(job)
    return schedule

def round_robin(processes, quantum):
    queue = processes[:]
    time = 0
    schedule = []
    burst_left = {p.pid: p.burst_time for p in queue}
    while queue:
        p = queue.pop(0)
        exec_time = min(quantum, burst_left[p.pid])
        start, finish = time, time + exec_time
        schedule.append((p.pid, start, finish))
        burst_left[p.pid] -= exec_time
        time = finish
        if burst_left[p.pid] > 0:
            queue.append(p)
    return schedule
