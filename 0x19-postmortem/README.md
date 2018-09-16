Postmortem for Holberton Project
Below is a postmortem for a webstack debugging assignment for Holberton School. A simple website utilizing was returning a 500 status code to any GET requests. Students were tasked with identifying the problem and creating a Puppet script for the solution.

#Summary:
Apache server was returning a 500 error for all GET requests. The website consists of one HTML page so problem with MySQL or PHP was identified as the likely culprit.

#Timeline:
9–11–2018, 12:00 AM PDT: Project release
9–12–2018, 1:00 PM PDT: Begin project. First check for error logs.
9–12–2018, 1:20 PM PDT: Find that error logging for PHP was disabled. Error logging re-enabled, server restarted, ‘no such file’ error found.
9–12–2018, 1:45 PM PDT: Typographical error found in PHP file. Manually fix. Server restarted. Request returns 200 status code.
9–12–2018, 2:30 PM PDT: Puppet script begun and testing for proper fix begin
9–12–2018, 4:00 PM PDT: Puppet script finished and able to be deployed across all servers. Script pushed to GitHub

#Impact:
Users unable to access website from at least midnight 9–11–2018 to 4:00 PM 9–12–2018. All servers affected by outage.

#Root Cause:
Root cause of problem was a typogrpahical error for file name at line 137 of the file /var/www/html/wp-settings.php. Line read: require_once( ABSPATH . WPINC . ‘/class-wp-locale.phpp’ );
Extension for file should have been ‘.php’
Error likely caused by human error in updated settings and subsequent lack of testing to ensure server was still functional.

#Solution:
Upon finding of error, a manual fix on one server was first completed to ensure the fix would work. A puppet file was then created to distribute across all servers.

#Prevention:
Error could have been easily prevented from user who updated config file to test that the server was still functional before exiting. In addition, debugging should not have been turned off for PHP files. The fix was quite obvious when error logging was turned back on. Testing procedures must be more strcitly enforced for production environments in future situations as well as more stringent monitoring and protection of who has access to write to config files.