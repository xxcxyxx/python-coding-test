import heapq


def solution(jobs):
    jobs.sort()

    heap = []
    current_time = 0
    total_time = 0
    index = 0
    count = 0
    job_count = len(jobs)

    while count < job_count:
        while index < job_count and jobs[index][0] <= current_time:
            request_time, duration = jobs[index]
            heapq.heappush(heap, (duration, request_time))
            index += 1

        if heap:
            duration, request_time = heapq.heappop(heap)
            current_time += duration
            total_time += current_time - request_time
            count += 1
        else:
            current_time = jobs[index][0]

    return total_time // job_count
