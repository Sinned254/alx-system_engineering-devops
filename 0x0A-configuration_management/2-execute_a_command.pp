# This Puppet manifest kills a process named 
# killmenow using the exec resource and pkill
  exec { 'kill_process':
    command => 'pkill -f killmenow',
    provide => 'shell'
    path    => ['/usr/bin', '/usr/sbin'],
  }
