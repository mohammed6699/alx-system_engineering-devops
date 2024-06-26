# increase Limit to default
exec { 'fix -- for-nginx':
	# modify the ulimit value
	# not n value is 4096
	command => '/bin/sed -i "s/4096/4096" /etc/default/nginx',
	# specify path for sed command
	path	=> '/usr/local/bin/:/bin/',
}
# Restart nginx
exec {'nginx-restart':
	# restart nginx
	command => '/etc/init.d/nginx restart',
	# specify path for init.d
	path	=> '/etc/init.d',
}
