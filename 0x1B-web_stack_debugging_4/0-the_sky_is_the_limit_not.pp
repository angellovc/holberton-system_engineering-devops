# change the nginx limits
exec { 'change the limit':
    path    => '/bin',
    command => "sed -i 's/15/2000/g' /etc/default/nginx"
}

exec { 'restart web server':
    path    => '/etc/init.d',
    command => 'nginx restart'
}
