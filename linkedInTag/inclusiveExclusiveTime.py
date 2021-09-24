class Solution:
    def inclusiveExclusiveTime(self, jobs, func_id):
        child_id = ""
        child_start = -1
        total_children_time = 0
        start_time = -1
        job_started = False
        res = [0, 0]

        for job in jobs:
            job = job.split(',')
            job_id, job_name, time = job[0], job[1], job[2]
            if job_id == func_id:
                if job_name == 'START':
                    start_time = int(time)
                    job_started = True
                else:
                    res[0] = int(time) - start_time
                    res[1] = res[0] - total_children_time
                    return res
            else:
                if job_started:
                    if job_id == child_id:
                        total_children_time += int(time) - child_start
                        child_id = ""
                        child_start = -1
                    elif child_id == "":
                        child_id = job_id
                        child_start = int(time)
        return res

res = Solution().inclusiveExclusiveTime(["abc,START,100","def,START,150","def,END,180","abc,END,200"], 'abc')
print(res)