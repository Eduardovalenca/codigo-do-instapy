from instapy import InstaPy
from instapy import smart_run

session = InstaPy(username='kyoto_sushi_pe', password='83470284')

with smart_run(session):
	
	#Isso irá ignorar todas as contas comerciais que possuem categoria na lista fornecida.
	session.set_skip_users(skip_private=False,
                       skip_no_profile_pic=True,
                       skip_business=True,
                       skip_business_categories=['Creators & Celebrities'])

	#Irá ignorar os usuários que possuem conta privada, mesmo se forem seguidos por conta em execução
	session.set_skip_users ( skip_private = False ,
                        private_percentage = 0 )

	# default enabled = False, segue ~ 10% dos usuários das imagens, times = 1 
	# (segue um usuário apenas uma vez (se não seguir novamente)) 
	session.set_do_follow(enabled = True,
						 percentage = 100)
	
	# So curti 94 porcentos dos perfils que entrar
	session.set_do_like(enabled = True,
						 percentage= 94)
	
	# deixar de seguir, independentemente de um usuário seguir você ou não
	session.unfollow_users(amount=40, allFollowing=True,
						   style="RANDOM", unfollow_after=60*60, sleep_delay=0)
	
	# Segue os seguidores de cada usuário
	# Os nomes de usuário podem ser uma lista ou uma string
	# O valor é para cada conta, neste caso 30 usuários serão acompanhados
	# Se randomize for false, ele escolherá de cima para baixo
	session.follow_user_followers(['realsushioficial'], amount=300,
									 randomize=True, sleep_delay=0)
	
	# default sleep_delay = 600 (10min) para cada 10 usuários seguindo, neste caso
	# dormir por 60 segundos
	session.follow_user_following(['realsushioficial'], amount=300,
									 randomize=True, sleep_delay=0)
	
	# Para 50% das 30 novas seguidas, vá para o perfil delas 
	# e escolha 5 fotos aleatoriamente para gostar. 
	# Leve em consideração as outras opções definidas, como a taxa de comentários 
	# e a filtragem por palavras inadequadas ou 
	session.set_user_interact(amount=5, randomize=True, percentage=50, media='Photo')
	session.follow_user_followers(['friend1', 'friend2', 'friend3'], amount=10, randomize=False, interact=True)

	session.join_pods()