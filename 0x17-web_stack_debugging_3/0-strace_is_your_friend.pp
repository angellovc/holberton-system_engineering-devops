#Fix server apache error 500
exec { 'change phpp words to php':
  command => "sed -i 's/phpp/php/' /var/www/html/wp-settings.php",
  path    => "/bin/",
}
