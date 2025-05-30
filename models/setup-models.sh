#!/bin/bash

# Verifica se o Ollama está rodando
if ! curl -s http://localhost:11434 > /dev/null; then
    echo "Ollama não está rodando. Iniciando servidor em segundo plano..."
    ollama serve > /dev/null 2>&1 &
    sleep 3
    
    if curl -s http://localhost:11434 > /dev/null; then
        echo "✅ Ollama iniciado com sucesso (PID: $!)"
    else
        echo "❌ Falha ao iniciar Ollama"
        exit 1
    fi
else
    echo "✓ Ollama já está rodando"
fi

# Funções de saída colorida
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m'

success() {
    echo -e "${GREEN}✓ $1${NC}"
}

error() {
    echo -e "${RED}✗ $1${NC}"
    exit 1
}

progress() {
    echo -e "${YELLOW}➜ $1...${NC}"
}

# Lista de modelos para baixar
model_list="mistral phi3"

# Baixa cada modelo
for model in $model_list; do
    progress "Baixando modelo $model"
    
    # Versão simplificada sem subshell complexa
    download_output=$(ollama pull "$model" 2>&1)
    status=$?
    
    if [ $status -eq 0 ]; then
        success "$model baixado com sucesso!"
    else
        error "Falha ao baixar $model: $download_output"
    fi
done

success "Todos os modelos foram baixados com sucesso!"
echo -e "\nModelos disponíveis:"
ollama list