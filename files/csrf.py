ó
˙c           @   sa   e  Z e r# d  d  Z   Z n  d d l Z d d l Z d d l Z d Z d   Z e   d S(   i    i˙˙˙˙NsĆ   [1;94m
    _   __    _       ____________
   / | / /   | |     / / ____/ __ )
  /  |/ /____| | /| / / __/ / __  |
 / /|  /_____/ |/ |/ / /___/ /_/ /
/_/ |_/      |__/|__/_____/_____/[1;31m(Pentesting)

Created By : [1;96mNabil-Rahman |[1;0m [V 1.2.2]

[1;32m------------------------------------------
[93m AUTHOR  : Team DarkWeb T-D
[93m GITHUB  : github.com/Nabil-Official
[93m FB      : nabil.404
[1;32m--------------------------------------
c          C   sś   t  j d  t GHHt d  }  |  d k r3 d GHn Hd |  GHd GHt j d  d GHyO t  j d	 |  d
  } | GHd GHHt d  } H| d k r˘ t  j d  n  Wn d GHn Xd  S(   Nt   clears,   [1;31m>> [1;32mEnter Domain Name : [1;35mt    s!   [1;31m[+] Enter A Domain To Scans/      [1;31m[+] [1;32mTARGET   [1;31m>> [1;33ms;      [1;31m[+] [1;32mSCANNING [1;31m>> [1;33mStarting....i   s   [1;32ms!   nmap -p80 --script http-csrf.nse s    | grep '|_http-csrf:'s/     [1;31m<<< [1;33mThanks For Using [1;31m>>>s8   [1;31m[+] [1;34mPRESS ENTER TO GO BACK MENU [1;31m[+]s   cd .. && python2 n-web.pys"   [1;31m[+] Something Went Wrong ! (   t   ost   systemt   logot	   raw_inputt   timet   sleep(   t   domaint   out_putt   user(    (    s   csrf.pyt   main   s,    	(   t   Falset   foot   barR   t   sysR   R   R   (    (    (    s   csrf.pyt   <module>   s   
	