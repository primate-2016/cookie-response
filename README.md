# cookie-response

Put the contents of the userdata file in the userdata of an AL2, kernel 5.x, EC2 instance.
Open SG on port 8443 to the world

https://x.x.x.x:8443/slot0 will set a cookie called release_slot with a value of slot0. <br>
slot0 to 3 will set release_slot cookie with relevant slot value

https://x.x.x.x:8443/getcookie will return the cookie that has been set - it will match the previously visited path above


