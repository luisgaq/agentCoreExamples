# AgentCore Examples

Este repositorio contiene ejemplos de agentes usando OpenAI Agents SDK y AWS Bedrock AgentCore.

## Estructura del Proyecto

```
agentcore/
├── example1/          # Agente standalone con OpenAI SDK
├── example2/          # Agente desplegado en AWS Bedrock AgentCore
└── README.md
```

---

## Example 1: OpenAI Agents SDK Standalone

Agente que usa OpenAI Agents SDK para crear un vector store y responder preguntas basadas en datos de Star Trek.

### Archivos
- `CreateOpenAIVectorStore.py` - Crea un vector store en OpenAI con los datos
- `Data_Agent_SDK_Standalone.py` - Agente que responde preguntas usando el vector store
- `data_lines.txt` - Datos de dialogos de Star Trek
- `requirements.txt` - Dependencias

### Ejecucion
```bash
cd example1
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# Primero crear el vector store
python CreateOpenAIVectorStore.py

# Luego ejecutar el agente
python Data_Agent_SDK_Standalone.py
```

---

## Example 2: Agente en AWS Bedrock AgentCore

Agente desplegado en AWS Bedrock AgentCore que responde como el personaje Data de Star Trek.

### Archivos
- `data_agent_agentcore.py` - Codigo del agente
- `requirements.txt` - Dependencias
- `instructions.txt` - Instrucciones detalladas de despliegue

### Requisitos Previos
- Python 3.10+
- AWS CLI configurado
- uv instalado (`brew install uv`)

### Permisos IAM Necesarios
El usuario de AWS necesita estas politicas:
- AmazonEC2ContainerRegistryFullAccess
- IAMFullAccess
- CloudWatchLogsFullAccess
- AmazonS3FullAccess
- AWSCodeBuildAdminAccess
- BedrockAgentCoreFullAccess

### Despliegue Rapido

```bash
cd example2

# 1. Crear entorno virtual
python3 -m venv venv
source venv/bin/activate

# 2. Instalar dependencias
pip install -r requirements.txt

# 3. Configurar agente
agentcore configure --entrypoint data_agent_agentcore.py

# 4. Desplegar (con API key)
agentcore deploy --env OPENAI_API_KEY='tu_api_key'

# 5. Invocar
agentcore invoke '{"prompt": "Data, who was Lal?"}'
```

### Comandos Utiles
```bash
agentcore status              # Ver estado del agente
agentcore obs                 # Ver logs/observabilidad
agentcore destroy             # Eliminar recursos
agentcore invoke '{"prompt": "pregunta"}' # Invocar agente
```

---

## Configuracion de Python en macOS

### Problema comun: Multiples versiones de Python
Si tienes problemas con pip instalando en la version incorrecta de Python:

```bash
# En ~/.zshrc, usar alias generico (no ruta absoluta)
alias python='python3'

# NO usar alias para pip - dejarlo sin alias
# Asi el venv puede controlar pip correctamente
```

### Flujo de trabajo con venv
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
# pip ahora usa el del venv automaticamente
```

---

## Notas Importantes

1. **API Keys**: Nunca subir `.env` o `.env.local` al repositorio
2. **Nombres de agente**: No usar guiones (-) en el nombre
3. **Python version**: Usar PYTHON_3_10 para mayor compatibilidad
4. **Credenciales AWS**: Configurar con `aws configure` antes de desplegar
