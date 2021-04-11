from crontab import CronTab

cron = CronTab(user=True)
job = cron.new(command="python3 grabData.py")
job.setall("0 0 1 * *")

if cron[0].is_valid:
    cron.write()
    print("Job Created")