from invoke import task, run

@task
def build(c):
    run("nosetests --detailed-errors")