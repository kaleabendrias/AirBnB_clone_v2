# File: /etc/puppet/manifests/setup_web_static.pp

# Ensure Nginx is installed
package { 'nginx':
  ensure => 'installed',
}

# Create necessary directories
file { '/data':
  ensure => 'directory',
  owner  => 'ubuntu',
  group  => 'ubuntu',
}

file { '/data/web_static':
  ensure => 'directory',
  owner  => 'ubuntu',
  group  => 'ubuntu',
}

file { '/data/web_static/releases':
  ensure => 'directory',
  owner  => 'ubuntu',
  group  => 'ubuntu',
}

file { '/data/web_static/shared':
  ensure => 'directory',
  owner  => 'ubuntu',
  group  => 'ubuntu',
}

file { '/data/web_static/releases/test':
  ensure => 'directory',
  owner  => 'ubuntu',
  group  => 'ubuntu',
}

# Create the index.html file
file { '/data/web_static/releases/test/index.html':
  ensure  => 'file',
  owner   => 'ubuntu',
  group   => 'ubuntu',
  content => '<html><head></head><body>Holberton School</body></html>',
}

# Create or recreate the symbolic link
file { '/data/web_static/current':
  ensure  => 'link',
  target  => '/data/web_static/releases/test',
  force   => true,
  owner   => 'ubuntu',
  group   => 'ubuntu',
}

# Update Nginx configuration
file { '/etc/nginx/sites-available/default':
  content => template('nginx/default.erb'),
  notify  => Service['nginx'],
}

# Notify Nginx to restart when the configuration is updated
service { 'nginx':
  ensure    => 'running',
  enable    => true,
  subscribe => File['/etc/nginx/sites-available/default'],
}
