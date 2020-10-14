# changing the security limits
exec { 'change the hard hard limit':
  path    => '/bin/',
  command => 'sed -i "s/holberton hard nofile 5/holberton hard nofile 1024/" /etc/security/limits.conf',
}

exec { 'change the soft limits':
  path    => '/bin/',
  command => 'sed -i "s/holberton soft nofile 4/holberton soft nofile 1024/" /etc/security/limits.conf',
}
