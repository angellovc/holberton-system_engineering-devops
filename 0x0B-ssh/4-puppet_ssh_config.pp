# make changes to ssh configuration file

file_line { 'IdentityFile':
    ensure => present,
    path   => '/etc/ssh/ssh_config',
    match  => '^IdentityFile',
    line   => 'IdentityFile ~/.ssh/holberton_ssh',
}

file_line { 'PasswordAuthentication':
    ensure => present,
    path   => '/etc/ssh/ssh_config',
    match  => '^PasswordAuthentication',
    line   => 'PasswordAuthentication no',
}