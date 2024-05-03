#this process to kill the file have been provided
exec { killmenow :
command > '/user/bin/pkill killmenow',
provider > 'shell',
returns > [0, 1],
}
