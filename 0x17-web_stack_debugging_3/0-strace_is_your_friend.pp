# Fix a 500 request error
exec {'replace':
      provider =>shell,
      command  => 'sed -i "s/phpp/php/g" /var/www/html/wp-settings.php'
}
