from fabric.api import env, local, run, put, get, cd
import datetime

#env.hosts = ['jchampion@wbsrch.com:722']
env.hosts = ['xangis@216.151.17.10:722']
deployhosts = ['xangis@216.151.17.10:722', 'xangis@216.151.17.11:722', 'xangis@216.151.17.12:722']
code_dir = '/var/django/'
app_name = 'wbsrch'
db_name = 'zetaweb'
init_name = 'wbsrch'
model_dir = 'dir'

def test():
    local("./manage.py test")

def pack():
    local('tar cvzf /tmp/django-' + app_name + '.tgz . --exclude=top-1m.csv --exclude=env --exclude=urls --exclude=crawler --exclude=log --exclude=test_logs --exclude=*.log --exclude=*.out --exclude=.git --exclude=top-1m* --exclude=alexatmp --exclude=wordlists --exclude=other_stopwords')

def push():
    env.hosts = deployhosts
    pack()
    put('/tmp/django-' + app_name + '.tgz', '/tmp/')
    with cd(code_dir + app_name):
        run('tar xzf /tmp/django-' + app_name +'.tgz')
        run('rm /tmp/django-' + app_name + '.tgz')
    local('rm /tmp/django-' + app_name + '.tgz')
    local('echo Code deployed. You will need to perform database migrations and restart the service yourself.')

def getdb():
    run('sudo -u postgres pg_dump ' + db_name + ' > /tmp/' + db_name + '.sql')
    get('/tmp/' + db_name + '.sql', './' + db_name + '.sql')
    run('rm /tmp/' + db_name + '.sql')
    local('./manage.py reset ' + model_dir)
    local('sudo -u postgres psql ' + db_name + ' < ' + db_name + '.sql')

def getcode():
    local('mkdir -p ../bak')
    local('tar czf ../bak/' + app_name + '_' + str(datetime.date.today()) + '.tgz . --exclude=*.log --exclude=*.out --exclude=.git --exclude=top-1m* --exclude=urls --exclude=env')
    with cd(code_dir + app_name + '/'):
        run('tar czf /tmp/django-' + app_name + '.tgz . --exclude=top-1m.csv --exclude=env --exclude=urls --exclude=crawler --exclude=log --exclude=test_logs --exclude=*.log --exclude=*.out --exclude=x* --exclude=*.txt --exclude=alexatmp')
    get('/tmp/django-' + app_name + '.tgz', './django-' + app_name + '.tgz')
    run('rm /tmp/django-' + app_name + '.tgz')
    local('tar xzf ./django-' + app_name + '.tgz')
    local('rm ./django-' + app_name + '.tgz')
