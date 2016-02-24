#!/usr/bin/env python
import click
import subprocess
import shlex

@click.command()
@click.argument('inputlhe')
@click.argument('outputhepmc')
@click.option('-e','--events', default = 10000)
def runmadgraph(inputlhe,outputhepmc,events):
    runcardtmpl = 'pythia.tmpl'
    runcardname = 'pythiasteer.dat'
    with open(runcardtmpl) as template:
        with open(runcardname,'w') as filled:
            filled.write(template.read().format(LHEF    = inputlhe,
                                                NEVTS   = events
                                                ))
    subprocess.check_call(shlex.split('./example_main {} {}'.format(runcardname,outputhepmc)))

if __name__ == '__main__':
    runmadgraph()
