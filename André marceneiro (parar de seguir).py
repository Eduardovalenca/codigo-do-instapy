from instapy import InstaPy
from instapy import smart_run

session = InstaPy (username ='andre.marceneirooficial',
                 password ='697230794d' ,
                 nogui=True,
                 bypass_security_challenge_using = 'sms')


zx = True
while zx==True:

    with smart_run(session):

        session.set_action_delays(enabled=True,
                           like=0.5,
                           comment=0.5,
                           follow=1,
                           unfollow=2,
                           story=3)

        #Isso irá ignorar todas as contas comerciais que possuem categoria na lista fornecida.
        session.set_skip_users(skip_private=False,
                       skip_no_profile_pic=False,
                       skip_business=True)

        # default enabled = False, segue ~ 10% dos usuários das imagens, times = 1 
	    # (segue um usuário apenas uma vez (se não seguir novamente)) 
        session.set_do_follow(enabled = True, percentage = 100)

        # deixar de seguir, independentemente de um usuário seguir você ou não
        session.unfollow_users(amount=100, allFollowing=True, style="RANDOM", unfollow_after=2*60*60, sleep_delay=0)
        session.unfollow_users(amount=100, allFollowing=True, style="RANDOM", unfollow_after=2*60*60, sleep_delay=0)
        session.unfollow_users(amount=50, allFollowing=True, style="RANDOM", unfollow_after=2*60*60, sleep_delay=0)
        session.unfollow_users(amount=50, allFollowing=True, style="RANDOM", unfollow_after=2*60*60, sleep_delay=0)