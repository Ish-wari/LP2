n=int(input("enter the number of jobs"))
jobs=[]
for i in range(n):
    print("enter job details for job",i+1)
    job_id=input("enetr job_id")
    job_deadline=int(input("enter deadline"))
    job_profit=int(input("enetr profit"))
    jobs.append([job_id,job_deadline,job_profit])
jobs.sort(key=lambda x:x[2],reverse=True)
print("Jobs after sorting")
print(jobs)
max_deadline=0
total_profit=0
for job in  (jobs):
    if job[1]>max_deadline:
        max_deadline=job[1]
slots=[-1]* max_deadline
for job in jobs:
    job_id=job[0]
    job_deadline=job[1]
    job_profit=job[2]
    for i in range(job_deadline-1,-1,-1):
        if slots[i]==-1:
            slots[i]=job_id
            total_profit+=job_profit
            break
print("Final Scehduled jobs")
for job in slots:
    if job!=-1:
        print(job)
print("total Profit: ",total_profit)

# 1 enter jobs
# 2 jobs=[]
# 3 enter the details of job for i+1
# 4 sort in desc order  jobs.sort(key=lambda x:x[2],reverse=True)
# max deadline and profit =0
# 5 maxdealind comapre with job[1]
# 6 make slots 
# revrse tracking of slots  for i in range(job_deadline-1,-1,-1):
#     then fill the job in empty slots
# 7 final jobs 
# for job in slots:
#     if job!=-1:
#         print(job)