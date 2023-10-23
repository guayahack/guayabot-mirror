import random

def handle_response(message) -> str:
    p_message = message.lower()

    #if p_message == 'hello':
    #   return 'Hey there!'
    
    #if p_message == 'roll':
    #    return str(random.randint(1, 6))
    
    if p_message == '!quote':
        phrases = ['Steak término full hecho \n -Harold',
                    'Bonyogurt \n -Bliss',
                    'Siempre el enfoque es el entendimiento, siempre. \n -Jayson',
                    'cada quien vive y actúa como su consciencia le permite. \n -Jayson',
                    'las herramientas son solo herramientas de nada te sirve saber cómo clavar puntillas si no sabes dónde clavarlas \n -profe de Mcveight'
                    ]
        return f"`{random.choice(phrases)}`"
