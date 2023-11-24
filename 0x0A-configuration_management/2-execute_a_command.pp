# This Puppet manifest kills a process named killmenow using the exec resource and pkill
class killmenow {
  exec { 'killmenow':
    command => 'pkill killmenow',
    path    => ['/usr/bin'],
  }
}

include killmenow
