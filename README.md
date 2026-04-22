# Bot de Telegram en Vercel

Un bot de Telegram desplegado en Vercel que responde "¡Hola!" y envía un mensaje automático cada 30 minutos.

## Requisitos

- Python 3.9+
- Token de bot de Telegram (obtén uno de [@BotFather](https://t.me/BotFather))
- Tu ID de usuario de Telegram (obtén uno de [@userinfobot](https://t.me/userinfobot))
- Cuenta de Vercel
- Cuenta de GitHub

## Instalación Local

### 1. Clonar y configurar el proyecto

```bash
git clone https://github.com/tu-usuario/BotAgente.git
cd BotAgente
```

### 2. Crear archivo `.env`

Copia `.env.example` a `.env` y completa los valores:

```bash
cp .env.example .env
```

Edita `.env` con tus valores:
```
TELEGRAM_BOT_TOKEN=tu_token_del_botfather
TELEGRAM_CHAT_ID=tu_id_de_usuario
WEBHOOK_URL=https://tu-proyecto.vercel.app/api/webhook
```

### 3. Instalar dependencias (opcional para desarrollo local)

```bash
python3 -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
pip install -r requirements.txt
```

## Despliegue en Vercel

### 1. Conectar GitHub a Vercel

- Ve a [vercel.com](https://vercel.com)
- Haz login con GitHub
- Haz clic en "New Project"
- Selecciona tu repositorio de GitHub

### 2. Configurar variables de entorno en Vercel

En el dashboard de Vercel, ve a:
- Settings > Environment Variables

Agrega estas variables:
- `TELEGRAM_BOT_TOKEN`: Tu token del bot
- `TELEGRAM_CHAT_ID`: Tu ID de usuario

### 3. Desplegar

Vercel desplegará automáticamente cuando hagas push a GitHub.

Una vez desplegado, tu URL será algo como:
`https://tu-proyecto.vercel.app`

## Configurar el Webhook de Telegram

Después de desplegar en Vercel, necesitas configurar el webhook. Ejecuta esto en tu terminal:

```bash
curl -X POST https://api.telegram.org/bot{TOKEN}/setWebhook \
  -H "Content-Type: application/json" \
  -d '{"url": "https://tu-proyecto.vercel.app/api/webhook"}'
```

Reemplaza:
- `{TOKEN}` con tu token de bot
- `tu-proyecto.vercel.app` con tu dominio de Vercel

## Configurar el mensaje automático cada 30 minutos

Vercel tiene un límite de 1 invocación por minuto en planes gratuitos para crons. Para solucionar esto, usa **EasyCron** (gratuito):

### 1. Ir a [easycron.com](https://www.easycron.com/)

### 2. Crear un nuevo cron job

- **URL**: `https://tu-proyecto.vercel.app/api/send_message`
- **Cron Expression**: `*/30 * * * *` (cada 30 minutos)
- **Timezone**: Tu zona horaria

### 3. Guardar

¡El bot ahora enviará "¡Hola!" cada 30 minutos!

## Estructura del proyecto

```
BotAgente/
├── api/
│   ├── webhook.py          # Maneja mensajes de Telegram
│   └── send_message.py     # Envía mensajes automáticos
├── .env.example            # Plantilla de variables de entorno
├── .gitignore              # Archivos ignorados por Git
├── requirements.txt        # Dependencias de Python
├── vercel.json             # Configuración de Vercel
└── README.md               # Este archivo
```

## Uso

### Mensajes privados

Simplemente escribe un mensaje al bot en Telegram y responderá "¡Hola!"

### Comando /start

Escribe `/start` para recibir un mensaje de bienvenida.

### Mensaje automático

Cada 30 minutos, el bot te enviará un mensaje de saludo automático.

## Troubleshooting

### El bot no responde

1. Verifica que tu token sea correcto
2. Asegúrate de que el webhook está registrado:
   ```bash
   curl https://api.telegram.org/bot{TOKEN}/getWebhookInfo
   ```

### El webhook falla

1. Revisa los logs en Vercel: Dashboard > Deployments > Logs
2. Verifica que `TELEGRAM_BOT_TOKEN` esté configurado en Vercel

### El mensaje automático no se envía

1. Verifica que `TELEGRAM_CHAT_ID` sea tu ID de usuario (no el nombre de usuario)
2. Comprueba que EasyCron está activado en tu cuenta

## Licencia

MIT

## Soporte

Para problemas, abre un issue en GitHub.
