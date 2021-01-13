from subprocess import call

while True:
    for x in range(10000, -20, -20):
        call(['python', 'manage.py', 'crawl', '-r', '-m', '20', '-s', '15', '-o', str(x)])
