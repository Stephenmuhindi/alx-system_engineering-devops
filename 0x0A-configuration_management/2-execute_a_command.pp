# Using Puppet, create a manifest that kills
exec { 'pkill killmenow':
  path    => '/usr/bin/',
  command => 'pkill -x killmenow'
}
