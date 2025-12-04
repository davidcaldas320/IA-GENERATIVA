import google.generativeai as genai
from dotenv import load_dotenv  # Para carregar a chave de um arquivo seguro (.env)
import os                       # Para acessar a variável de ambiente

# 1. CARREGA AS VARIÁVEIS DE AMBIENTE (do arquivo .env)
load_dotenv() 

# 2. CONFIGURA COM A CHAVE OBTIDA DE FORMA SEGURA
# Sua chave agora está escondida e não mais embutida no código
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# 3. INICIA O MODELO
model = genai.GenerativeModel("gemini-2.5-flash")

# 4. INICIA A SESSÃO DE CHAT PARA MANTER O HISTÓRICO
chat = model.start_chat()

print("=== Agente IA Generativa (Python) ===")
print("Digite 'sair' para encerrar, ou 'historico' para ver a conversa.\n")

while True:
    user_input = input("Você: ")

    if user_input.lower() == "sair":
        print("Encerrando o agente. Até mais!")
        break
    
    # NOVO COMANDO: VISUALIZAR O HISTÓRICO
    if user_input.lower() == "historico":
        print("\n--- HISTÓRICO DE CONVERSA ---\n")
        # Itera sobre todas as mensagens que o agente "lembrou"
        for message in chat.get_history():
            print(f'[{message.role.capitalize()}]: {message.text}')
        print("\n---------------------------\n")
        continue 

    # 5. ENVIA A MENSAGEM VIA OBJETO CHAT (mantendo o contexto)
    try:
        response = chat.send_message(user_input)
        print("Agente:", response.text, "\n")
    except Exception as e:
        print(f"Erro ao gerar conteúdo: {e}")
        print("Por favor, tente novamente ou verifique sua chave/conexão.")