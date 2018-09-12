# change phpp to php
exec { 'replace':
  command => '/bin/sed -ie \'s/class-wp-locale.phpp/class-wp-locale.php/\' /var/www/html/wp-settings.php'
}

exec { 'restart':
  command    => '/etc/init.d/apache2 restart'
}
