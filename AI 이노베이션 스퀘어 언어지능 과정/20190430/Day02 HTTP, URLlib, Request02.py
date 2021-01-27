from builtwith import builtwith
from whois import whois
from urllib import robotparser

print(builtwith('https://wordpress.com'))
print(builtwith('https://webscraping.com'))
print(builtwith('https://jquery.com'))
print(builtwith('https://joomla.com'))

print(whois('https://ko.wordpress.com/'))
print(whois('https://webscraping.com'))
print(whois('https://jquery.com'))
print(whois('https://joomla.com'))

robot = robotparser.RobotFileParser()
robot.set_url('https://www.google.com/robots.txt')
print(robot.read())
print(robot.can_fetch('AgentName', 'https://www.google.com'))