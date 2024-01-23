#!/usr/bin/env bash
# Just as you did before, we’d like you to install and configure an Nginx server using Puppet instead of Bash

package { 'nginx':
  ensure => installed,
}

file_line { 'aaaaa':
  ensure => 'present',
  path   => '/etc/nginx/sites-available/default',
  after  => 'listen 80 default_server;',
  line   => 'rewrite ^/redirect_me https://youtube.com/shorts/qrt7PMcsQms?si=JkPXx59ExZDm7en1;',
}

file { '/var/www/html/index.html':
  content => 'Hello World!',
}

service { 'nginx':
  ensure  => running,
  require => Package['nginx'],
}
