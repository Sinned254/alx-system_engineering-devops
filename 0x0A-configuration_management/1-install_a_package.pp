# This Puppet manifest installs Flask version 2.1.0 from pip3
class flask_installation {
  package { 'python3-pip':
    ensure => installed,
  }

  exec { 'install flask':
    command => 'pip3 install Flask==2.1.0',
    path    => ['/usr/bin'],
    unless  => 'pip3 show Flask | grep -q "Version: 2.1.0"',
  }
}

include flask_installation
