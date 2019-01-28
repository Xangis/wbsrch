from subprocess import call

while True:
    for x in range(10000, 0, -20):
        call(['python', 'manage.py', 'crawl', '-r', '-m', '20', '-s', '60', '-o', str(x)])
