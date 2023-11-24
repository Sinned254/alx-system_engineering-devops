# This Puppet manifest installs Flask version 2.1.0 from pip3
# Installs 'flask' from 'pip3' using puppet
package{'flask':
  ensure   => '2.1.0',
  provider => 'pip3'
}
