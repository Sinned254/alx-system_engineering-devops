# Puppet Manifest: Create a file in /tmp/school
# File path: /tmp/school
# File permission: 0744
# File owner: www-data
# File group: www-data
# File content: I love Puppet

file { '/tmp/school':
  ensure   => file,
  path     => '/tmp/school'
  mode     => '0744',
  owner    => 'www-data',
  group    => 'www-data',
  content  => 'I love Puppet',
}
