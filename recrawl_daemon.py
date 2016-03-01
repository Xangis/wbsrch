from subprocess import call

while True:
    for x in range(100000, 0, -20):
        call(['python', 'manage.py', 'crawl', '-r', '-m', '20', '-s', '5', '-o', str(x)])
